"""

Fonction maxi qui prend en paramètre une liste tab de nombres entiers 
et renvoie un couple donnant le plus grand élément de cette liste, 
ainsi que l’indice de la première apparition de ce maximum dans la liste.

"""

def maxi(tab):
  if tab == None:
    return None
  else:
    tmp = max(tab)
    for x in range(len(tab)):
      if tab[x] == tmp:
        return tmp, x
  
maxi([1,5,6,9,1,2,3,7,9,8])