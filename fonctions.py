import random

def choix_mot(difficulté_choisie):
    mot = random.choice(difficulté_choisie)
    return mot

def show_word(mot_choisi, liste_deviné):
    resultat = ''
    for element in mot_choisi:
        if element in liste_deviné:
            resultat = resultat + element
        else:
            resultat = resultat + '_'
    return resultat

def rejouer():
    reponse = ''
    while reponse != 'oui' and reponse != 'non':
        reponse = input("Voulez vous rejouer? oui ou non : ")
    return reponse
