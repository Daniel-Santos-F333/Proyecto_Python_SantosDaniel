import sys
from gastos import (registrarGasto, listarGastos, calcularGastos, generarReporte, cargarGastos, guardarGastos)

def limpiarPantallaSimulada():
    print("\n" * 50)

def mostrarMenuPrincipal():
    print("=============================================")
    print("              Menu Principal                ")
    print("=============================================")
    print("Seleccione una opción:")
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    print("=============================================")

def main():
    cargarGastos()

    while True:
        limpiarPantallaSimulada()
        mostrarMenuPrincipal()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            limpiarPantallaSimulada()
            registrarGasto()
        elif opcion == '2':
            while True:
                limpiarPantallaSimulada()
                print("\n=============================================")
                print("                Listar Gastos                ")
                print("=============================================")
                print("Seleccione una opción para filtrar los gastos:")
                print("1. Ver todos los gastos")
                print("2. Filtrar por categoría")
                print("3. Filtrar por rango de fechas")
                print("4. Regresar al menú principal")
                print("=============================================")
                
                filtroOpcion = input("Elige una opción: ")

                if filtroOpcion == '1':
                    limpiarPantallaSimulada()
                    listarGastos()
                    break
                elif filtroOpcion == '2':
                    categoria = input("Introduce la categoría a filtrar: ")
                    limpiarPantallaSimulada()
                    listarGastos(filtroCategoria=categoria)
                    break
                elif filtroOpcion == '3':
                    print("\nFiltrar por rango de fechas:")
                    print("  a) Diario (solo hoy)")
                    print("  b) Semanal (últimos 7 días)")
                    print("  c) Mensual (mes actual)")
                    rango = input("Elige un rango (a/b/c): ").lower()
                    if rango == 'a':
                        limpiarPantallaSimulada()
                        listarGastos(filtroRangoFechas='diario')
                    elif rango == 'b':
                        limpiarPantallaSimulada()
                        listarGastos(filtroRangoFechas='semanal')
                    elif rango == 'c':
                        limpiarPantallaSimulada()
                        listarGastos(filtroRangoFechas='mensual')
                    else:
                        print("Opción de filtro de fecha inválida.")
                    break
                elif filtroOpcion == '4':
                    break
                else:
                    print("Opción no válida. Por favor, elige un número del 1 al 4.")
                input("\nPresiona Enter para continuar...")

        elif opcion == '3':
            limpiarPantallaSimulada()
            while True:
                print("\n=============================================")
                print("          Calcular Total de Gastos         ")
                print("=============================================")
                print("Seleccione el periodo de cálculo:")
                print("1. Calcular total diario")
                print("2. Calcular total semanal")
                print("3. Calcular total mensual")
                print("4. Regresar al menú principal")
                print("=============================================")
                 
                periodoOpcion = input("Elige una opción: ")

                if periodoOpcion == '1':
                    limpiarPantallaSimulada()
                    calcularGastos(periodoCalculo='diario')
                    break
                elif periodoOpcion == '2':
                    limpiarPantallaSimulada()
                    calcularGastos(periodoCalculo='semanal')
                    break
                elif periodoOpcion == '3':
                    limpiarPantallaSimulada()
                    calcularGastos(periodoCalculo='mensual')
                    break
                elif periodoOpcion == '4':
                    break
                else:
                    print("Opción no válida. Por favor, elige un número del 1 al 4.")
                input("\nPresiona Enter para continuar...")

        elif opcion == '4':
            while True:
                limpiarPantallaSimulada()
                print("\n=============================================")
                print("           Generar Reporte de Gastos         ")
                print("=============================================")
                print("Seleccione el tipo de reporte:")
                print("1. Reporte diario")
                print("2. Reporte semanal")
                print("3. Reporte mensual")
                print("4. Regresar al menú principal")
                print("=============================================")
                
                reporteOpcion = input("Elige una opción: ")

                if reporteOpcion == '1':
                    limpiarPantallaSimulada()
                    generarReporte(tipoReporte='diario')
                    break
                elif reporteOpcion == '2':
                    limpiarPantallaSimulada()
                    generarReporte(tipoReporte='semanal')
                    break
                elif reporteOpcion == '3':
                    limpiarPantallaSimulada()
                    generarReporte(tipoReporte='mensual')
                    break
                elif reporteOpcion == '4':
                    break
                else:
                    print("Opción no válida. Por favor, elige un número del 1 al 4.")
                input("\nPresiona Enter para continuar...")

        elif opcion == '5':
            confirmarSalida = input("\n¿Desea salir del programa? (S/N): ").upper()
            if confirmarSalida == 'S':
                print("\n¡Gracias por usar su Simulador de Gasto Diario por excelencia!")
                sys.exit()
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()