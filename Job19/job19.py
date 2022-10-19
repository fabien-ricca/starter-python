
# On féfinit la fonction en précisant avec *nbr qu'il n'y a pas de paramètres maximum
def myFunction( *nbr ):
    list=[] 
    for i in nbr:
        if type(i) is int:
            list.append(i)
        else:
            print("Veuillez saisir des nombres uniquement.")
            return
    myList=[] # On crée une deuxième liste dans laquelle on ajoute les éléments s'ils remplissent la condition de comparaison
    while list:
        x = list[0]  
        for y in list: 
            if y < x:
                x = y
        myList.append(x)  # On ajoute l'élément à la nouvelle liste
        list.remove(x) # On le supprime de l'ancienne
            
   
    print(myList) # On affiche la nouvelle liste

myFunction(1, 9, 28, "toto", 7, 6, 32, 59, 42, 36, 71, 92, 11)