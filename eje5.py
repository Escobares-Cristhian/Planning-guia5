#!/usr/bin python
import os
import sys
import time

# ----- Checkeo de argumentos -----
if len(sys.argv) != 2:
    print('Error en la cantidad de argumentos. Se esperaba 1.')
    print('Uso: python eje5.py <segundos>')
    print('<segundos>: segundos a esperar. Debe ser un número entero.')
    sys.exit(1)

# ----- Importo parámetros -----
seconds_to_wait = int(sys.argv[1])

# ----- Validación de argumentos -----
if seconds_to_wait < 0:
    print('Los segundos no pueden ser negativos.')
    sys.exit(1)

# ----- Ejecución -----
# Obtengo pid del proceso actual
pid = os.getpid()

for i in range(seconds_to_wait):
    print(f'En el proceso con PID {pid}, ha contado {i+1} segundos...')
    time.sleep(1)