#!/usr/bin/python3

def initPile(l:list):
    # initialise un pile à partir d'une liste
    if estVide(l):
        n=int(input("Hauteur de la pile ? "))
        for i in range (0,n):
            x = int(input("? "))
            empiler(l,x)
    else:
        print(estVide)
    return l

def empiler(l:list,x:int):
    # rajoute x en haut de pile
    l.append (x)
    return l

def estVide(l:list):
    # vérifie si la pile est vide
    return len(l) == 0

def dépiler(l:list):
    # supprime le sommet de la pile 
    if (not estVide(l)):
        return l.pop()

def sommet(liste:list):
    # retourne l'élément au sommet de la pile
    return liste[-1]
