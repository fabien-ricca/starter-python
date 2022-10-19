# Demander une input à l'utlisateur.
var1 = input("> ")

# Si l'input est "Aurevoir" alors fn du programme.
# Si l'input est "Bonjour" alors : "Bonjour à toi".
# Si l'input ne correspond à aucun des deux on redemande une input.
while True:
    if var1 == "Au revoir":
        break
    elif var1 == "Bonjour" or "bonjour":
        print("Bonjour à toi !")
        var1 = input("> ")
    else:
        var1 = input("> ")