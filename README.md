# **PROYECTO: SIMULADOR DE GASTO DIARIO**

## Tabla de contenidos 
| Indice | Titulo |
| -- | -- |
|1   | Descripción del proyecto|
|2   | Funciones principal|
|3   | Tecnologias y herramientas utilizadas|
|4   | Instrucciones y requisitos|

## Descripción del proyecto
El es una aplicación de consola diseñada para ayudar a los usuarios a registrar y monitorear sus gastos diarios en diferentes categorías, como comida, transporte, entretenimiento, entre otros. Este simulador permite llevar un control básico de los gastos diarios, semanales o mensuales y obtener un resumen o reporte de los gastos en cada categoría. Toda la información se guarda en un archivo JSON, lo que permite mantener un historial de gastos entre distintas sesiones del programa.

## Funciones principales
- **Registro de gastos**: Permite crear registros de gastos segun su categoria (comida, transporte, entretenimiento, otros...)
- **Listado de gastos**: Muestra al usuario los gastos registrados y posee un filtrado por su categoría o fecha de creación.
- **Calculación de los gastos**: Proporciona el total de los gastos acumulados por día, semana o mes. También los desglosa por cada categoría
- **Generación de reportes**: Crea un resumen de gastos en formato de texto. El reporte puede ser visualizado en pantalla o guardado en un archivo de texto para su visualización externa o su impresión.
- **Persistencia de datos**: La información ingresada al programa se guarda en y se carga en un archivo JSON, lo que asegura la continuidad de los registros.

## Tecnologias y herramientas utilizadas:
-   **Python3**: Fue el lenguaje principal usado en este programa.
-   **Librerías de Python**: 
     - `json`: Utilizado para la serialización y deserialización de datos en formato JSON.
     - `datetime`: Utilizado para la gestión de fechas y horas.
     -  `tabulate`: Utilizado para presentar diferentes datos en forma tabulada en la consola.

## Instrucciones y requisitos para la ejecución del programa:
Para ejecutar este Simulador de Gasto Diario, deberá seguir los siguientes pasos:

#### 1. Requisitos del sistema
Este Simulador de Gasto Diario requiere tener instalado Python 3 en su equipo para su ejecución.

#### 2. Dependencias
El Simulador de Gasto Diario utiliza la dependencia `tabulate` por lo que será necesario instalar para su correcta visualización. Lo podrá instalar con el siguiente comando desde su terminal:

```
pip install tabulate #Debes tener ya instalado python 3
```
#### 3. Descarga del código
Descargue los archivos del proyecto y ejecutelos desde su terminal. O clone el repositorio en su dispositivo con el siguiente comando:

```
git clone https://github.com/Daniel-Santos-F333/Proyecto_Python_SantosDaniel
```
#### 4. Estructura de los archivos
El proyecto consta de los siguientes archivos:
```
├──.gitignore #Para que git ignore los archivos cache generados por el programa
├──gastos.py  #Archivo que almacena todas las funcionalidades del programa
└──main.py    #Archivo que almacena la interfaz visual y ejecuta el programa
```
#### 5. Ejecución del programa
Desde la terminal y ubicado en la carpeta del programa escribir el siguiente código: ==python3 main.py==
```
/user/carpeta/Proyecto_Python_SantosDaniel/: python3 main.py
```

#### 6. Link Sustentacion del proyecto
https://youtu.be/XLVYnxM4b_Q
