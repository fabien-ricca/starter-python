
# On féfinit la fonction en précisant avec *args qu'il n'y a pas de paramètres maximum
def myFunction(*args):
    # On affiche dans le terminal chaque élément
    for i in args:
            print(i)
    

myFunction(1, 2, "Toto", 3, 4, 5, 6, 7, "Bonjour", 8, 9)