nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

result = [int(num) for num in nombres] 

n = 0
for _ in result:
    n += 1

print (result)

for i in range (len(result)):
    for j in range (len(result)):
       if result[i]<=result[j]:
           result[i],result[j]=result[j],result[i]


print (result)