"""

Fonction recherche, prenant en paramètre un tableau non vide tab (type list) d'entiers et un entier n, 
et qui renvoie l'indice de la dernière occurrence de l'élément cherché. 
Si l'élément n'est pas présent, la fonction renvoie la longueur du tableau.

"""

def recherche(tab, element):
  tmp = ""
  if tab == []:
    return None
  else:
    for x in range(len(tab)):
      if tab[x] == element:
        tmp = x
    if tmp == "":
      return len(tab)
    else:
      return tmp

print(recherche([5, 3],3))