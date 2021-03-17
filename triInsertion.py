"""

La fonction triInsertion suivante prend en argument une liste L et trie cette liste en utilisant la méthode du tri par insertion.

"""

def triInsertion(L):
    n = len(L)
    if []:
      return L
    for j in range(1,n):
      e = L[j]
      i = j
      while  i > 0 and L[i-1] > n:
        i = i - 1
      if i != j:
        for k in range(j,i,1):
          L[k] = L[k+1]
          L[i] = e
    return L

triInsertion([2,5,-1,7,0,28])