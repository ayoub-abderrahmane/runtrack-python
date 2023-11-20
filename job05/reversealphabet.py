import string

def listAlphabet():
    return list(string.ascii_lowercase)

alphabet_list = listAlphabet()

reversed_alphabet_list = alphabet_list[::-1]

print(reversed_alphabet_list)