#  aa/\aa
#  a/  \a
#  /____\

# On réalise une input pour obtenir la hauteur
H= int(input ("Quelle hauteur souhaitez-vous pour le triangle ? "))

for i in range (0,H):
    if i == 0:
        # Sommet du triangle
        print (" "*(H-1) +"/" + "\\") 
    elif i == (H -1):
        # Base du triangle
        print ("/" + "_" * (i*2) + "\\") 
    else:
        # Centre du triangle
        print (" "*(H-i-1)+"/"  +" " *(i*2) + "\\") 