
# On ouvre le fichier, on met le contenu dans une variable, et on le referme
text = open("/home/padawan/git/starter-python/Job12/data.txt", "r")
file = text.read()    
text.close()

# On crée une liste à partir du contenu du fichier
list = file.split() 

# On affche le nombre de mots
print("Il y a", len(list), "mots.")  


