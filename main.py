print("hello world")
print("yannis est gay")

def creer_paquet():
    couleurs = ["rouge", "bleu", "vert", "jaune"]
    valeurs = ["0","1","2","3","4","5","6","7","8","9"]

    paquet = []

    for couleur in couleurs:
        for valeur in valeurs:
            paquet.append((couleur, valeur))

    return paquet