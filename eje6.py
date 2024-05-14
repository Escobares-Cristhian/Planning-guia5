#!/usr/bin python
import sys

# ----- Checkeo de argumentos -----
if len(sys.argv) != 2:
    print('Error en la cantidad de argumentos. Se esperaban 1.')
    print('Uso: python eje6.py <operacion>')
    print('Donde <operacion> es la operacion a realizar. Un string que puede contener los caracteres + - * / ( ) y numeros. Los espacios son permitidos.')
    print('Ejemplo: python3 eje6.py "(1/3+1-1)*3"')
    sys.exit(1)

# ----- Importo parámetros -----
operacion = sys.argv[1]

# ---- Elimino espacios -----
operacion = operacion.replace(' ', '')

# ----- Validación de argumentos -----
if not operacion.replace('+', '').replace('-', '').replace('*', '').replace('/', '').replace('.', '').replace('(', '').replace(')', '').isdigit():
    print('La operacion debe contener solo numeros y los caracteres +, -, *, /.')
    sys.exit(1)

# ----- Ejecución -----
resultado = eval(operacion)

# ---- Redondeo ante-último decimal por error de la máquina -----
digitos = len(str(1/7).split('.')[1])
resultado = round(resultado, digitos-2)

# ---- Elimino los ceros a la derecha -----
resultado = str(resultado)
if '.' in resultado:
    resultado = resultado.rstrip('0')
    if resultado[-1] == '.':
        resultado = resultado[:-1]
print(f'El resultado de la operación es: {resultado}')