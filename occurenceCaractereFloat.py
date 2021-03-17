"""

Fonction de recherche qui prend en paramètres caractere (un caractère) et mot (une chaîne de caractères)
et qui renvoie le nombre d’occurrences de caractere dans mot, c’est-à-dire le nombre de fois où caractere apparaît dans mot.

"""

def recherche(lettre, mot):
  compteur = 0
  for x in range(len(mot)):
    if mot[x] == lettre:
      compteur += 1
  return compteur

recherche('i',"mississippi")