# On importe regex
import re

# On demande en console de saisir le nombre de caractères
nbr_letter = int(input("Entrez un nombre entier : "))

# On crée une variable qui va conenir le resultat de la recherche de mots en foctions du nombre de caractères
with open("/home/padawan/git/starter-python/Job12/data.txt") as file:
   nbr_words = re.findall(r"\b[a-zA-Z]{%d}\b" %(nbr_letter), file.read())

# On affiche le nombre de mots trouvés
print("Nous avons trouvé", len(nbr_words), "mots constitués de", nbr_letter, ".")
