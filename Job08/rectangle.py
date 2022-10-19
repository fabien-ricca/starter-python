# Demander largeur et hauteur
# utiliser des '|' pour les côtés
# Utiliser des '-' pour le haut et le bas
# Utiliser des espaces pour le remplir

#  |-----|
#  |     |
#  |     |
#  |-----|


H=int(input("Quelle hauteur ? "))
L=int(input("Quelle largeur ? "))


for i in range (0, H):
    rec = " "
    for j in range (0, L):
        if i == 0 or i == H - 1:
            rec += "-"
        else:
            rec += " "
    rec += "|"
    print(rec)
