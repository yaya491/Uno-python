#Partie 1: création et gestion du paquet de cartes.On a commencé par cette partie parce que c'est la base du jeu
import random #pour la fonction qui melangfe les cartes avec "shuffle"
def creer_paquet(): #Cette fonction crée toutes les cartes du jeu UNO et les met dans une liste
    couleurs = ["rouge", "bleu", "vert", "jaune"]
    valeurs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
               "passer", "inverser", "+2"]  
    #on met tout dans une liste
    #on a ajouté les cartes spéciales passer, inverser et +2

    paquet = [] #liste vide qui contient les cartes futurs du paquets

    for couleur in couleurs: #boucle imbriquée: pour chaque couleur on parcourt toutes les valeurs, ça permet de créer une carte de chaque combinaison couleur/valeur
        for valeur in valeurs: # on crée toutes les combinaisons couleur / valeur 
            paquet.append((couleur, valeur)) #chaque carte est un TUPLE (couleur, valeur)

            #dans le UNO, toutes les cartes sauf le 0 sont en double, donc si la valeur n'est pas "0" on rajoute une deuxième fois la même carte
            if valeur != "0":
                paquet.append((couleur, valeur))  #deuxième exemplaire de la carte

    return paquet  #on retourne la liste complète de toutes les cartes


def melanger_paquet(paquet): #Cette fonction mélange le paquet de cartes de maniere aleatoire en modifiant directement son ordre en mémoire (ca ne crée pas une nouvelle liste). Chaque carte change donc de position de façon aléatoire
    random.shuffle(paquet)


def distribuer_cartes(paquet, nombre_cartes=7):#Cette fonction prend nb_cartes cartes depuis le paquet et les donne à un joueur
    main = [] #la main du joueur:une liste vide au départ

    for i in range(nombre_cartes):  #répète nb_cartes le nombre de fois necessaire 
        if len(paquet) > 0:   #on vérifie que le paquet est pas vide avant de piocher
            carte = paquet.pop()  #pop() enlève et retourne la dernière carte du paquet
            main.append(carte)   #ajoute la carte à la main du joueur

    return main #on retourne la liste des cartes du joueur


def carte_jouable(carte, carte_dessus):#Cette fonction vérifie si une carte peut être jouée sur la carte du dessus, elle retourne True si c'est jouable, False sinon
    #une règles du UNO:on peut jouer une carte si elle a soit la même couleur que la carte du dessus soit la même valeur que la carte du dessus
    if carte[0] == carte_dessus[0]: #carte[0] c'est la couleur, on compare les couleurs
        return True  # même couleur, alors on peut jouer
    if carte[1] == carte_dessus[1]: #carte[1] c'est la valeur, compare les valeurs
        return True #même valeur, alors on peut jouer
    return False  #si aucune des deux conditions, la carte n'est pas jouable