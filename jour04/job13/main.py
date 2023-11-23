def doublon(liste):
    res = []
    for i in liste:
        if i not in res:
            res.append (i)
    return res

L = [10,20,30,20,10,50,60,40,80,50,40]

print (doublon (L))
