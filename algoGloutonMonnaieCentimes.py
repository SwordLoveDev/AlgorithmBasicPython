"""

Algorithme qui permet de rendre la monnaie à partir d’une liste donnée de valeurs de pièces et de billets.

"""

pieces = [200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]

def rendreMonnaie(arendre):
  somme_restante = arendre
  compteur = 0
  resultat = []
  while round(somme_restante, 2) > 0:
    valeurPieces = pieces[compteur]
    if valeurPieces > somme_restante:
      compteur += 1
    elif valeurPieces == somme_restante:
      resultat.append(valeurPieces)
      somme_restante -= valeurPieces
      somme_restante = round(somme_restante, 2)
    else:
      resultat.append(valeurPieces)
      somme_restante -= valeurPieces
      somme_restante = round(somme_restante, 2)
  return resultat

rendreMonnaie(53.99)