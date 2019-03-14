# -*- coding: utf-8 -*-

'''
Implementación del problema:
Defina la función eval:BIN->N que devuelve el natural que resulta de ser interpretado como un número binario e.g. eval(1100) = 12.
'''

def eval(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        ultimo = n % 10
        resto = n / 10
        return 2*eval(resto) + ultimo

n = int(input())
print(eval(n))