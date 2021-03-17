"""

Fonction prenant en paramètre un tableau de 0 et de 1 tab (type list) 
qui renvoie le nombre décimal des éléments en binaire du tableau.

"""

def convertir(tab):
  tmp = []
  nombre = 0
  tab.reverse()
  for x in range(len(tab)):
    if tab[x] == 1:
      tmp2 = 2 ** x
      tmp.append(tmp2)
  for x in range(len(tmp)):
    nombre = tmp[x] + nombre
  return nombre

convertir([1, 0, 1, 0, 0, 1, 1])