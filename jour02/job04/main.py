def table_multi(N) :
    for i in range(1,11):
        print(i, "*",N,"=",i*N)
while True :
    N = int(input("veuillez saisir un nombre : "))
    if N > 0 :
        break

table_multi(N)
