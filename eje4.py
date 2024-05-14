# !/usr/bin python
import sys

# ----- Checkeo de argumentos -----
if len(sys.argv) != 3:
    print('Error en la cantidad de argumentos. Se esperaban 2.')
    print('Uso: python eje3.py <sueldo> <rango>')
    print('<sueldo>: sueldo bruto del empleado. Debe ser un número real.')
    print('<rango>: rango del empleado. Debe ser un número entero entre 1 y 3.')
    sys.exit(1)

# ----- Importo parámetros -----
sueldo = float(sys.argv[1])
rango = int(sys.argv[2])

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