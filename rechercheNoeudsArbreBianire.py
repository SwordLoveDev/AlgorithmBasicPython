"""

Fonction recherche(val) qui recherche une valeur dans l'arbre et renvoie le noeud contenant cette valeur, None sinon.

"""

abr = [12, [1, [91, [], [14, [], []]], [67, [], []]], [7, [], [82, [11, [], []], []]]]

def rechercher(arbre, element):
  if arbre == []:
    return False
  else:
    l = len(arbre)
    for x in range(l):
      if arbre[x][0] or arbre[x][1] == element:
        return True
    return False

rechercher(abr, 91)