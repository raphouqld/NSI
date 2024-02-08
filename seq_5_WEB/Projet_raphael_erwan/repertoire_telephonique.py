def afficherMenu() :
    print("\nChoisissez une option")
    print("1. Ajouter un numéro")
    print("2. Rechercher un numéro")
    print("3. Quitter")

def ajouterNumero() :
    print("coucou")

def rechercherNumero() :
    print("coucou")

while True :
    afficherMenu()
    choix = input("Choix : ")
    if choix == 1 :
        ajouterNumero()
    elif choix == 2 :
        rechercherNumero()
    elif choix == 3 :
        break
    else :
        print("Merci d'entrer un nombre valide (1/2/3)")