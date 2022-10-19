
from unittest import result


def myAddition(a = 0, b = 0):
    if type(a) is int and type(b) is int:   # On vérifie que les deux varables soient ben des nombres
        result = a + b  # On effectue l'apération
    else:
        print("Veuillez saisir des nombres uniquement.")
        return
    
    return result # On retourne le résultat


addition = myAddition(2, 8) # On attrbue la valeur retournée dans une variable

print(addition) 