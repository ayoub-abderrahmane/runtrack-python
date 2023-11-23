def multiple (L,n):
    i = 0
    for x in L:
        if (x%n == 0):
            i = i + 1
    return i
# Test de la fonction
n = 3
L = [8, 24 ,48 ,2 ,16]
print("Le nombre de multiples de 3 est : ",multiple(L,n))
