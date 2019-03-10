# -*- coding: utf-8 -*-

import re

'''
Implementación del problema:
Defina recursivamente la función par:BIN->{0,1} que devuelve 1 si la cantidad de unos en el numeral es par, y 0 si es impar.
'''

def par(numero):

  m = re.split(r'^(.)', numero)

  primero = m[1]
  resto = m[2]

  if (numero == '0'):
    return '1'
  elif (numero == '1'):
    return '0'
  elif (primero == '0'):
    return par(resto)
  else:
    if (par(resto) == '1'):
      # después de mí hay una cantidad PAR de unos
      return '0'
    else:
      # después de mí hay una cantidad IMPAR de unos
      return '1'


numero = input()

resultado = par(numero)
print(resultado)

if (resultado == '1'):
  print("-> Cant. PAR")
else:
  print("-> Cant. IMPAR")
