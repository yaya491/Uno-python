"""
import random

def creer_paquet():
    couleurs = ["rouge", "bleu", "vert", "jaune"]
    valeurs = ["0","1","2","3","4","5","6","7","8","9"]
    paquet = []
    for couleur in couleurs:
        for valeur in valeurs:
            paquet.append((couleur, valeur))
    return paquet

def distribution_cartes(paquet, nb_cartes=7):
    main = []
    for _ in range(nb_cartes):
        carte = paquet.pop()
        main.append(carte)
    return main

def nombre_joueurs():
    while True:  # Boucle jusqu'à une entrée valide
        joueurs = int(input("Combien de joueurs ? "))
        if 2 <= joueurs <= 10:
            return joueurs
        print("Nombre invalide : choisir entre 2 et 10.")

# Programme principal
paquet = creer_paquet()
random.shuffle(paquet)

joueurs = nombre_joueurs()

for j in range(joueurs):
    print(f"Joueur {j + 1} :")
    main = distribution_cartes(paquet)
    for carte in main:
        print(" ", carte[1], carte[0])
    print()
"""
game_start = True
card_colors = ["Red", "Green", "Blue", "Yellow"]
card_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
card_specials = ["Skip", "Reverse", "Draw Two", "Wild", "Wild Draw Four"]
players = None

while game_start:
    players = int(input("Combien de joueurs? (2-10): "))
    while players < 2 or players > 10:
        print("Nombre de joueurs invalide. Veuillez entrer un nombre entre 2 et 10.")
        players = int(input("Combien de joueurs? (2-10): "))
    print("Le jeu commence avec", players,"joueurs!")
