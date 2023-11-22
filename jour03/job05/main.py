# on définit la fonction calcule
def calcule(num1, operator, num2):
    # on ajoute une boucle qui permet de déterminer le symbole saisi
    if operator == "+":
       print (num1 + num2)
    elif operator == "-":
       print (num1 - num2)
    elif operator == "*":
       print (num1 * num2)
    elif operator == "%":
       print (num1 % num2)
    elif operator == "/":
       print (num1 / num2)

# on appelle ensuite la fonction    
calcule (30, "/", 20)