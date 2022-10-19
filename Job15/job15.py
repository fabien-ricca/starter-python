
# On définit la fonction, ainsi que la valeur par défaut de ces deux varables en paramètre
def myFunction(prenom="", nom=""):
    #On ajoute une sécurité au cas où il manquerait un ou les paramètres
    if prenom == "" or nom == "":
        print("Veuillez rentrer un prenom ET un nom.")
    # Sinon on affiche une phrase incluant les deux paramètres
    else:
        print("Bonjour", prenom, nom)

# On peut demander en input les deux variables 
# a = input("quel est votre prenom ? ")
# b = input("quel est votre nom ? ")

# On appelle la fonction
myFunction("Fabien", "Ricca")

