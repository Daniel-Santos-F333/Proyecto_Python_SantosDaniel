import json
import os
from datetime import datetime, timedelta

from tabulate import tabulate

dataDir = "data"
dataFile = os.path.join(dataDir, "gastos.json")

def cargaDeDatos():
    """Carga los datos desde el archivo JSON."""
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
    
