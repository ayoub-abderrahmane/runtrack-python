def nombrePremier(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True

for x in range (1,1001):
    if nombrePremier(x):
       print(x)