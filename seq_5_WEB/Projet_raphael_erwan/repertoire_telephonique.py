repertoire = ["raphael","07 69 12 56 14","erwan","07 46 58 39 29"]

def afficherMenu() :
    print("\n\n***** MENU *****")
    print("\nChoisissez une option")
    print("1. Ajouter un numéro")
    print("2. Rechercher un numéro")
    print("3. Quitter")

def ajouterNumero() :
    nom = input("Nom du contact : ")
    numero = input("Numéro de téléphone : ")
    repertoire.append(nom)
    repertoire.append(numero)

def rechercherNumero() :
    nom = input("Nom : ")
    if nom in repertoire :
        posnom = repertoire.index(nom)
        print("\nLe numéro de téléphone de ",nom," est : ",repertoire[posnom + 1])
    else :
        print("\nCe nom n'est pas dans le répertoire.")

while True :
    afficherMenu()
    choix = input("Choix : ")
    if choix == "1" :
        ajouterNumero()
    elif choix == "2" :
        rechercherNumero()
    elif choix == "3" :
        print( "\nAu revoir !\n")
        break
    else :
        print("\nMerci d'entrer un nombre valide (1/2/3)")