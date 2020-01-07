#!/usr/bin/python3

from random import *

#valeur ASCII de 33 à 126

mdp = []

taille = int(input("Taille du mot de passe (taille minimum conseillée 8)? "))

def genChar():
    x = randint(33,126)
    return x

print()
print("Votre mot de passe :")

for i in range(taille):
    charInt = genChar()
    char = chr(charInt)
    mdp.append(char)
motdepasse = ''.join(mdp)
print(motdepasse)
print()

rep = str(input("Enregistrer le mot de passe ? (o/n) ")) 

if rep == "o":
    nom = str(input("Description : "))
    identifiant = str(input("Identifiant du mot de passe : "))
    fileOut = str(input("Fichier de sortie : "))
    
    #Modifier pour pouvoir l'implémenter avec JS

    with open (fileOut, "a") as f1:
        f1.write(str('\n'))
        f1.write(str('nom : ')+nom)
        f1.write(str('\n'))
        f1.write(str('identifiant : ')+identifiant)
        f1.write(str('\n'))
        f1.write(str('mot de passe : ')+motdepasse)
        f1.write(str('\n'))
    f1.close
    print()
    print("Mot de passe enregistré !")
    print()
