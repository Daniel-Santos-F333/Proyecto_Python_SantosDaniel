import os
from gastos import registrarGasto, listarGastos, calcularTotales, calcularPorCategoria, gastosRegistrados
from reportes import mostrarReporte, guardarReporteJson

def mostrarMenuPrincipal():
    ### Muestra el menú principal de la aplicación
    print("\n=============================================")
    print("        Simulador de Gasto Diario")
    print("=============================================")
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular totales")
    print("4. Calcular gastos por categoría")
    print("5. Generar reporte")
    print("6. Guardar reporte en JSON")
    print("7. Salir")
    print("=============================================")
    opcion = input("Seleccione una opción: ")
    return opcion

def interfazRegistrarGasto():
    ### Interfaz visual para registrar un nuevo gasto
    print("\n=============================================")
    print("            Registrar Nuevo Gasto")
    print("=============================================")
    montoStr = input("- Monto del gasto: ")
    categoria = input("- Categoría (ej. comida, transporte, entretenimiento, otros): ").strip()
    descripcion = input("- Descripción (opcional): ").strip()
    confirmacion = input("\nIngrese 'S' para guardar o 'C' para cancelar: ").upper()
    print("=============================================")
    return montoStr, categoria, descripcion, confirmacion

def submenuListarGastos():
    ### Submenú para listar gastos con opciones de filtrado
    while True:
        print("\n=============================================")
        print("                Listar Gastos")
        print("=============================================")
        print("Seleccione una opción para filtrar los gastos:")
        print("\n1. Ver todos los gastos")
        print("2. Filtrar por categoría")
        print("3. Filtrar por rango de fechas")
        print("4. Regresar al menú principal")
        print("=============================================")
        opcionListar = input("Seleccione una opción: ")

        if opcionListar == "1":
            print("\n--- Listado de Todos los Gastos ---")
            listarGastos(gastosRegistrados)
        elif opcionListar == "2":
            categoriaFiltro = input("Ingrese la categoría a filtrar: ")
            print(f"\n--- Gastos en la categoría '{categoriaFiltro}' ---")
            listarGastos(gastosRegistrados, filtroCategoria=categoriaFiltro)
        elif opcionListar == "3":
            fechaInicio = input("Ingrese la fecha de inicio (YYYY-MM-DD, opcional): ") or None
            fechaFin = input("Ingrese la fecha de fin (YYYY-MM-DD, opcional): ") or None
            print(f"\n--- Gastos entre '{fechaInicio if fechaInicio else 'inicio'}' y '{fechaFin if fechaFin else 'fin'}' ---")
            listarGastos(gastosRegistrados, filtroFechaInicio=fechaInicio, filtroFechaFin=fechaFin)
        elif opcionListar == "4":
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def submenuCalcularTotales():
    ### Submenú para calcular el total de gastos por periodo
    while True:
        print("\n=============================================")
        print("          Calcular Total de Gastos")
        print("=============================================")
        print("Seleccione el periodo de cálculo:")
        print("\n1. Calcular total diario")
        print("2. Calcular total semanal")
        print("3. Calcular total mensual")
        print("4. Regresar al menú principal")
        print("=============================================")
        opcionCalcular = input("Seleccione una opción: ")

        if opcionCalcular == "1":
            totales = calcularTotales(gastosRegistrados, "diario")
            print("\n--- Total de gastos (diario) ---")
            if isinstance(totales, str):
                print(totales)
            elif isinstance(totales, dict):
                for periodoLabel, total in totales.items():
                    print(f"{periodoLabel}: ${total:.2f}")
        elif opcionCalcular == "2":
            totales = calcularTotales(gastosRegistrados, "semanal")
            print("\n--- Total de gastos (semanal) ---")
            if isinstance(totales, str):
                print(totales)
            elif isinstance(totales, dict):
                for periodoLabel, total in totales.items():
                    print(f"{periodoLabel}: ${total:.2f}")
        elif opcionCalcular == "3":
            totales = calcularTotales(gastosRegistrados, "mensual")
            print("\n--- Total de gastos (mensual) ---")
            if isinstance(totales, str):
                print(totales)
            elif isinstance(totales, dict):
                for periodoLabel, total in totales.items():
                    print(f"{periodoLabel}: ${total:.2f}")
        elif opcionCalcular == "4":
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def interfazCalcularPorCategoria():
    ### Interfaz visual para calcular gastos por categoría
    print("\n=============================================")
    print("        Calcular Gastos por Categoría")
    print("=============================================")
    resultado = calcularPorCategoria(gastosRegistrados)
    if isinstance(resultado, str):
        print(resultado)
    else:
        for categoria, total in resultado.items():
            print(f"{categoria}: ${total:.2f}")
    print("=============================================")
    input("Presione Enter para continuar...")

def submenuGenerarReporte():
    ### Submenú para generar reportes por periodo
    while True:
        print("\n=============================================")
        print("           Generar Reporte de Gastos")
        print("=============================================")
        print("Seleccione el tipo de reporte:")
        print("\n1. Reporte diario")
        print("2. Reporte semanal")
        print("3. Reporte mensual")
        print("4. Regresar al menú principal")
        print("=============================================")
        opcionReporte = input("Seleccione una opción: ")

        if opcionReporte == "1":
            print("\n--- Reporte Diario ---")
            mostrarReporte("diario")
        elif opcionReporte == "2":
            print("\n--- Reporte Semanal ---")
            mostrarReporte("semanal")
        elif opcionReporte == "3":
            print("\n--- Reporte Mensual ---")
            mostrarReporte("mensual")
        elif opcionReporte == "4":
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def interfazGuardarReporteJson():
    ### Interfaz visual para guardar reporte en json
    print("\n=============================================")
    print("           Guardar Reporte en JSON")
    print("=============================================")
    while True:
        periodoGuardar = input("Guardar reporte por (diario/semanal/mensual): ").lower().strip()
        if periodoGuardar in ["diario", "semanal", "mensual"]:
            break
        else:
            print("Periodo inválido. Debe ser 'diario', 'semanal' o 'mensual'.")
    nombreArchivo = input("Ingrese el nombre del archivo para guardar el reporte (ej: reporte.json): ")
    guardarReporteJson(periodoGuardar, nombreArchivo)
    print("=============================================")
    input("Reporte guardado. Presione Enter para continuar...")

def main():
    ### Función principal de la aplicación
    global gastosRegistrados
    while True:
        opcion = mostrarMenuPrincipal()

        if opcion == "1":
            montoStr, categoria, descripcion, confirmacion = interfazRegistrarGasto()
            if confirmacion == "S":
                try:
                    monto = float(montoStr)
                    if monto <= 0:
                        print("Error: El monto debe ser mayor que cero.")
                    else:
                        gastosRegistrados = registrarGasto(gastosRegistrados, monto, categoria, descripcion)
                except ValueError:
                    print("Error: Monto inválido. Debe ingresar un número.")
            elif confirmacion == "C":
                print("Registro de gasto cancelado.")

        elif opcion == "2":
            submenuListarGastos()

        elif opcion == "3":
            submenuCalcularTotales()

        elif opcion == "4":
            interfazCalcularPorCategoria()

        elif opcion == "5":
            submenuGenerarReporte()

        elif opcion == "6":
            interfazGuardarReporteJson()

        elif opcion == "7":
            print("\n¡¡Gracias por usar el Simulador de Gasto Diario!!")
            break

        else:
            print("\nOpción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()