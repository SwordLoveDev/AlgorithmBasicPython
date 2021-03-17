"""

La fonction pascal renvoit une liste correspondant au triangle de Pascal de la ligne 1 à la ligne n où
n est un nombre entier supérieur ou égal à 2 (le tableau sera contenu dans la variable C). 
La variable Ck doit, quant à elle, contenir, à l’étape numéro k, la k-ième ligne du tableau.

"""

def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C

pascal(10)