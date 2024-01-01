
# DEFINITIONS DES FONCTIONS -----------------------------------------------------------------------
#_____________________________________ Question 1) ________________________________________________
def afficherMenu():
    print("********** Bienvenue **********")
    print("Que voulez-vous faire ?")
    print("1 - Afficher une table de multiplication de votre choix")
    print("2 - Afficher toutes les tables de multiplication de 1 à 10")
    print("3 - Quitter l'application")
    return input("Votre choix :")

#_____________________________________ Question 3) ________________________________________________
def afficherTableDe(num_table):
	print("===== TABLE DE", num_table, "=====")
	for i in range(1,11):
		print(str(i) + " x " + str(num_table) + " = " + str(i * num_table))
	print("") # saute une ligne



def afficherTables():
    for j in range(1,11):
        print("===== TABLE DE", j, "=====")
        for i in range(1, 11):
            print(str(i) + " x " + str(j) + " = " + str(i * j))
    print("")


# PROGRAMME PRINCIPAL -----------------------------------------------------------------------------
#_____________________________________ Question 1) ________________________________________________
choix = afficherMenu()

#_____________________________________ Question 2) et 3)________________________________________________
while(choix != "3"):
	if choix == "1":
		choix_table = int(input("Quelle table voulez-vous afficher ? "))
		afficherTableDe(choix_table)
	elif choix == "2":
		afficherTables()
	choix = afficherMenu()

# Si on sort de la boucle, c'est que l'utilisateur a saisi le choix 3 et a donc décidé de quitter l'application
print("") # saut de ligne
print("Vous avez décide de quitter l'application. A bientôt...")