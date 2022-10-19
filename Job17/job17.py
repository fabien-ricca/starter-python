
# On féfinit la fonction en précisant avec *args qu'il n'y a pas de paramètres maximum
def myFunction(*args):
    # On crée une liste
    mylist = []   
    # Pour chaque argument si son modulo = 0 on l'ajoute à la liste
    for i in args:
        if type(i) is int:
            if i % 2 == 0:
                mylist.append(i)
        else:
            print("Veuillez saisir des nombres uniquement.")
            return
    # On affiche la liste
    print(mylist)


myFunction(0, 1, "toto", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)