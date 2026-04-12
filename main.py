import random  # on importe random pour pouvoir mélanger le paquet avec shuffle

# Projet NSI - Jeu UNO en Python
#Réalisé par Yannis et André

# Répartition du travail :
#Yannis: creer_paquet, melanger_paquet, distribuer_cartes, afficher_main, carte_jouable, boucle principale du jeu
# André: creer_joueurs,afficher_carte_du_dessus, joueur_pioche, jouer_tour, verifier_victoire


# PARTIE 1 : création et gestion du paquet de cartes (fait par Yannis). On a commencé par cette partie parce que c'est la base du jeu

def creer_paquet(): #Cette fonction crée toutes les cartes du jeu UNO et les met dans une liste
    couleurs = ["rouge", "bleu", "vert", "jaune"]
    valeurs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
               "passer", "inverser", "+2"]  
    #on met tout dans une liste
    #on a ajouté les cartes spéciales passer, inverser et +2

    paquet = []  # liste vide qui contient les cartes futurs du paquets

    for couleur in couleurs: #boucle imbriquée: pour chaque couleur on parcourt toutes les valeurs, ça permet de créer une carte de chaque combinaison couleur/valeur
        for valeur in valeurs: # on crée toutes les combinaisons couleur / valeur 
            paquet.append((couleur, valeur)) #chaque carte est un TUPLE (couleur, valeur)

            # dans le UNO, toutes les cartes sauf le 0 sont en double
            # donc si la valeur n'est pas "0", on rajoute une deuxième fois la même carte
            if valeur != "0":
                paquet.append((couleur, valeur))  #deuxième exemplaire de la carte

    return paquet  #on retourne la liste complète de toutes les cartes


def melanger_paquet(paquet): #Cette fonction mélange le paquet de cartes de maniere aleatoire en modifiant directement son ordre en mémoire (ca ne crée pas une nouvelle liste). Chaque carte change donc de position de façon aléatoire
    random.shuffle(paquet)


def distribuer_cartes(paquet, nombre_cartes=7):#Cette fonction prend nb_cartes cartes depuis le paquet et les donne à un joueur
    main = [] #la main du joueur: une liste vide au départ

    for i in range(nombre_cartes):  #répète nb_cartes le nombre de fois necessaire 
        if len(paquet) > 0:   #on vérifie que le paquet est pas vide avant de piocher
            carte = paquet.pop()  #pop() enlève et retourne la dernière carte du paquet
            main.append(carte)   #ajoute la carte à la main du joueur

    return main #on retourne la liste des cartes du joueur



# PARTIE 2 : création et gestion des joueurs (fait par André)

def creer_joueurs(nb_joueurs, paquet): #Cette fonction crée tous les joueurs et leur distribue leurs cartes. On a utilisé un dictionnaire pour les joueurs comme ca on peut accéder à la main d'un joueur avec son nom directement
 # dictionnaire : clé = nom du joueur et valeur = main du joueur
    joueurs = {}  # dictionnaire vide qui va se remplir dans la boucle

    for i in range(nb_joueurs):  #on fait ça autant de fois qu'il y a de joueurs
        nom = "Joueur " + str(i + 1) #on donne un nom automatique au joueur: "Joueur 1", "Joueur 2"...
        # str(i + 1) parce que i commence à 0 mais les joueurs commencent à 1

        # on appelle distribuer_cartes pour donner 7 cartes à ce joueur et on stocke la liste de cartes dans le dictionnaire avec le nom comme clé
        joueurs[nom] = distribuer_cartes(paquet)

    return joueurs  #on retourne le dictionnaire avec tous les joueurs et leurs mains


def afficher_main(nom, main): #Cette fonction affiche les cartes d'un joueur dans la console. On a fait une fonction à part pour ça parce qu'on en a besoin à plusieurs endroits
   

    print("Main de " + nom + " ---")  # titre avec le nom du joueur

    for i in range(len(main)): #on parcourt toute les cartes du joueur
        carte = main[i]        #on récupère la carte à la position i
        # carte[1] c'est la valeur 
        # carte[0] c'est la couleur 
        # on affiche "numéro. valeur couleur"
        print(str(i + 1) + ". " + carte[1] + " " + carte[0])



def afficher_carte_du_dessus(carte):#affiche la carte qui est sur le dessus de la pile de défausse, c'est important car le joueur doit voir cette carte avant de choisir quoi jouer
    print("[Carte du dessus : " + carte[1] + " " + carte[0] + "]")


def carte_jouable(carte, carte_dessus):#Cette fonction vérifie si une carte peut être jouée sur la carte du dessus, elle retourne True si c'est jouable, False sinon
    
    #Une règles du UNO : on peut jouer une carte si elle a soit la même couleur que la carte du dessus soit la même valeur que la carte du dessus

    
    if carte[0] == carte_dessus[0]: #carte[0] c'est la couleur, on compare les couleurs
        return True  # même couleur, alors on peut jouer

    # carte[1] c'est la valeur, compare les valeurs
    if carte[1] == carte_dessus[1]:
        return True  # même valeur, alors on peut jouer

    return False  #si aucune des deux conditions, la carte n'est pas jouable


def joueur_pioche(paquet, defausse, main):  #Cette fonction fait piocher une carte au joueur et elle gère aussi le cas où le paquet est vide 

    # si le paquet est vide, on prend la défausse pour reformer un paquet
    if len(paquet) == 0:
        print("Le paquet est vide, on remelange la defausse !")  # on garde la dernière carte de la défausse (celle du dessus)
        derniere = defausse[-1]  # defausse[-1] = dernier élément de la liste
        for carte in defausse[:-1]:
            paquet.append(carte)  # on remet chaque carte dans le paquet

        defausse.clear()         # on vide complètement la défausse
        defausse.append(derniere)  # on remet juste la dernière carte sur la défausse
        melanger_paquet(paquet)  # on mélange le nouveau paquet

    if len(paquet) > 0: # maintenant on vérifie à nouveau si le paquet a des cartes
        nouvelle_carte = paquet.pop()      # on pioche la carte du dessus
        main.append(nouvelle_carte)        # on l'ajoutela carte à la main du joueur
        print("Vous avez pioché : " + nouvelle_carte[1] + " " + nouvelle_carte[0])   # on affiche quelle carte a été piochée
        return nouvelle_carte  
    else:
        print("Plus de cartes disponibles !")
        return None  # on retourne None pour signaler qu'on a rien pu piocher


def verifier_victoire(main):# Vérifie si un joueur a gagné, c'est-à-dire s'il n'a plus de cartes
    return len(main) == 0



# PARTIE 3 : effets des cartes spéciales 

def appliquer_effet(carte, joueurs, ordre, index_courant, paquet, defausse): # Cette fonction applique l'effet d'une carte spéciale
    valeur = carte[1]  # on récupère la valeur de la carte

    noms = list(joueurs.keys())   # on récupère la liste des noms des joueurs depuis le dictionnaire puis on transforme les clés du dictionnaire en liste
    nb = len(noms)  # nombre total de joueurs, utile pour le modulo juste après

    if valeur == "passer":
        print("Carte PASSER ! Le joueur suivant passe son tour.")   # pour faire passer un tour on avance l'index d'un joueur de plus
        index_courant = (index_courant + ordre) % nb   # le % nb (modulo) sert à revenir à 0 quand on dépasse le dernier joueur
        return index_courant, ordre  # on retourne les deux valeurs modifiées

    elif valeur == "inverser":
        print("Carte INVERSER ! Le sens du jeu change.")
        ordre = ordre * -1    # en multipliant par -1 on change le sens
        return index_courant, ordre

    elif valeur == "+2":  # le joueur suivant doit piocher 2 cartes et passer son tour
        # d'abord on calcule quel est le joueur suivant
        index_suivant = (index_courant + ordre) % nb # On dois dabord calculer quel est le joueur suivant
        nom_suivant = noms[index_suivant]  # on récupère son nom dans la liste
        print("Carte +2 ! " + nom_suivant + " doit piocher 2 cartes.")     # on fait piocher 2 cartes au joueur suivant

        # on appelle joueur_pioche deux fois
        joueur_pioche(paquet, defausse, joueurs[nom_suivant])
        joueur_pioche(paquet, defausse, joueurs[nom_suivant])

        # le joueur suivant passe aussi son tour
        index_courant = (index_courant + ordre) % nb
        return index_courant, ordre

    return index_courant, ordre   # si c'est aucune carte spéciale connue, on retourne les valeurs sans les changer



# PARTIE 4 : déroulement d'un tour de jeu

def jouer_tour(nom, main, carte_dessus, paquet, defausse):  # C'est la fonction principale pour gérer le tour d'un joueur (alaffichage, le choix de la carte et si on dois piocher ou pas
    afficher_carte_du_dessus(carte_dessus)  # on montre la carte du dessus avant tout
    afficher_main(nom, main)               # on affiche les cartes du joueur

    # on cherche quelles cartes du joueur sont jouables
    # on stocke leurs INDEX dans une liste (pas les cartes elles-mêmes)
    # comme ça on peut retrouver la carte avec main[index] facilement
    cartes_jouables = []  # liste vide au départ
    for i in range(len(main)):              # on parcourt toutes les cartes de la main
        if carte_jouable(main[i], carte_dessus):  # si la carte est jouable on ajoute son index à la liste
            cartes_jouables.append(i)             

    print("\nC'est à vous de jouer, " + nom + " !")

    if len(cartes_jouables) == 0: # cas où le joueur n'a aucune carte jouable : il doit piocher obligatoirement
        print("Aucune carte jouable. Vous devez piocher.")
        input("Appuyez sur Entrée pour piocher")
        nouvelle = joueur_pioche(paquet, defausse, main) # on fait piocher une carte

        # si la carte piochée est jouable, le joueur peut choisir de la jouer
        if nouvelle is not None and carte_jouable(nouvelle, carte_dessus):
            print("La carte piochée est jouable !")
            choix = input("Voulez-vous la jouer ? (o/n) : ")
            if choix.lower() == "o":  # .lower() pour accepter "O" et "o"
                main.remove(nouvelle) # on enlève la carte de la main
                defausse.append(nouvelle)  # on la met sur la défausse
                return nouvelle  # on retourne la nouvelle carte du dessus
        return carte_dessus

    else:
        print("Cartes jouables :")
        for idx in cartes_jouables: # on affiche chaque carte jouable avec son numéro dans la main
           
            # idx+1 parce que l'affichage commence à 1 mais les index commencent à 0
            print("  -> " + str(idx + 1) + ". " + main[idx][1] + " " + main[idx][0])  # idx+1 parce que l'affichage commence à 1 mais les index commencent à 0
        # boucle pour demander le choix du joueur jusqu'à ce qu'il entre un choix valide
       
        while True:
            try: 
                choix = int(input("Choisissez le numéro de la carte à jouer : "))
                choix = choix - 1  # on soustrait 1 parce que l'index Python commence à 0
                
                if choix in cartes_jouables:  # le choix est valide et la carte est bien jouable
                    carte_choisie = main[choix]  # on récupère la carte choisie
                    main.pop(choix) # on l'enlève de la main (pop avec l'index)
                    defausse.append(carte_choisie)  # on la met sur la pile de défausse
                    print("Vous jouez : " + carte_choisie[1] + " " + carte_choisie[0])
                    return carte_choisie  # on retourne la carte jouée, elle devient la carte du dessus
                else:
                    print("Cette carte n'est pas jouable, choisissez une autre.") # le joueur a entré un numéro qui existe mais la carte n'est pas jouable

            except ValueError: # si le joueur tape autre chose qu'un nombre, int() plante
                
               print("Entrez un nombre valide.") #le except ValueError attrape cette erreur et on redemande
               
#PARTIE 5 : lancement et boucle principale du jeu


def demander_nb_joueurs(): # Demande combien de joueurs veulent jouer

    while True:  # boucle infinie, on sortira avec return quand l'entrée sera bonne
        try:
            nb = int(input("Combien de joueurs ? (2 à 10) : "))
            if 2 <= nb <= 10: # On verifie si le nombre de joueur est bien compris entre 2 et 10 
                return nb  # entrée valide, on sort de la fonction
            else:
                print("Il faut choisir entre 2 et 10 joueurs.") # Si le nombre est pas compris entre 2 et 10 
        except ValueError:
            print("Veuillez entrer un nombre entier.")  # si le joueur tape des lettres ou autre chose qui n'est pas un entier


def lancer_jeu(): # C'est la fonction principale qui lance les parties et fait fonctionner les fonction dans le bon ordre
    print("..............................")  # message d'accueil
    print("   Bienvenue dans le UNO !  ")
    print("............................\n")
    
    nb_joueurs = demander_nb_joueurs() # 1. on demande le nombre de joueurs

    # 2. on crée le paquet et on le mélange
    paquet = creer_paquet()      # on crée toutes les cartes
    melanger_paquet(paquet)      # on les mélange avec random.shuffle

    # 3.on crée les joueurs et on leur distribue leurs cartes
    joueurs = creer_joueurs(nb_joueurs, paquet)

    # 4. on tire la première carte pour la défausse, on fait attention que ce ne soit pas une carte spéciale
    premiere_carte = paquet.pop()  # on prend la première carte du paquet mélangé

    while premiere_carte[1] in ["passer", "inverser", "+2"]:  # si c'est une carte spéciale on la remet dans le paquet et on en reprend une autre
        paquet.insert(0, premiere_carte)  # on la remet au fond du paquet
        premiere_carte = paquet.pop()     # on en reprend une nouvelle

    defausse = [premiere_carte] # la défausse est une liste qui commence avec cette carte
    carte_dessus = premiere_carte  # on se souvient de la carte du dessus

    print("\nLa partie commence... ")
    print("Première carte : " + carte_dessus[1] + " " + carte_dessus[0])

    # variables pour gérer l'ordre des tours
    ordre = 1          # 1 = sens normal (joueur 1, 2, 3...), -1 = sens inverse
    noms_joueurs = list(joueurs.keys())  # on transforme les clés du dictionnaire en liste
    index_courant = 0  # on commence par le premier joueur (index 0 dans la liste)
    gagnant = None     # pas encore de gagnant, on met None


    while gagnant is None: #Boucle principale, elle tourne jusqu'a ce qu'il y ait un gagniant

        # on récupère le nom et la main du joueur dont c'est le tour
        nom = noms_joueurs[index_courant]  # nom du joueur actuel
        main = joueurs[nom]                # sa main (liste de cartes) depuis le dico

        input("\n[Entrée pour commencer le tour de " + nom + "]")

        nouvelle_carte = jouer_tour(nom, main, carte_dessus, paquet, defausse)
        carte_dessus = nouvelle_carte  # on met à jour la carte du dessus

        # on vérifie si ce joueur a gagné (plus de cartes dans sa main)
        if verifier_victoire(joueurs[nom]):
            gagnant = nom   # on enregistre son nom comme gagnant
            break # on sort de la boucle, la partie est finie

        if len(joueurs[nom]) == 1:
            print("\n!!! " + nom + " dit UNO ! Il ne lui reste qu'une seule carte.")

        # on vérifie si la valeur de la carte est dans notre liste de cartes spéciales
        if carte_dessus[1] in ["passer", "inverser", "+2"]:
            index_courant, ordre = appliquer_effet(
                carte_dessus, joueurs, ordre, index_courant, paquet, defausse)

        # on passe au joueur suivant en avançant l'index le modulo (%) permet de revenir à 0 quand on dépasse le dernier joueur
        index_courant = (index_courant + ordre) % len(noms_joueurs) # ex: 4 joueurs, on est à l'index 3, (3+1) % 4 = 0 -> on revient au début

    # message de fin quand on sort de la boucle (Break)
    print("\n...........................")
    print("  " + gagnant + " a gagné la partie !")
    print(".............................")

lancer_jeu()