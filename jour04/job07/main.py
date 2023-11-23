n = 3
L = [8, 24 ,48 ,2 ,16]

def multiple ():
    i = 0
    for x in L:
        if (x%n == 0):
            i += 1
    return i
# Test de la fonction
print("Le nombre de multiples de 3 est de : ",multiple())
