def moyenne():
    n1 = int(input("Entrez la première note :"))
    n2 = int(input("Entrez la deuxième note :"))
    n3 = int(input("Entrez la troisième note :"))
    
    moyenne_etudiant = (n1 + n2 + n3) / 3
    
    return moyenne_etudiant

moyenne_etudiant = moyenne()

print("La moyenne de l'étudiant est ", moyenne_etudiant)

if moyenne_etudiant >= 15:
    print ("Très bon élève")
elif moyenne_etudiant >=11:
    print ("Bon élève")
elif moyenne_etudiant >=8:
    print ("Élève moyen")
elif moyenne_etudiant <=7:
    print ("Élève devant faire des efforts")