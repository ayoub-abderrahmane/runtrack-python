chaine = "abcdefghijklmnopqrstuvwxyz" *10
n = 40
for i in range(1, n) :
    pyramide = chaine[:2*i - 2]
    print(pyramide)