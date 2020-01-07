#!/usr/bin/python3

from random import *

scoreBot = 0
scoreJoueur = 0
gg = -1

def action ():
    print("________________________")
    print()
    print("R. Pierre")
    print("P. Feuiile")
    print("S. Sciseaux")
    print()
    result = str(input("Que faire ? "))
    if result !="R" and result !="P" and result != "S":
        while result !="R" and result !="P" and result != "S":
            print("Désoler, Veuiller choisir entre R, P et S.")
            print()
            result = str (input())
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
            print("Égalité.")
            return 0
        elif resultatBot == "P":
            print("L'ordi gagne cette manche.")
            return 2
        else:
            print("Le joueur gagne cette manche.")
            return 1
    elif resultatJoueur == "P":
        if resultatBot == "P":
            print("Égalité.")
            return 0
        elif resultatBot == "S":
            print("L'ordi gagne cette manche.")
            return 2
        else:
            print("Le joueur gagne cette manche.")
            return 1
    else:
        if resultatBot == "S":
            print("Égalité.")
            return 0
        elif resultatBot == "R":
            print("L'ordi gagne cette manche.")
            return 2
        else:
            print("Le joueur gagne cette manche.")
            return 1
def lesRegles():
    print()
    print("_____________________________________________________")
    print()
    print("But du jeu :")
    print("Être le premier à atteindre le score limite.")
    print()
    print("Chaque joueurs choisit entre Pierre, Feuille et sciseaux.")
    print()
    print("La pierre bat les sciseaux.")
    print("Les sciseaux battent la feuille.")
    print("La feuille bat la pierre.")
    print()
    print("Good Luck, Have Fun.")
    print()
    print("_____________________________________________________")

print()
print("Bienvenu dans le RPS")
print()
rule = str(input("Rapeller les règles ? [o/n] "))
if rule == "o":
    lesRegles()
print()
limitScore = int(input("Score limite : "))
while scoreBot < limitScore and scoreJoueur < limitScore:
    resultatJoueur = action()
    print()
    resultatBot = actionBot()
    print("Action de l'Ordi :",resultatBot)
    print()
    gg = (gagnant(resultatJoueur,resultatBot))
    if gg == 1:
        scoreJoueur += 1
    elif gg == 2:
        scoreBot += 1
    print()
    print("+--------------------+")
    print("| Score Joueur :",scoreJoueur,"  |")
    print("| Score Ordi :",scoreBot,"    |")
    print("+--------------------+")

    print()
if scoreJoueur > scoreBot:
    print()
    print("Le Joueur a gagné.")
else:
    print()
    print("L'Ordi a gagné.")