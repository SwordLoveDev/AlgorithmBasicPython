"""

Algorithme récursif qui permet de rendre la monnaie à partir d’une liste donnée de valeurs de pièces et de billets 
- le système monétaire est donné sous forme d’une liste pieces=[100, 50, 20, 10, 5, 2, 1] 
- (on supposera qu’il n’y a pas de limitation quant à leur nombre), on cherche à donner la liste de pièces à rendre pour une somme donnée en argument.

"""

pieces = [100,50,20,10,5,2,1]

def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
      return solution
    p = pieces[i]
    if p <= arendre :
      solution.append(p)
      return rendu_glouton(arendre - p, solution, i)
    else :
      return rendu_glouton(arendre, solution, i+1)

rendu_glouton(291,[],0)