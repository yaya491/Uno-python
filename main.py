def creer_paquet():
    couleurs = ["rouge", "bleu", "vert", "jaune"]
    valeurs = ["0","1","2","3","4","5","6","7","8","9"]

    paquet = []

    for couleur in couleurs:
        for valeur in valeurs:
            paquet.append((couleur, valeur))

    return paquet


import random

couleurs = ["rouge", "bleu", "vert", "jaune"]

def distribution_cartes():
    for i in range(7): #Distribution des 7 catres par joueur
        nombre = random.randint(0, 9)
        couleur = random.choice(couleurs)
        print(nombre, couleur)
        
while True:
    joueurs = int(input("Combien de joueurs ?"))
    if 2 <= joueurs <= 10:
        break #donne la possibilité de quitter une boucle
    print("Nombre de joueur invalide : choisit un autre nombre qui est compris entre 2 et 10 .")

for j in range(joueurs):
    print("Joueur", j + 1)
    distribution_cartes()
    
    print()