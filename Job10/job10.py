# On réalise une input pour obtenr le texte
content = input("Que voulez vous écrire dans le fichier ? ")

 # On ouvre (puisqu'i n'exste pas Python va le créer) le fcher 'output.txt', on y écrit le texte, puis on le referme
file = open("/home/padawan/git/starter-python/Job10/output.txt", "a")
file.write(content)
file.close()

# On affiche le fichier dans le terminal
file = open("/home/padawan/git/starter-python/Job10/output.txt", "r")
print(file.read())
file.close()