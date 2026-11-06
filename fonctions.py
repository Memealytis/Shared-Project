from donnees import *
import random

# --- 1. SETUP DES VARIABLES ---

liste_facile = ['RAM','Tom','Bit','Pic','Pois','Bug']
liste_medium = ['Chien','Pearl','Mange','Salut','Lampure','Octet','Thonny','Clavier','Cheval','Grand','Maitre','Patate']
liste_difficile = ['Constant','Attaque','Ordinateur','Analyse']
alphabet = 'abcdefghijklmnopqrstuvwxyz'

mot_choisi = ''

liste_deviné = []

erreurs = 0

win = 0

difficulté = int(input('Quel difficulté voulez vous choisir? Facile = 1 | Medium = 2 | Difficile = 3 : '))

if difficulté == 1:
    difficulté_choisie = liste_facile
elif difficulté == 2:
    difficulté_choisie = liste_medium
else:
    difficulté_choisie = liste_difficile


# --- 2. DEFINITION DES FONCTIONS ---

def choix_mot(difficulté_choisie):
    mot = random.choice(difficulté_choisie)
    return mot

mot_choisi = choix_mot(difficulté_choisie)
mot_choisi = mot_choisi.lower()
#print(mot_choisi)

def show_word(mot_choisi, liste_deviné):
    resultat = ''
    for element in mot_choisi:
        if element in liste_deviné:
            resultat = resultat + element
        else:
            resultat = resultat + '_'
            
    return resultat

def lettre_demandé():
    pass

def mot_trouvee():
    global win
    if show_word(mot_choisi, liste_deviné) == mot_choisi:
        win = 1

def rejouer():
    reponse = ''
    while reponse != 'oui' or reponse != 'non':
        reponse = input("voulez vous rejouer? oui ou non")



# --- 3. CONFIGURATION DU JEU ---

while win == 0:
    
    print("Votre progres:", show_word(mot_choisi, liste_deviné))
    
    deviner = int(input('Voulez vous deviner une lettre ou un mot? Lettre = 1 | Mot = 2 : '))
    if deviner == 1:
        lettre_choisi = input("Deviner une lettre : ")
    else:
        mot_choisi = input("Deviner un mot : ")
