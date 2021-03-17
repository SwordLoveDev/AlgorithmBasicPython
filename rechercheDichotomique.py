"""
tab : tableau d’entiers trié dans l’ordre croissant
x : nombre entier
La fonction renvoie l'index de x si tab contient x et False sinon

"""

def dichotomie(tab, x):
    debut = 0 
    fin = len(tab) - 1
    while debut <= fin:
        m = (fin + debut) // 2
        if x == tab[m]:
            return m
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1			
    return False

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))