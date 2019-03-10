# -*- coding: utf-8 -*-

'''
Implementación del problema:
Defina recursivamente la función f:N->2^Sigma^* tal que cumple que:
f(k) = { w : w en Sigma^* y largo(w) = k }
'''

def f(n):
  if (n == 0):
    return set([""])
  else:
    resultado = set([])
    for w in f(n-1):
      for x in alfabeto:
        resultado.add(w+x)
    return resultado


alfabeto = set(["a", "b", "c", "d", "e"])

n = int(input())
res = f(n)
print("\nf("+str(n)+") = ")
print(res)

print("\n#f("+str(n)+") = "+str(len(res)))
