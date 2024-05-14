#!/bin/bash

for i in {3..9..3}
do
    python3 eje5.py $i
done

# No es necesario poner un wait ya que los procesos hijos se ejecutan de manera secuencial
echo "Todos los procesos hijos terminaron"