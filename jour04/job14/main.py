import string

def my_long_word(n, s):
    
    mots = [
        mots.strip(string.punctuation)
        for mots in s.split()  
        
        if mots.strip(string.punctuation)[n:]
    ]
    
    return ' '.join(mots)

input_str = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(3, input_str)
print (resultat)