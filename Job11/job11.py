# On ouvre le fichier, on met le contenu dans une variable
file = open("/home/padawan/git/starter-python/Job11/domains.xml", "r")

# On crée une liste vide, et une varible avec le contenu du fichier
list = []
text = file.readlines()

# On crée la boucle pour ajouter chaque ligne tu tete à la liste
for line in text:
    line = line.replace("</column>\n", "").strip()
    list.append(line)
file.close()

# On créer une 2eme liste qui ne contiendra que les lignes qui comporte la cdc '<column name="domain">'
list2 = [s for s in list if '<column name="domain">' in s]

# On compte le nombre d'éléments de cette liste
print(len(list2))
