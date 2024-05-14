#!/usr/bin python

# Cree un programa en Python que imprima la hora del sistema,
# estado de memoria RAM y almacenamiento disponible en la partición montada en “/”.

import os
import pandas as pd

# ----------------------------------------
# ---------- Obtención de datos ----------
# --- Obtengo hora ---
fecha_hora = os.popen('date').read()
hora = fecha_hora.split(' ')[4]

# --- Obtengo RAM ---
# ram = os.popen('free -h').read() # Redondea GB a enteros, no me gusta
ram = os.popen('free').read()
ram = [x.split() for x in ram.split('\n') if x] # Separo por líneas y elimino las vacías
ram[0] = [''] + ram[0]
indices = [x[0] for x in ram] # Obtengo los índices
indices = [x for x in indices if x] # Elimino los elementos vacíos
ram = [x[1:] for x in ram] # Elimino la primera columna
ram = pd.DataFrame(ram[1:], columns=ram[0], index=indices)

# - Transformo a GB -
def to_gb(x):
    if x is None:
        return '-nc-'
    elif x.isdigit():
        return round(int(x)/(1024**2), 2)
    return x
ram = ram.map(to_gb)


# --- Obtengo almacenamiento ---
almacenamiento = os.popen('df -h /').read()
almacenamiento = almacenamiento.split('\n')[1] # Selecciono la segunda línea
almacenamiento = almacenamiento.split(' ') # Separo por espacios
almacenamiento = [x for x in almacenamiento if x] # Elimino los elementos vacíos

almacenamiento_dev = almacenamiento[0]
almacenamiento_disponible = almacenamiento[3]
almacenamiento_total = almacenamiento[1]

# ----------------------------------------
# ---------- Impresión de datos ----------
print(f'-'*80)
print(f'Hora del sistema:')
print(hora)
print(f'-'*80)
print(f'Almacenamiento disponible en la partición montada en "/":')
print(f'{almacenamiento_disponible} en el dispositivo {almacenamiento_dev} con un total de {almacenamiento_total}.')
print(f'-'*80)
print(f'Estado de la memoria RAM en GB:\n{ram}')