# !/usr/bin python
import os

desired_path = '/dev'

print(f'Listado de directorios en {desired_path}:')
print('-----------------------------------------')
for dir in os.listdir(desired_path):
    # --- Filtro para listar solo los directorios ---
    if os.path.isdir(f'{desired_path}/{dir}'):
        print(dir)