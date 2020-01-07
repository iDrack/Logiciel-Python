#!/usr/bin/python3

import ctypes
from matrice import *

m = initMat(6,7) #correspond a init(jeu)

choix = "1 2 3 4 5 6 7"

def jouer(joueur):
    #Le joueur choisit la oclonne où il veut joueur
    print(choix)
    print("")
    afficher(m)
    print("")
    print("Joueur",joueur,"c'est à vous de jouer:")
    colonne = int(input())
    return colonne

def update(m,joueur,colonne):
    #Ajoute un jeton du joueur en train de jouer selon la colonne choisit
    ligne =5
    while m[ligne][colonne]!=0:
        ligne -= 1 
        
    m[ligne][colonne] = joueur 
    
    
    return m
    
def estRempli(m):
    #Vérifie si le plateau de jeu est plein
    for e in m[0]:
        if (e == 0):
            return False
    return True

def ligne4(jeu,joueur):
    for i in range (len(jeu)):
        for j in range (len(jeu[i])-3):
            if jeu[i][j] == joueur and jeu[i][j+1] == joueur and jeu[i][j+2] == joueur and jeu[i][j+3] == joueur:
                return True
                
def colonne4(jeu,joueur):
    for i in range (len(jeu)-3):
        for j in range (len(jeu[i])):
            if jeu[i][j] == joueur and jeu[i+1][j] == joueur and jeu[i+2][j] == joueur and jeu[i+3][j] == joueur:
                return True

def diagonal4(jeu,joueur):
    for i in range(len(jeu)):
        for j in range(len(jeu[i])):
            if jeu[i][j] == joueur and (j+1 < len(jeu[i])) and j+2 < len(jeu[i]) and j+3 < len(jeu[i]):
                if jeu[i-1][j+1] == joueur and jeu[i-2][j+2] == joueur and jeu[i-3][j+3] == joueur:
                    return True
                elif jeu[i-1][j-1] == joueur and jeu[i-2][j-2] == joueur and jeu[i-3][j-3] == joueur:
                    return True

for i in range (1,44):
    #Boucle principal
    joueur = i%2 == 0
    joueur += 1

    colonne = jouer(joueur)-1

    #Vérifie là où le joueur veut jouer
    while colonne < 0 or colonne > 6:
        colonne = jouer(joueur)-1
    m = update(m,joueur,colonne)
    print()
    #test si il y a un gagnant
    if ligne4(m,joueur) or colonne4(m,joueur) or diagonal4(m,joueur):
        print("---------------------")
        print()
        afficher(m)
        print()
        print("Le joueur",joueur,"a gagné !")
        break
    if estRempli(m):
        break




    
    


