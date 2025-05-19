import json
from gastos import Gastos

def cargaDeDatos():
    try:
        with open('data.json','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def guardadoDeDatos(gastos):
    with open('data.json','w') as file:
        json.dump(gastos, file, indent=4)

def mostrarMenu():
    print("=============================================")
    print("         Simulador de Gasto Diario           ")
    print("=============================================")
    print("Seleccione una opción: ")
    print("                                            ")
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    print("=============================================")
def main():
    gastos = cargaDeDatos()
    gastosManager = Gastos(gastos)
    while True:
        mostrarMenu()
        opcion = input("Ingrese su elección: ")

        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad: "))
            categoria = input("Ingrese la categoria: " )
            descripcion = input("Ingrese una descripción (Opcional): ")

gastosManager.calcularTotalGastos(cantidad,categoria,descripciond)

guardarDatos(gastosManager.gastos)
            

