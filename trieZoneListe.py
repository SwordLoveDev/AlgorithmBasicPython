"""

On considère un tableau d'entiers tab (type list dont les éléments sont des 0 ou des 1).
On se propose de trier ce tableau selon l'algorithme suivant : à chaque étape du tri, le tableau est constitué de trois zones consécutives, 
la première ne contenant que des 0, la seconde n'étant pas triée et la dernière ne contenant que des 1.

[ Zone de 0 - Zone non triée - Zone de 1 ]

Tant que la zone non triée n'est pas réduite à un seul élément, on regarde son premier élément :

- Si cet élément vaut 0, on considère qu'il appartient désormais à la zone ne contenant que des 0 ;
- Si cet élément vaut 1, il est échangé avec le dernier élément de la zone non triée et on considère alors qu’il appartient à la zone ne contenant que des 1.
Dans tous les cas, la longueur de la zone non triée diminue de 1.

"""

def tri(tab):
    i= 0
    j= len(tab) - 1
    while i != j :
        if tab[i]== 0:
            i= i + 1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j= j-1
    return tab
 
tri([0,1,0,1,0,1,0,1,0])