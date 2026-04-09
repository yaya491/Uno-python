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
card_colors = ["Rouge", "Vert", "Bleu", "Jaune"]
card_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
card_specials = ["Passer", "Inverser", "Piocher Deux", "Générique", "Générique Piocher Quatre"]
players_hand = {}


def allcards():
    all_cards = []
    for i in range(len(card_colors)):
        for j in range(len(card_values)):
            if card_values[j] == "0":
                all_cards.append("0 " + card_colors[i])
            else:
                all_cards.extend([card_values[j] + " " + card_colors[i]] * 2)
    return all_cards
print(allcards())


while game_start:
    count = int(input("combien de joueurs? (2-10): "))
    while count < 2 or count > 10:
        print("Nombre de joueurs invalide. Veuillez entrer un nombre entre 2 et 10.")
        count = int(input("Combien de joueurs? (2-10): "))
    for i in range(count):
        players_hand[f"Joueur {i + 1}"] =  []
    print(players_hand)
    break