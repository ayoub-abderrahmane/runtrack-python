nom="lit"
prix="prix400"
qté=400

print (nom , prix , qté)

wallet=int(input("Veuillez saisir la quantité souhaité :"))

if wallet<=qté :
    print ("Toujours disponible")
else:
    print("Rupture de stock")
