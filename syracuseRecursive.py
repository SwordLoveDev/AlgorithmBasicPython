"""

Suite de Syracuse : soit un la suite d'entiers définie, pour u0 un entier strictement supérieur à 1, par un+1 = un / 2 si un pair et un+1 = 3un + 1
La conjecture de Syracuse (non démontrée à ce jour) postule qu'il existe toujours un entier n tel que un = 1 quel que soit le choix de u0

"""

def syracuse(n):
  if n > 1:
    print(n)
    if n % 2 == 0:
      return syracuse(n / 2) 
    else:
      return syracuse(3 * n + 1)
  else:
    return n

syracuse(42)