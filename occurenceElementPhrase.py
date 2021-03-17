"""

Fonction occurences prenant comme paramètre une variable phrase de type str. 
Cette fonction doit renvoyer un dictionnaire de type constitué des occurrences des caractères présents dans la phrase.

"""

def occurences(chaine):
  tmp = {}
  for x in range(len(chaine)):
    lettre = chaine[x]
    tmp[chaine[x]] = chaine.count(lettre)
  return tmp

occurences('Hello world !')