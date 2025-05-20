import json
import os
from datetime import datetime, timedelta

from tabulate import tabulate

dataDir = "data"
dataFile = os.path.join(dataDir, "gastos.json")

def cargarGastos():
    ### Carga los gastos desde el archivo json
    if not os.path.exists(dataDir):
        os.makedirs(dataDir)
    try:
        with open(dataFile, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: El archivo de gastos está corrupto. Se iniciará como una lista vaciá.")
        return[]
    
def guardarGastos(gastos):
    ### Guarda los gastos en el archivo json
    with open(dataFile, 'w') as f:
        json.dump(gastos, f, indent=4)

def registrarGasto(gastos, cantidad, categoria, descripcion):
    ### Registra un nuevo gasto con los datos proporcionados
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nuevoGasto = {
        "fecha": fecha,
        "categoria": categoria,
        "cantidad": cantidad,
        "descripcion": descripcion
    }
    gastos.append(nuevoGasto)
    guardarGastos(gastos)
    print("Gasto registrado exitosamente.")
    return gastos

def listarGastos(gastos, filtroCategoria=None, filtroFechaInicio=None, filtroFechaFin=None):
    ### Muestra los gastos registrados, con opciones de filtrado
    gastosFiltrados = gastos
    if filtroCategoria:
        gastosFiltrados = [gasto for gasto in gastosFiltrados if gasto['categoria'].lower() == filtroCategoria.lower()]
    if filtroFechaInicio:
        try:
            fechaInicio = datetime.strptime(filtroFechaInicio, "%Y-%m-%d")
            gastosFiltrados = [gasto for gasto in gastosFiltrados if datetime.strptime(gasto['fecha'].split()[0], "%Y-%m-%d") >= fechaInicio]
        except ValueError:
            print("Formato de fecha de inicio inválido (YYYY-MM-DD).")
            return
    if filtroFechaFin:
        try:
            fechaFin = datetime.strptime(filtroFechaFin, "%Y-%m-%d")
            gastosFiltrados = [gasto for gasto in gastosFiltrados if datetime.strptime(gasto['fecha'].split()[0], "%Y-%m-%d") <= fechaFin]
        except ValueError:
            print("Formato de fecha de fin inválido (YYYY-MM-DD).")
            return
    if gastosFiltrados:
        headers = ["Fecha", "Categoría", "Cantidad", "Descripción"]
        tablaGastos = [[gasto['fecha'], gasto['categoria'], f"${gasto['cantidad']:.2f}", gasto['descripcion']] for gasto in gastosFiltrados]
        print(tabulate(tablaGastos, headers=headers, tablefmt="grid"))
    else:
        print("No se encontraron gastos según los criterios de búsqueda.")

def getSemanaAño(fechaStr):
    ### Obtiene el año y el número de semana ISO de una fecha
    fechaDt = datetime.strptime(fechaStr.split()[0], "%Y-%m-%d")
    return fechaDt.isocalendar()[0], fechaDt.isocalendar()[1]

def calcularTotales(gastos, periodo='diario'):
    ### Calcula los gastos totales diarios, semanales o mensuales
    if not gastos:
        return "No hay gastos registrados."
    
    totales = {}
    if periodo == 'diario':
        for gasto in gastos:
            fecha = gasto['fecha'].split()[0]
            totales[fecha] = totales.get(fecha, 0) + gasto['cantidad']
    elif periodo == 'semanal':
        for gasto in gastos:
            año, semana = getSemanaAño(gasto['fecha'])
            claveSemana = f"{año}-Semana {semana}"
            totales[claveSemana] = totales.get(claveSemana, 0) + gasto['cantidad']
    elif periodo == 'mensual':
        for gasto in gastos:
            fecha = gasto['fecha'][:7]  # YYYY-MM
            totales[fecha] = totales.get(fecha, 0) + gasto['cantidad']
    else:
        return "Periodo inválido. Use 'diario', 'semanal' o 'mensual'."

    return totales

def calcularPorCategoria(gastos, periodo='total'):
    ### Calcula el gasto acumulado por categoría
    if not gastos:
        return "No hay gastos registrados."

    gastosPorCategoria = {}
    for gasto in gastos:
        categoria = gasto['categoria']
        gastosPorCategoria[categoria] = gastosPorCategoria.get(categoria, 0) + gasto['cantidad']

    return gastosPorCategoria

### Inicializar la lista de gastos al cargar el módulo
gastosRegistrados = cargarGastos()
