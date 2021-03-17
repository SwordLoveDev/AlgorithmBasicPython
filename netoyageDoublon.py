"""

Fonction nettoie qui prend en paramètre une liste triée et qui élimine les éléments identiques. 
Par exemple si la liste est : liste = [1,1,2,6,6,6,8,8,9,10], après l’instruction nettoie(liste), 
cette liste a pour valeur [1,2,6,8,9,10].


"""

def nettoie(L):
    n = len(L)
    k = 0
    while k < n-1:
        if L[k] != L[k+1]:
            k = k+1
        else :
            del L[k]
        n = len(L)