import random

liste_facile = ['RAM','Tom','Bit','Pic','Pois','Bug']
liste_medium = ['Chien','Pearl','Mange','Salut','Lampure','Octet','Thonny','Clavier','Cheval','Grand','Maitre','Patate']
liste_difficile = ['Constant','Attaque','Ordinateur','Analyse']
alphabet = 'abcdefghijklmnopqrstuvwxyz'

mot_choisi = ''
difficulté = int(input('Quel difficulté voulez vous choisir? Facile = 1 | Medium = 2 | Difficile = 3'))

liste_deviné = []

mot_choisi = choix_mot(difficulté_choisie)
mot_choisi = mot_choisi.lower()
#print(mot_choisi)

# -- 2 CONFIGURATION DU JEU -- 
if difficulté == 1:
    difficulté_choisie = liste_facile
elif difficulté == 2:
    difficulté_choisie = liste_medium
else:
    difficulté_choisie = liste_difficile

def choix_mot(difficulté_choisie):
    mot = random.choice(difficulté_choisie)
    return mot

def show_word(mot_choisi, liste_deviné):
    resultat = ''
    pass

while win == 0:
    deviner = int(input('Voulez vous deviner une lettre ou un mot? Lettre = 1 | Mot = 2'))
    if deviner == 1:
        lettre_choisi = input("Deviner une lettre")
    else:
        mot_choisi = input("Deviner un mot")
