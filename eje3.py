#!/usr/bin python
import sys

# ----------------------------------------------------------------------
# ------------------------- Colocar parámetros -------------------------
sueldo = 1200
rango = 3


# ----------------------------------------------------------------------
# ----------------- NO MODIFICAR A PARTIR DE ESTE PUNTO ----------------
# ----------------------------------------------------------------------
# ----- Validación de argumentos -----
if rango not in [1, 2, 3]:
    print('El rango debe ser un número entero entre 1 y 3.')
    sys.exit(1)
if sueldo < 0:
    print('El sueldo no puede ser negativo.')
    sys.exit(1)
    
# ----- Ejecución -----
if rango == 1:
    remuneracion = sueldo * 0.83
elif rango == 2:
    remuneracion = sueldo * 1.2
else:
    remuneracion = sueldo * 5

print(f'La remuneración es: {remuneracion:.2f}')