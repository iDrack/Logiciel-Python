#!/usr/bin/python3

from random import *

KM_VOYAGE = 300
KM_NORM_MIN = 10
KM_NORM_MAX = 15
KM_RAP_MIN = 20
KM_RAP_MAX = 25
AVANTAGE_VOYAGEUR = 20
GOURDE_PLEINE = 12
MORT_SOIF = 4
MORT_FATIGUE = 4
DIF_AIDE = 3
AVANCE_NATIFS = 4
ALCOOL = 3
SPECIAL = 9
BLIZZ = 5


print("")
print("LE JEU DU CAP'TAIN !")
print("Vous avez volé tout l'or du cap'tain.")
print("Il veut le récupérer, ces délicieux filets de colin.")
print("Votre objectif est de survivre à la traversée de 300 km sans être attrapé(e).")

km_voyageur = 0
km_natifs = km_voyageur-AVANTAGE_VOYAGEUR
gourde = GOURDE_PLEINE//2.
soif = 0
fatigue = 0
bu = 0

option = 0

#options du joueur

while option != 6:
    print("")
    print("OPTIONS")
    print("")
    print("1. Boire")
    print("2. Avancer pépére")
    print("3. Avancer rapidement")
    print("4. Repos")
    print("5. Attendre de l'aide")
    print("6. Abandonner")
    print("")
    print("Qu'allez-vous faire ?")
    option = int(input(""))
    print("")

#déterminant du spécial

    spe = randint(0,SPECIAL)
    blizar = randint(0,BLIZZ)

#détermine si un blizzard spawn ou non,(si oui -> on peut rien faire)

    if blizar == 0:
        print("")
        print("Un puissant blizzard se léve.")
        print("Vous ne pouvez rien faire")
        option == 7

#actions du joueur et leurs effets

    if blizar !=0:
        if option == 1:
            if gourde == 0:

                print("La vodka est vide, blyat !")
            else:
                soif = 0
                gourde -= 1
                print("Vous avez bu une gorgée de vodka.")
                bu += 1

        elif option == 2:
            fatigue += 1
            tmp=randint(KM_NORM_MIN,KM_NORM_MAX)
            km_voyageur += tmp
            print("Vous venez de parcourir",tmp,"km")
            bu = 0
            soif += 1

        elif option == 3:
            fatigue += 2
            tmp=randint(KM_RAP_MIN,KM_RAP_MAX)
            km_voyageur += tmp
            print("Vous venez de parcourir",tmp,"km")
            bu = 0
            soif += 1


        elif option == 4:
            fatigue = 0
            print("Vous laissez Igor l'ours sibérian se reposer pendant 3h.")
            bu = 0
            soif += 1

        elif option == 5:
            aide = randint(0,DIF_AIDE)
            if aide == 0:
                if gourde >= GOURDE_PLEINE:
                    print("Malheureux ! Elle est déjà pleine, tu perds ton temps !")
                    bu = 0
                else:
                    print("Un voyageur vous aide.")
                    print("")
                    print("Voyageur: Cyka Blyat.")
                    print("")
                    if gourde == 10:
                        gourde += 2
                    elif gourde == 11:
                        gourde += 1
                    else:
                        gourde += 3
                    bu = 0
            else:
                print("Vous ne trouvez pas d'aide. DOMMAGE !")
                bu = 0

        elif option == 7:
            bu == 0

        else :
            print("Prof Chen: Chaque choses en son temps trouduc !")
        print ("Votre gourde contient",gourde,"gorgée(s) de vodka.")        
        print("Vous avez parcouru un total de",km_voyageur,"km")
        print("")
        

#conditions de défaite ou de victoire

    if km_voyageur >= KM_VOYAGE:
        print("")
        print ("Vous avez quitté la Sibérie et vous avez pû voler tout le trésor du Cap'tain, des délicieux fillet de colin, le véritable trésor du Cap'tain !!")
        break

    if spe != 0:
        russ = randint(0,AVANCE_NATIFS)
        if russ == 0:
            rtmp=randint(KM_RAP_MIN,KM_RAP_MAX)
            km_natifs = km_natifs+rtmp
        elif russ == 1:
            rtmp=randint(KM_NORM_MIN,KM_NORM_MAX)
            km_natifs = km_natifs+rtmp

    if km_natifs >= km_voyageur:
        fin = randint(0,1)
        print("")
        if fin == 1:
            print ("Le Cap'tain et son équipage vous ont rattrapé ! Comme punissement vous devrez faire le tour du monde à bord de son navire.")
        elif fin == 0:
            print("Le Cap'tain vous a rattrapé ! Au Gulag !")
        break
    else:
        print ("Vous avez",km_voyageur-km_natifs,"km d'avance sur le Cap'tain.")

   

    if soif >= MORT_SOIF:
        print("")
        print("Vous n'êtes plus saoul et reprennez vos esprits. Tout ceci n'était qu'une allussination.")
        break

    if soif == 0:
        print("Vous n'avez pas soif.")
    elif soif == 1:
        print("Vous avez soif.")
    elif soif == 2:
        print("Vous avez beaucoup soif.")
    elif soif == 3:
        print("À boire, vite !")

    if fatigue >= MORT_FATIGUE:
        print("")
        print("Igor l'ours sibérian est mort. RIP in PEPERONNI")
        print ("Le Cap'tain et son équipage vous ont rattrapé ! Comme punissement vous devrez faire le tour du monde à bord de son navire.")
        break
    elif fatigue == 0:
        print("Igor l'ours sibérian est en pleine forme.")
    elif fatigue == 1:
        print("Igor l'ours sibérian commence à fatiguer.")
    elif fatigue == 2:
        print("Igor l'ours sibérian est très fatigué.")
    else:
        print("Igor l'ours sibérian a besoin de repos, viiite!")

#événements spéciaux

    if spe == 0:
        print("")
        print("Vous trouvez un magasin Absolut Vodka et remplissez votre gourde, vous buvez aussi un coup.")
        gourde = GOURDE_PLEINE
        soif = 0
        bu += 1

    if bu == 3:
        print("")
        print("Vous faites un comma éthylique.")
        break

    if km_voyageur-km_natifs <= 5:
        print("Vous entendez au loin: Cheeki Breeki !")
