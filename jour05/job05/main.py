def decaler_message(message, decalage=3):
    resultat = ""
    for char in message:
        if char.isalpha():  
            if char.isupper():  
                resultat += chr((ord(char) - decalage - ord('A')) % 26 + ord('A'))
            elif char.islower():  
                resultat += chr((ord(char) - decalage - ord('a')) % 26 + ord('a'))
        else:
            resultat += char  
    return resultat

message_original = input ("Veuilliez entrez une phrase :")
message_decale = decaler_message(message_original)
print("Message original:", message_original)
print("Message décalé de 3 lettres:", message_decale)