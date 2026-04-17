from cartes import creer_paquet, melanger_paquet
from joueurs import creer_joueurs, verifier_victoire
from actions import demander_nb_joueurs, jouer_tour, joueur_pioche, appliquer_effet
#comme on a séparé le code en plusieurs fichiers, on doit importer les fonctions qu'ont on a besoin depuis chaque fichier, sinon Python les connait pas

def lancer_jeu(): #c'est la fonction principale qui lance les parties et fait fonctionner les fonction dans le bon ordre
     
    print("Bienvenue dans le UNO !")
    nb_joueurs = demander_nb_joueurs() #1.on demande le nombre de joueurs

    #2.on crée le paquet et on le mélange
    paquet = creer_paquet() #on crée toutes les cartes
    melanger_paquet(paquet) #on les mélange avec random.shuffle

    #3.on crée les joueurs et on leur distribue leurs cartes
    joueurs = creer_joueurs(nb_joueurs, paquet)

    #4.on tire la première carte pour la défausse, on fait attention que ce ne soit pas une carte spéciale
    premiere_carte = paquet.pop()  #on prend la première carte du paquet mélangé

    while premiere_carte[1] in ["passer", "inverser", "+2"]:  #si c'est une carte spéciale on la remet dans le paquet et on en reprend une autre
        paquet.insert(0, premiere_carte) #on la remet au fond du paquet
        premiere_carte = paquet.pop()  #on en reprend une nouvelle

    defausse = [premiere_carte] #la défausse est une liste qui commence avec cette carte
    carte_dessus = premiere_carte #carte du dessus

    print("La partie commence... ")
    print("Première carte : " + carte_dessus[1] + " " + carte_dessus[0])
    # variables pour gérer l'ordre des tours
    ordre = 1    #1= sens normal(joueur 1, 2, 3...), et -1 =sens inverse
    noms_joueurs = list(joueurs.keys()) #on transforme les clés du dictionnaire en liste
    index_courant = 0 #on commence par le premier joueur (index 0 dans la liste)
    gagnant = None  #pas encore de gagnant, on met none


    while gagnant is None: #Boucle principale, elle tourne jusqu'a ce qu'il y ait un gagniant

        #on récupère le nom et la main du joueur dont c'est le tour
        nom = noms_joueurs[index_courant]  # nom du joueur actuel
        main = joueurs[nom]  #sa main (liste de cartes) depuis le dico

        input("[Entrée pour commencer le tour de " + nom + "]")
        nouvelle_carte = jouer_tour(nom, main, carte_dessus, paquet, defausse)
        carte_dessus = nouvelle_carte  #on met à jour la carte du dessus

        #on vérifie si ce joueur a gagné (plus de cartes dans sa main)
        if verifier_victoire(joueurs[nom]):
            gagnant = nom   #on enregistre son nom comme gagnant
            break #on sort de la boucle, la partie est finie

        if len(joueurs[nom]) == 1:
            print("!!! " + nom + " dit UNO ! Il ne lui reste qu'une seule carte.")

        #on vérifie si la valeur de la carte est dans notre liste de cartes spéciales
        if carte_dessus[1] in ["passer", "inverser", "+2"]:
            index_courant, ordre = appliquer_effet(carte_dessus, joueurs, ordre, index_courant, paquet, defausse)

        #on passe au joueur suivant en avançant l'index, le % permet de revenir à 0 quand on dépasse le dernier joueur
        index_courant = (index_courant + ordre) % len(noms_joueurs) #par exemple:4 joueurs, on est à l'index 3, (3+1) % 4= 0 alors on revient au début

     
    print(gagnant + " a gagné la partie !") #message de fin quand on sort de la boucle
    
lancer_jeu()