import random

liste_facile = ['RAM','Tom','Bit','Pic','Pois','Bug']
liste_medium = ['Chien','Pearl','Mange','Salut','Lampure','Octet','Thonny','Clavier','Cheval','Grand','Maitre','Patate']
liste_difficile = ['Constant','Attaque','Ordinateur','Analyse']
alphabet = 'abcdefghijklmnopqrstuvwxyz'

mot_choisi = ''
difficulté = int(input('Quel difficulté voulez vous choisir? Facile = 1 | Medium = 2 | Difficile = 3  : '))

if difficulté == 1:
    difficulté_choisie = liste_facile
elif difficulté == 2:
    difficulté_choisie = liste_medium
else:
    difficulté_choisie = liste_difficile

def choix_mot(difficulté_choisie):
    mot = random.choice(difficulté_choisie)
    return mot

mot_choisi = choix_mot(difficulté_choisie)
print(mot_choisi)