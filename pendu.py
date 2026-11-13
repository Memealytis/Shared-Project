from fonctions import *
from donnees import *
import random

liste_facile = ['RAM','Tom','Bit','Pic','Pois','Bug']
liste_medium = ['Chien','Pearl','Mange','Salut','Lampure','Octet','Thonny','Clavier','Cheval','Grand','Maitre','Patate']
liste_difficile = ['Constant','Attaque','Ordinateur','Analyse']
alphabet = 'abcdefghijklmnopqrstuvwxyz'

print("Bienvenu sur notre jeu de pendu")

continuer = True

while continuer:
    erreurs = 0
    win = 0
    liste_deviné = []

    # Choix de la difficulte
    difficulté = int(input('Quel difficulté voulez vous choisir? Facile = 1 | Medium = 2 | Difficile = 3 : '))

    if difficulté == 1:
        difficulté_choisie = liste_facile
    elif difficulté == 2:
        difficulté_choisie = liste_medium
    else:
        difficulté_choisie = liste_difficile

    mot_choisi = choix_mot(difficulté_choisie)
    mot_choisi = mot_choisi.lower()

    # Boucle de la partie
    while win == 0 and erreurs < len(DRAWINGS) - 1:
        print(DRAWINGS[erreurs])
        print("Votre progres:", show_word(mot_choisi, liste_deviné))
        
        deviner = int(input("Voulez vous deviner une lettre ou un mot? Lettre = 1 | Mot = 2 : "))
        
        if deviner == 1:
            lettre_choisi = input("Deviner une lettre : ").lower()
            liste_deviné.append(lettre_choisi)
            
            if lettre_choisi not in mot_choisi:
                erreurs += 1
                print("Mauvaise Lettre !!")
            else:
                print('Bien joue !!')
        else:
            mot_proposé = input("Deviner un mot : ").lower()
            if mot_proposé == mot_choisi:
                win = 1
            else:
                erreurs += 1
                print("Mauvais mot !!")

        
        if show_word(mot_choisi, liste_deviné) == mot_choisi:
            win = 1

    #win lose 
    if win == 1:
        print("Vous avez gagne ! Le mot etait :", mot_choisi)
    else:
        print(DRAWINGS[len(DRAWINGS) - 1])
        print("Vous avez perdu ! Le mot etait :", mot_choisi)

    #replay
    reponse_rejouer = rejouer()
    if reponse_rejouer == 'non':
        continuer = False

print("Fin du jeu")
