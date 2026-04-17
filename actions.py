from cartes import melanger_paquet, carte_jouable 
from joueurs import afficher_main, afficher_carte_du_dessus  #Car joueur_pioche appelle melanger_paquet, et jouer_tour appelle afficher_main, afficher_carte_du_dessus et carte_jouable, ces fonctions sont dans d'autres fichiers, donc Python a besoin qu'on lui dise où les chercher

def joueur_pioche(paquet, defausse, main): #cette fonction fait piocher une carte au joueur et elle gère aussi le cas où le paquet est vide 

    if len(paquet) == 0:#si le paquet est vide, on prend la défausse pour reformer un paquet
        print("Le paquet est vide, on remelange la defausse!")  
        derniere = defausse[-1]  #on garde la dernière carte de la défausse(celle du dessus): defausse[-1] est le dernier élement de la liste
        for carte in defausse[:-1]: #on parcourt toutes les cartes sauf la dernière
            paquet.append(carte)  #on remet chaque carte dans le paquet
        defausse.clear() #on vide completement la défausse
        defausse.append(derniere) #on remet juste la dernière carte sur la défausse
        melanger_paquet(paquet) #on mélange le nouveau paquet

    if len(paquet) > 0: #maintenant on vérifie encore une fois si le paquet contient des cartes pour pouvoir piocher
        nouvelle_carte = paquet.pop()  #on pioche la carte du dessus
        main.append(nouvelle_carte)  #on l'ajoutela carte à la main du joueur
        print("Vous avez pioché : " + nouvelle_carte[1] + " " + nouvelle_carte[0])  #on affiche quelle carte a été piochée
        return nouvelle_carte  
    
def appliquer_effet(carte, joueurs, ordre, index_courant, paquet, defausse): #cette fonction applique l'effet d'une carte spéciale comme +2, passer ou inverser
    valeur = carte[1] #on récupère la valeur de la carte

    noms = list(joueurs.keys()) #on transforme les noms des joueurs (qui sont des clés du dictionnaire) en liste pour pouvoir les parcourir
    nb = len(noms) #nombre de joueurs (pour la suite)

    if valeur == "passer":
        print("Carte PASSER! Le joueur suivant passe son tour.") #pour faire passer un tour on avance l'index d'un joueur de plus
        index_courant = (index_courant + ordre) % nb   #le % nb sert à revenir à 0 quand on dépasse le dernier joueur
        return index_courant, ordre #on retourne les deux valeurs modifiée

    if valeur == "inverser":
        print("Carte INVERSER! Le sens du jeu change.")
        ordre= ordre *-1  #en multipliant par -1 on change le sens
        return index_courant, ordre

    if valeur == "+2": #le joueur suivant doit piocher 2 cartes et passer son tour
        index_suivant = (index_courant + ordre) % nb #d'abord on calcule quel est le joueur suivant
        nom_suivant = noms[index_suivant]  #on récupère son nom dans la liste
        print("Carte +2! " + nom_suivant + " doit piocher 2 cartes.")  #on fait piocher 2 cartes au joueur suivant

        #on appelle joueur_pioche deux fois pour qu'il pioche 2 cartes
        joueur_pioche(paquet, defausse, joueurs[nom_suivant])
        joueur_pioche(paquet, defausse, joueurs[nom_suivant])

        #le joueur suivant passe aussi son tour
        index_courant = (index_courant + ordre) % nb
        return index_courant, ordre
    return index_courant, ordre #si c'est aucune carte spéciale connue,on change rien



#Partie 4: le déroulement d'un tour 

def jouer_tour(nom, main, carte_dessus, paquet, defausse): #c'est la fonction principale pour gérer le tour d'un joueur (alaffichage, le choix de la carte et si on dois piocher ou pas
    afficher_carte_du_dessus(carte_dessus)  #on montre la carte du dessus pour commencer
    afficher_main(nom, main)   #on affiche les cartes du joueur pour qu'ils choisissent
    #on cherche quelles cartes du joueur sont jouables
    #on stocke leurs index dans une liste (pas les cartes elles-mêmes), comme ça on peut retrouver la carte avec main[index] facilement
    cartes_jouables = []  #liste vide au depart
    for i in range(len(main)): #on parcourt toutes les cartes de la main
        if carte_jouable(main[i], carte_dessus): #si la carte est jouable on ajoute son index à la liste
            cartes_jouables.append(i)             

    print("C'est à vous de jouer, " + nom + " !")

    if len(cartes_jouables) == 0: #cas où le joueur n'a aucune carte jouable : il doit piocher obligatoirement
        print("Aucune carte jouable. Vous devez piocher.")
        input("Appuyez sur Entrée pour piocher")
        nouvelle = joueur_pioche(paquet, defausse, main) #on fait piocher une carte

        #si la carte piochée est jouable, le joueur peut choisir de la jouer
        if nouvelle is not None and carte_jouable(nouvelle, carte_dessus):
            print("La carte piochée est jouable !")
            choix = input("Voulez-vous la jouer ? (oui/non) : ")
            if choix== "oui":  #si le joueur dit oui
                main.remove(nouvelle) #on enlève la carte de la main
                defausse.append(nouvelle)  #on la met sur la défausse
                return nouvelle #on retourne la nouvelle carte du dessus
        return carte_dessus

    else:
        print("Cartes jouables :")
        for idx in cartes_jouables: #on affiche chaque carte jouable avec son numéro dans la main
           
            #idx+1 parce que l'affichage commence à 1 mais les index commencent à 0
            print(str(idx + 1) + ". " + main[idx][1] + " " + main[idx][0])  #idx+1 parce que l'affichage commence à 1 mais les index commencent à 0
       
        while True:#boucle pour demander le choix du joueur jusqu'à ce qu'il entre un choix valide
            try: 
                choix = int(input("Choisissez le numéro de la carte à jouer : "))
                choix = choix - 1  #on soustrait 1 parce que l'index python commence à 0
                
                if choix in cartes_jouables: #si le choix de la carte est bien jouable
                    carte_choisie = main[choix] #alors on récupère la carte choisie
                    main.pop(choix) #on l'enlève de la main 
                    defausse.append(carte_choisie) #on la met sur la pile de défausse
                    print("Vous jouez : " + carte_choisie[1] + " " + carte_choisie[0])
                    return carte_choisie  #on retourne la carte jouée et elle devient la carte du dessus
                else:
                    print("Cette carte n'est pas jouable, choisir une autre.") #on affiche ca si le joueur a entré un numéro qui existe mais la carte n'est pas jouable

            except ValueError: #on a mis ca car si le joueur tape autre chose qu'un nombre cela fait une erreur
                
               print("Entrez un nombre valide.") #le except ValueError detecte cette erreur et on redemande
               
#Partie 5 :lancement et boucle principale du jeu

def demander_nb_joueurs(): #demande combien de joueurs veulent jouer

    while True: #boucle infinie, on sort de cette boucle avec return quand le joueur entre met une bonne entrée
        try:
            nb = int(input("Combien de joueurs ? (2 à 10) : "))
            if 2 <= nb <= 10: #on verifie si le nombre de joueur est bien compris entre 2 et 10 
                return nb  #entrée valide alors on sort de la fonction
            else:
                print("Il faut choisir entre 2 et 10 joueurs.") #si le nombre est pas compris entre 2 et 10 
        except ValueError:
            print("Veuillez entrer un nombre entier.") #si le joueur tape des lettres ou autre chose qui n'est pas un entier

