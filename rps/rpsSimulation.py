#!/usr/bin/python3

from random import *

nbTour = 0
scoreBot = 0
scoreJoueur = 0

#pour savoir combien de cfois chaque coups on été joué
jr = 0
jp = 0
js = 0
br = 0
bp = 0
bs = 0

gg = -1

def action ():
    #choix de l'option du joueur
    result = actionBot()
    return result


def actionBot():
    x=randint(1,3)
    if x == 1:
        return "R"
    elif x == 2:
        return "P"
    else:
        return "S"

def gagnant(resultatJoueur,resultatBot):
    if resultatJoueur == "R":
        if resultatBot == "R":
            #Égalité.
            return 0
        elif resultatBot == "P":
            #L'ordi gagne cette manche.
            return 2
        else:
            #Le joueur gagne cette manche.
            return 1
    elif resultatJoueur == "P":
        if resultatBot == "P":
            #Égalité.
            return 0
        elif resultatBot == "S":
            #L'ordi gagne cette manche.
            return 2
        else:
            #Le joueur gagne cette manche.
            return 1
    else:
        if resultatBot == "S":
            #Égalité.
            return 0
        elif resultatBot == "R":
            #L'ordi gagne cette manche.
            return 2
        else:
            #Le joueur gagne cette manche.
            return 1
print()
fileOut = str(input("Fichier de sortie : "))
limitScore = int(input("Score limite : "))

with open (fileOut,"w") as f1:

    while scoreBot < limitScore and scoreJoueur < limitScore:
        nbTour += 1
        resultatJoueur = action()
        resultatBot = actionBot()
        #Enregistrer les résultat de la manche dans le fichier des résultats

        gg = (gagnant(resultatJoueur,resultatBot))
        if gg == 1:
            scoreJoueur += 1
        elif gg == 2:
            scoreBot += 1

        #ajouter ceci dans le fichier des résultats
        print()
        print("Tour n°",nbTour) #Pour chaque tour
        print(" Score Joueur1 :",scoreJoueur)
        print(" Score Joueur2 :  ",scoreBot)
        print()
        print(" Le Joueur1 a joué :",resultatJoueur)
        print(" Lz Joueur2 a joué :",resultatBot)
        print("-------------------------------------")

    #ajouter ceci dans le fichier des résultats

        
    print()
    print("Résultats finaux.")
    print()
    if scoreJoueur > scoreBot:
        print("Le Joueur1 a gagné.")
        f1.write(str("Le joueur1 a gagné."))
    else:
        print("Le Joueur2 a gagné.")
        f1.write(str("Le joueur2 a gagné."))
    print()
    print(" Nombre de tours :",nbTour)
    print()
    print(" Score Joueur1 :   ",scoreJoueur)

    print(" Score Joueur2 :     ",scoreBot)
    print()
    f1.write(str('\n'))
    f1.write(str("Nombre de tour :  "))
    f1.write(str (nbTour))
    f1.write(str('\n'))
    f1.write(str('Score Joueur1 :    '))
    f1.write(str(scoreJoueur))
    f1.write(str('\n'))
    f1.write(str('Score Joueur2 :      '))
    f1.write(str(scoreBot))
    f1.write(str('\n'))


f1.close()

