from gastos import gastosRegistrados, calcularTotales, calcularPorCategoria
from datetime import datetime
import json

def generarReporte(periodo="mensual"):
    ### Genera un reporte de gastos en formato texto
    if not gastosRegistrados:
        return "No hay gastos registrados para generar un reporte."

    reporte = f"--- Reporte de Gastos ({periodo.capitalize()}) ---\n\n"
    reporte += f"Fecha de Generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    totales = calcularTotales(gastosRegistrados, periodo)
    if isinstance(totales, str):
        reporte += totales + "\n\n"
    elif isinstance(totales, dict):
        reporte += f"--- Totales por {periodo.capitalize()} ---\n"
        for periodoLabel, total in totales.items():
            reporte += f"{periodoLabel}: ${total:.2f}\n"
        reporte += "\n"

    gastosCategoria = calcularPorCategoria(gastosRegistrados)
    if isinstance(gastosCategoria, str):
        reporte += gastosCategoria + "\n"
    elif isinstance(gastosCategoria, dict):
        reporte += "--- Gasto por Categoría ---\n"
        for categoria, total in gastosCategoria.items():
            reporte += f"{categoria}: ${total:.2f}\n"

    return reporte

def mostrarReporte(periodo="mensual"):
    ### Muestra el reporte en la consola
    reporte = generarReporte(periodo)
    print(reporte)

def guardarReporteJson(periodo="mensual", nombreArchivo="reporte_gastos.json"):
    ### Guarda el reporte en un archivo json
    totales = calcularTotales(gastosRegistrados, periodo)
    gastosCategoria = calcularPorCategoria(gastosRegistrados)

    reporteData = {
        "fechaGeneracion": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "totales": totales if isinstance(totales, dict) else totales,
        "gastosPorCategoria": gastosCategoria if isinstance(gastosCategoria, dict) else gastosCategoria
    }
    try:
        with open(nombreArchivo, "w") as f:
            json.dump(reporteData, f, indent=4)
        print(f"Reporte guardado exitosamente en {nombreArchivo}")
    except IOError:
        print(f"Error al guardar el reporte en {nombreArchivo}")