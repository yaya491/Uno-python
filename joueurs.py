from cartes import distribuer_cartes  # creer_joueurs en a besoin pour distribuer les cartes aux joueurs

#Partie:création et gestion des joueurs

def creer_joueurs(nb_joueurs, paquet): #Cette fonction crée tous les joueurs et leur distribue leurs cartes. On a utilisé un dictionnaire pour les joueurs comme ca on peut accéder à la main d'un joueur avec son nom directement
 # dictionnaire: clé = nom du joueur et valeur = main du joueur
    joueurs = {}  #dictionnaire vide qui va se remplir dans la boucle

    for i in range(nb_joueurs): #on fait ça autant de fois qu'il y a de joueurs
        nom = "Joueur " + str(i + 1) #on donne un nom automatique au joueur: "Joueur 1", "Joueur 2"...
        #str(i + 1) parce que i commence à 0 mais les joueurs commencent à 1

        #on appelle distribuer_cartes pour donner 7 cartes à ce joueur et on stocke la liste de cartes dans le dictionnaire avec le nom comme clé
        joueurs[nom] = distribuer_cartes(paquet)
    return joueurs #on retourne le dictionnaire avec tous les joueurs et leurs mains


def afficher_main(nom, main): #Cette fonction affiche les cartes d'un joueur dans la console. On a fait une fonction à part pour ça parce qu'on en a besoin à plusieurs endroits
    print("Main de " + nom + " ---") #titre avec le nom du joueur
    for i in range(len(main)): #on parcourt toute les cartes du joueur
        carte = main[i]        #on récupère la carte à la position i
        #carte[1]c'est la valeur 
        #carte[0]c'est la couleur 
        #on affiche "numéro. valeur et couleur" pour toute les cartes du jeu du joueur
        print(str(i + 1) + ". " + carte[1] + " " + carte[0])



def afficher_carte_du_dessus(carte):#affiche la carte qui est sur le dessus de la pile de défausse, c'est important car le joueur doit voir cette carte avant de choisir quoi jouer
    print("[Carte du dessus : " + carte[1] + " " + carte[0] + "]")

def verifier_victoire(main):#vérifie si un joueur a gagné (s'il n'a plus de cartes)
    return len(main) == 0 #len(main) donne le nombre de cartes dans la main, si la main est vide, alors il a gagné