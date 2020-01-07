#!/usr/bin/python3

from random import *
from pile import *

#Fonctions utilent aux jeu
#TODO intégrer la structure pile

l=["a",2,3,4,5,6,7,8,9,10,10,10,10,"a",2,3,4,5,6,7,8,9,10,10,10,10,"a",2,3,4,5,6,7,8,9,10,10,10,10,"a",2,3,4,5,6,7,8,9,10,10,10,10]
hand=[]
bank=[]
t = 0
tb = 0

def ajout(ret,new):
	for e in new:
		ret.append(e)
	return ret

def tirer(l:list)->list:
	x = randint(0,len(l)-1)
	ret = l[x]
	l.pop(x)
	return ret	

def pioche(l:list,n:int)->list:
	ret = []
	for i in range (n):
		ret.append(tirer(l))

	return ret

def total(mj:list)->int:
	tj = 0
	for e in mj:
		if (e == "a"):
			if tj <= 10:
				tj += 11
			else:
				tj += 1
		else:
			tj += e
	return tj

#afin de piocher 2 cartes au début
p = pioche(l,1)
hand = ajout(hand,p)
t = total(hand)
p1 = pioche(l,1)
bank = ajout(bank,p1)
tb = total(bank)


print("            BLACKJACK            ")
print()
print("Prêt pour une partie de Blackjack")
print()
regle = str(input("Rappeler les règles ? [o/n] "))
if regle == "o":
	print()
	print("But du jeu :")
	print("Obtenir un nombre supèrieur à celui de l'adversaire sans dépasser 21.")
	print()
	print("Si vous obtener un Blackjack, vous gagner automatiquement la manche.")

#a chaque nouveau tour
while t < 21:
	p = pioche(l,1)
	hand = ajout(hand,p)
	t = total(hand)
	if t == 21:
		print("---------------------------")		
		print("Votre main : ")
		print(hand)
		print("Total :",t)
		print()
		print("BLACKJACK !")
		print()
		print()
		print()
		print()
		print()
		break
	elif t > 21:
		print("---------------------------")
		print("Votre main :")
		print(hand)
		print("Votre total :",t)
		print("DOMMMAGE !")	
		print()
		print()
		print()
		print()
		print()
		break
	else:	
		print("---------------------------")	
		print("Votre main : ")
		print(hand)
		print("Total :",t)
		print()
		print("Que faire ?")
		print()
		print("1. Continuer")
		print("2. Se coucher")
		print()
		action = int(input())
		if action != 1 and action != 2:
			while action != 1 and action != 2:
				print("action invalide")
				print()
				print("Que faire ?")
				print()
				print("1. Continuer")
				print("2. Se coucher")
				print()
				action = int(input())
		elif action == 1:
			p2 = pioche(l,1)
			bank = ajout(bank,p2)
			tb = total(bank)

		elif action == 2:
			while tb < 21 and tb <= t:
				if tb <= 21:
					p2 = pioche(l,1)
					bank = ajout(bank,p2)
					tb = total(bank)
				elif tb > t and tb <= 21:
					print("---------------------------")
					print("Votre main : ")
					print(hand)
					print("Votre total :",t)
					print()
					print("Main adverse: ")
					print(bank)		
					print("Total adversaire :",tb)
					print("DÉFAITE !")
					print()
					break
			if tb > 21:
				print("---------------------------")	
				print("Votre main : ")
				print(hand)			
				print("Votre total :",t)
				print()
				print("Main adverse: ")
				print(bank)		
				print("Total adversaire :",tb)
				print("VICTOIRE !")
				print()
				break
			elif tb > t:
				print("---------------------------")
				print("Votre main : ")
				print(hand)
				print("Votre total :",t)
				print()
				print("Main adverse: ")
				print(bank)		
				print("Total adversaire :",tb)
				print("DÉFAITE !")
				print()
				break

			break