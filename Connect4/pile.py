#!/usr/bin/python3

def initPile(l:list):
    if estVide(l):
        n=int(input("Hauteur de la pile ? "))
        for i in range (0,n):
            x = int(input("? "))
            empiler(l,x)
    else:
        print(estVide)
    return l
 
def empiler(l:list,x:int):
    l.append (x)
    return l

def estVide(l:list):
    return len(l) == 0

def dépiler(l:list):
    if (not estVide(l)):
        return l.pop()

def sommet(liste:list):
    return liste[-1]
