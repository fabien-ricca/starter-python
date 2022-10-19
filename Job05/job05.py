# l'utilisateur doit entrer deux valeurs
val1 = int(input("Valeur 1 : "))
val2 = int(input("Valeur 2 : "))

# Si les deux valeurs sont égales : "Valeurs égales"
# On affiche les nombres de l'input1 à l'input2 inclus
if val1 == val2:
    print("Les valeurs sont égales.")
else:
    for i in range (val1, val2 + 1):
        print (i)
