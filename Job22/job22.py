import re


def maj(character):     # On crée un premer dictionnaire minuscule vers majuscule
    dictionary = {
        "a" : "A",
        "b" : "B",
        "c" : "C",
        "d" : "D",
        "e" : "E",
        "f" : "F",
        "g" : "G",
        "i" : "I",
        "j" : "J",
        "k" : "K",
        "l" : "L",
        "m" : "M",
        "n" : "N",
        "o" : "O",
        "p" : "P",
        "q" : "Q",
        "r" : "R",
        "s" : "S",
        "t" : "T",
        "u" : "U",
        "v" : "V",
        "w" : "W",
        "x" : "X",
        "y" : "Y",
        "z" : "Z"
    }
    if character in dictionary:     # Si la lettre est dans le dictionnaire on retourne sa valeur
        return dictionary[character]
    else:
        return character            # Sinon on retourne la lettre telle quel


def min(character):     # On crée un second dictionnaire majuscule vers minuscule
    dictionary = {
        "A" : "a",
        "B" : "b",
        "C" : "c",
        "D" : "d",
        "E" : "e",
        "F" : "f",
        "G" : "g",
        "I" : "i",
        "J" : "j",
        "K" : "k",
        "L" : "l",
        "M" : "m",
        "N" : "n",
        "O" : "o",
        "P" : "p",
        "Q" : "q",
        "R" : "r",
        "S" : "s",
        "T" : "t",
        "U" : "u",
        "V" : "v",
        "W" : "w",
        "X" : "x",
        "Y" : "y",
        "Z" : "z"
    }
    if character in dictionary:
        return dictionary[character]
    else:
        return character


def myUpper(a=""):
    if type(a) is str or a == "":
        b = ""
        for character in a:     # Pour chaque lettre de la chaine on vérifie si elle est présente dans le dictionnaire
            b += maj(character) # Si oui on la remplace et retourne sa nouvelle valeur
    else:
        print("Il ne faut saisir que des lettres svp.")
        return

    return b

# print(myUpper("bonjour"))


def myLower(a=""):
    if type(a) is str or a == "":
        b = ""
        for character in a:
            b += min(character)
    else:
        print("Il ne faut saisir que des lettres svp.")
        return

    return b

# print(myLower("BONJOUR"))


def myTitle(a=""):
    return re.sub(r'(((?<=\s)|^|-)[a-z])', lambda x: myUpper(x.group()), a)
    
# print(myTitle("je suis une chaine"))

def myClean(a):
    return re.sub(' +', ' ', a)

# print(myClean("je  suis  une  chaine"))


while True:
    var1 = input("Veuillez entrer une chaîne de caractères : ")
    var2 = input("Quelle action souhaitez-cous effectuer ? ")
    if type(var1) is str and var1 != "":
        if var2 == "upper":
            print(myUpper(var1))

        elif var2 == "lower":
            print(myLower(var1))

        elif var2 == "title":
            print(myTitle(var1))

        elif var2 == "clean":
            print(myClean(var1))

    else: 
        var1 = input("Veuillez entrer une chaîne de caractères : ")
