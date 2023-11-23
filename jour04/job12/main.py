L = [18 ,15, 39 ,5 ,44]
    
for i in range (len(L)):
    for j in range (len(L)):
       if L[i]<=L[j]:
           L[i],L[j]=L[j],L[i]

print (L)