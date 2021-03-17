"""

Fonction qui nécessite deux appels récursifs dans une même fonction.
La suite de Fibonacci est une suite numérique définie par u0=0, u1=1 et pour n>=2, un=un−1+un−2.

"""

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(20)