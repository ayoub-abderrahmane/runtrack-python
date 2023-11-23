L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

min=L [0]
max=L [0]

for i in range (len(L)):
    if L[i] > max:
        max= L[i]
    if L[i] < min:
        min=L[i]

print ("la valeur max est :", max)
print ("la valeur min est :", min)

