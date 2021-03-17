"""

http://championmath.free.fr/tourhanoi.htm

"""

def hanoi(n,debut,inter,fin):
    if (n > 0):
        hanoi(n-1,debut,fin,inter)
        print ("Déplace ",debut,"->",fin)
        hanoi(n-1,inter,debut,fin)

hanoi(5, 'A', 'B', 'C')