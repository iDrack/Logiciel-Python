#!/usr/bin/python3

import os


def initMat(n,p):
    """
    name: initMat

    Creer une matrice m de taille n,p
    C'est une liste de liste

    :param n: nombre de lignes
    :param p: nombre de colonnes
    :type n: int
    :type p: int

    :return: matrice m
    :rtype: list de list
    """
    l =[]
    for i in range (0,n):
        li=[]
        for j in range (0,p):
            li.append(0)
        l.append(li)
    return l

def afficher(m):
    for i in range (len(m)):
        for j in range (len(m[i])):
                print(m[i][j],end=" ")
        print(end = '\n')
        
