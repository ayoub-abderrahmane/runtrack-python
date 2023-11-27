def afficher_tapis_diagonale(n, width, height):
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if j == 1 or j == width:
                print("|", end=" ")
            elif i == 1 or i == height:
                print("-", end=" ")
            else:
                if j == width - i + 1:
                    print("", end=" ")
                else:
                    print("#", end=" ")
        print()

afficher_tapis_diagonale(5, 10, 10)