import json
from datetime import datetime, timedelta
from tabulate import tabulate

archivoGastos = 'gastos.json'

def cargarGastos():
    try:
        with open(archivoGastos, 'r', encoding='utf-8') as f:
            contenido = f.read()
            if contenido:
                return json.loads(contenido)
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def guardarGastos(gastos):
    with open(archivoGastos, 'w', encoding='utf-8') as f:
        json.dump(gastos, f, indent=4)

def registrarGasto():
    print("=============================================")
    print("            Registrar Nuevo Gasto            ")
    print("=============================================")
    print("\nIngrese la información del gasto:")

    montoValido = False
    while not montoValido:
        montoStr = input("\n- Monto del gasto: ")
        esNumero = True
        for caracter in montoStr:
            if not (caracter.isdigit() or caracter == '.'):
                esNumero = False
                break
        if esNumero and montoStr:
            montoGasto = float(montoStr)
            if montoGasto <= 0:
                print("El monto debe ser un número positivo.")
            else:
                montoValido = True
        else:
            print("Entrada inválida. Por favor, ingrese un número para el monto.")

    categoriaGasto = input("- Categoría (ej. comida, transporte, entretenimiento, otros): ").lower()
    descripcionGasto = input("- Descripción (opcional): ")

    confirmacion = input("Ingrese 'S' para guardar o 'C' para cancelar. ").upper()
    if confirmacion == 'S':
        fechaGasto = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nuevoGasto = {
            "monto": montoGasto,
            "categoria": categoriaGasto,
            "descripcion": descripcionGasto,
            "fecha": fechaGasto
        }
        gastosActuales = cargarGastos()
        gastosActuales.append(nuevoGasto)
        guardarGastos(gastosActuales)
        print("\n¡Gasto registrado con éxito!")
        
    else:
        print("\nRegistro de gasto cancelado.")

def listarGastos(filtroCategoria=None, filtroRangoFechas=None):
    gastos = cargarGastos()
    if not gastos:
        print("\nNo hay gastos registrados todavía.")
        return

    print("=============================================")
    print("                Listado de Gastos            ")
    print("=============================================")

    gastosAMostrar = []

    for gasto in gastos:
        mostrar = True
        if filtroCategoria and gasto['categoria'] != filtroCategoria.lower():
            mostrar = False
        if filtroRangoFechas and mostrar:
            fechaStr = gasto['fecha'].split(' ')[0]
            fechaGasto = datetime.strptime(fechaStr, "%Y-%m-%d").date()
            hoy = datetime.now().date()
            if filtroRangoFechas == 'diario':
                if fechaGasto != hoy:
                    mostrar = False
            elif filtroRangoFechas == 'semanal':
                haceUnaSemana = hoy - timedelta(days=7)
                if not (haceUnaSemana <= fechaGasto <= hoy):
                    mostrar = False
            elif filtroRangoFechas == 'mensual':
                if fechaGasto.month != hoy.month or fechaGasto.year != hoy.year:
                    mostrar = False
        if mostrar:
            gastosAMostrar.append([
                gasto['fecha'],
                gasto['categoria'].capitalize(),
                f"{gasto['monto']:.2f}",
                gasto['descripcion'] if gasto['descripcion'] else "N/A"
            ])

    if not gastosAMostrar:
        print("No se encontraron gastos con los filtros aplicados.")
        return

    print(tabulate(gastosAMostrar, headers=["Fecha", "Categoría", "Monto", "Descripción"], tablefmt="grid"))

def calcularGastos(periodoCalculo=None):
    gastos = cargarGastos()
    if not gastos:
        print("No hay gastos registrados para calcular.")
        return

    print("=============================================")
    print("          Cálculo Total de Gastos          ")
    print("=============================================")

    totalGeneral = 0
    gastosPorCategoria = {}
    gastosFiltradosPorPeriodo = []

    hoy = datetime.now().date()

    for gasto in gastos:
        fechaStr = gasto['fecha'].split(' ')[0]
        fechaGasto = datetime.strptime(fechaStr, "%Y-%m-%d").date()
        incluirGasto = True

        if periodoCalculo == 'diario':
            if fechaGasto != hoy:
                incluirGasto = False
        elif periodoCalculo == 'semanal':
            haceUnaSemana = hoy - timedelta(days=7)
            if not (haceUnaSemana <= fechaGasto <= hoy):
                incluirGasto = False
        elif periodoCalculo == 'mensual':
            if fechaGasto.month != hoy.month or fechaGasto.year != hoy.year:
                incluirGasto = False

        if incluirGasto:
            gastosFiltradosPorPeriodo.append(gasto)
            totalGeneral += gasto['monto']
            categoria = gasto['categoria'].capitalize()
            gastosPorCategoria[categoria] = gastosPorCategoria.get(categoria, 0) + gasto['monto']

    if not gastosFiltradosPorPeriodo:
        print(f"No hay gastos registrados para el periodo '{periodoCalculo}'.")
        return

    print(f"Total general de gastos para el periodo: ${totalGeneral:.2f}")

    print("Gastos por categoría en el periodo:")
    datosTablaCategorias = []
    for categoria, total in gastosPorCategoria.items():
        datosTablaCategorias.append([categoria, f"${total:.2f}"])

    print(tabulate(datosTablaCategorias, headers=["Categoría", "Total"], tablefmt="grid"))

def generarReporte(tipoReporte=None):
    gastos = cargarGastos()
    if not gastos:
        print("No hay gastos registrados para generar un reporte.")
        return

    print("=============================================")
    print("           Generar Reporte de Gastos         ")
    print("=============================================")

    totalGeneral = 0
    gastosPorCategoria = {}
    gastosPorDia = {}
    gastosFiltradosPorPeriodo = []

    hoy = datetime.now().date()

    for gasto in gastos:
        fechaStr = gasto['fecha'].split(' ')[0]
        fechaGasto = datetime.strptime(fechaStr, "%Y-%m-%d").date()
        incluirGasto = True

        if tipoReporte == 'diario':
            if fechaGasto != hoy:
                incluirGasto = False
        elif tipoReporte == 'semanal':
            haceUnaSemana = hoy - timedelta(days=7)
            if not (haceUnaSemana <= fechaGasto <= hoy):
                incluirGasto = False
        elif tipoReporte == 'mensual':
            if fechaGasto.month != hoy.month or fechaGasto.year != hoy.year:
                incluirGasto = False

        if incluirGasto:
            gastosFiltradosPorPeriodo.append(gasto)
            totalGeneral += gasto['monto']
            categoria = gasto['categoria'].capitalize()
            gastosPorCategoria[categoria] = gastosPorCategoria.get(categoria, 0) + gasto['monto']
            fechaCorta = gasto['fecha'].split(' ')[0]
            gastosPorDia[fechaCorta] = gastosPorDia.get(fechaCorta, 0) + gasto['monto']

    if not gastosFiltradosPorPeriodo:
        print(f"No hay gastos registrados para el reporte '{tipoReporte}'.")
        return

    reporteTexto = f"--- REPORTE DE GASTOS ({tipoReporte.upper() if tipoReporte else 'GLOBAL'}) ---\n"
    reporteTexto += f"Total general de gastos: ${totalGeneral:.2f}\n"
    reporteTexto += "Gastos por categoría:\n"
    for categoria, total in gastosPorCategoria.items():
        reporteTexto += f"- {categoria}: ${total:.2f}\n"
    reporteTexto += "Gastos por día:\n"
    for fecha, total in sorted(gastosPorDia.items()):
        reporteTexto += f"- {fecha}: ${total:.2f}\n"

    print(reporteTexto)

    opcionGuardar = input("¿Deseas guardar este reporte en un archivo de texto? (S/N): ").upper()
    if opcionGuardar == 'S':
        nombreArchivo = f"reporte_gastos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(nombreArchivo, 'w', encoding='utf-8') as f:
            f.write(reporteTexto)
        print(f"Reporte guardado como '{nombreArchivo}'")