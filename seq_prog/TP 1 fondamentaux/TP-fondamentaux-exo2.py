print("** TP sur la boucle FOR **")
"""
# tester, modifier et analyser cette boucle avant de vous lancer dans l'exercice
for i in range(10):
	print((i+1)*3)

"""
"""
# _______________________________ Question 1) _____________________________________________________
# demander à l'utilisateur la table qu'il veut afficher
choix_table = int(input("Quel table de multiplication voulez-vous réviser ? "))

# affichage de la table de votre choix
print("===== TABLE DE", choix_table, "=====")
for i in range(1,11):
	print(str(i) + " x " + str(choix_table) + " = " + str(i * choix_table))
print("") # saute une ligne


"""

# _______________________________ Question 2) _____________________________________________________
# affichage de toutes les tables de 1 à 10
print("Voici toutes les tables de multiplications de 1 à 10")
for j in range(1,11):
	print("===== TABLE DE", j, "=====")
	for i in range(1, 11):
		print(str(i) + " x " + str(j) + " = " + str(i * j))
	print("") # permet de sauter une ligne entre chaque table

