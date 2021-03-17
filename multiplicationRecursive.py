"""

Fonction multiplication recursive, prenant en paramètres deux nombres entiers n1 et n2, 
et qui renvoie le produit de ces deux nombres. Les seules opérations autorisées sont l’addition et la soustraction.

"""

def multiplication(x, y):
    """x et y sont des entiers naturels"""
    if x == 0:
        return x
    else:
        return y + multiplication(x - 1, y)

multiplication(2,6)