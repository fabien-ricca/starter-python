
# On féfinit la fonction en précisant avec *nbr qu'il n'y a pas de paramètres maximum
def myFunction(*nbr):
    mylist = []    
    for i in nbr:   
        if type(i) is int:  # On s'assure que chaque argument est un nombre
            mylist.append(i)    # Si oui on l'ajoute à la liste
            mylist.sort()   # On la trie avec sort
        else:   # Si non on affiche un message d'erreur et on arrête la boucle
            print("Veuillez saisir des nombres uniquement.") 
            return
    print(mylist) # On affiche la liste triée

myFunction(1, 9, 2, 7, 6, 2, 59, 42, 36, 71, 2, 11)
