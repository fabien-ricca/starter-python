
liste =[1, 9, 28, 7, 6, 32, 59, 42, 36, 71, 92, 11]


def myFunction(a):
    list=[] 
    for i in a:
        if type(i) is int:
            list.append(i)
        else:
            print("Veuillez saisir des nombres uniquement.")
            return
    myList=[] 
    while list:
        x = list[0]  
        for y in list: 
            if y < x:
                x = y
        myList.append(x)
        list.remove(x)
            
   
    return myList   # On return le nouvelle lste



def myDisplay(f):
    print(f)


# On passe myFunction en paramètre de myDisplay() pour afficher myList dans le terminal
myDisplay(myFunction(liste))