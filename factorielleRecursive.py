"""

Si n est un entier naturel non nul, n! (factorielle n) est le produit des n premiers entiers naturels non nuls.
Ainsi, 4!=4x3x2x1, donc 4!=24.

"""

def factorielle(n):
  if n == 0:
    return 1
  else:
    return n * factorielle(n-1)

factorielle(7)