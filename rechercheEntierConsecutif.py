"""

Fonction recherche qui prend en paramètre un tableau de nombres entiers tab, 
et qui renvoie la liste (éventuellement vide) des couples d'entiers consécutifs successifs qu'il peut y avoir dans tab.

"""

def recherche(tab):
  tmp = []
  for x in range(len(tab)):
    if x == 0:
      pass
    elif tab[x-1] == tab[x]:
      a = (tab[x],tab[x-1])
      tmp.append(a)
  return tmp
  
recherche([1, 4, 5, 3])