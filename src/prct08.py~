#!usr/bin/python
#!encoding: UTF-8

import sys
import math
import modulo

argumentos = sys.argv[1:]
#Si la lista tiene un elemento se ejecuta el if, en caso contrario te lo pide por pantalla.
if (len(argumentos) == 8):         # la lista ahora tiene 8 argumentos  
    n = int (argumentos[0])
    aproximaciones = int (argumentos[1])
    umbral = []
    for i in range (2,7):
      umbral.append(float (argumentos[i]))
    nombre_fichero = argumentos[7]  
else:
    print"Introduzca el nº de intervalos (n>0): "
    n = int (raw_input());
    print "Introduzca el numero de aproximaciones: "
    aproximaciones = int (raw_input());
    print"Introduzca 5 umbrales de aproximaciones"
    umbral = []
    for i in range(5):
      print"Introduzca el umbral", i, ":"
      umbral.append(float (raw_input()));
    print "Introduzca el nombre del fichero para almacenar los resultados: "
    nombre_fichero = raw_input();
    
if (n>0):
  # Una forma para averiguar si un fichero existe o no puede ser esta
    try:
      fichero = open (nombre_fichero, "a")
    except:
      fichero = open (nombre_fichero, "w")
    fichero.write ("Nº de intervalos: %d\n" % (aproximaciones))
    for i in range (5):
      porcentaje = modulo.error (n, aproximaciones, umbral[i])
      fichero.write ("%2.2f%% de fallos para el umbral %2.5f\n" % (porcentaje, umbral[i]))
    fichero.close ()  
else:
    print "El valor de los intervalos debe ser mayor que 0"