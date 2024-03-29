#!usr/bin/python
#!encoding: UTF-8

import sys
import math
PI35DT = PI35 = 3.1415926535897931159979634685441852

# def calcular_xi (n, i):
#xi = (i -1.0/2.0) / n               # Esta es una función que podemos emplear.
#return xi
def calcular_pi(n):
    PI35 = 3.1415926535897931159979634685441852    #Muestra el valor real de la constante pi.
    sumatorio = 0.0
    ini = 0
    intervalos = 1.0 / float (n)
    for i in range (n):
       x_i = ((i+1) - 1.0/2.0) / n  # Aquí se puede utilizar la funcion def que hemos puesto antes.
       fx_i = 4.0 / (1+x_i * x_i)
       ini += intervalos
       sumatorio += fx_i
    valor_pi = sumatorio / n
    return (valor_pi)
    
    
def error (n, aproximaciones, umbral):
      intervalo = n
      lista = []
      for i in range (aproximaciones):
	valor = calcular_pi (intervalo)
	lista.append (valor)
	intervalo += n
#      print lista
      diferencia = []
      for i in range (aproximaciones):
	dif = abs(PI35DT - lista[i])
	diferencia.append (dif)
      correcto = 0
      for i in range (aproximaciones):
	if (diferencia[i]<=umbral):
	  correcto = correcto + 1
      porcentaje = 100.0 * (1.0 - (float(correcto) / float(aproximaciones)))  
      return (porcentaje)	
    
    
    
if (__name__=="__main__"):    

  argumentos = sys.argv[1:]

  if (len(argumentos) == 3):           #Si la lista tiene un elemento se ejecuta el if, en caso contrario te lo pide por pantalla.
    n = int (argumentos[0])
    aproximaciones = int (argumentos[1])
    umbral = float (argumentos[2])
  else:
      print"Introduzca el nº de intervalos (n>0): "
      n = int (raw_input());
      print "Introduzca el numero de aproximaciones: "
      aproximaciones = int (raw_input());
      print "Introduzca el umbral del error"
      umbral = float (raw_input());
    
  if (n>0):
    porcentaje = error(n, aproximaciones, umbral);    
    print "El porcentaje de fallos es del ", porcentaje
  
  else:
      print "El valor de los intervalos debe ser mayor que 0"