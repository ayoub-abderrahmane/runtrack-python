height = int(input("Quelle est la taille de votre triangle ? : "))
hauteur = -1

for _ in range(height):
    if hauteur == height - 2:
        break
    else:
        hauteur = hauteur + 1
        triangle = "/" + (hauteur * " ") + (hauteur * " ") + " \\"
        espace = " " * (1 + (height - hauteur - 1))
        
        if hauteur == height - 1:
            break
            
        print(f"{espace}{triangle}")

print(" /" + ((height * 2) - 2) * "_" + " \\")