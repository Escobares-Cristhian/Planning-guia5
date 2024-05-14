#!/bin/bash

for i in {3..9..3}
do
    python3 eje5.py $i &
done

wait # Espero a que todos los procesos hijos terminen
echo "Todos los procesos hijos terminaron"