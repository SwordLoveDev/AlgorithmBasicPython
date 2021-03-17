"""

Fonction moyenne prenant en paramètre un tableau d'entiers tab (type list) 
qui renvoie la moyenne de ses éléments si le tableau est non vide et affiche 'erreur' si le tableau est vide.

"""

def moyenne(tab):
  if tab == []:
    return "erreur"
  else:
    somme = 0
    for x in range(len(tab)):
      somme = tab[x] + somme
    return somme / len(tab)

moyenne([1,2,3,4,5,6,7,8,9,10])