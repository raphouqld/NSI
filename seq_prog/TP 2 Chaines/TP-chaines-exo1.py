# DEFINITIONS DES FONCTIONS -----------------------------------------------------------------------
#_____________________________________ Question 2) ________________________________________________
def compter_lettres(mot):
	cpt = .....
	# l'idée est d'utiliser un raccourci syntaxique de Python, ce qui évite une erreur d'indexation
	# en dehors des limites de la chaîne -> IndexError: string index out of range
	for lettre in mot:
		cpt = cpt + 1
	return ........

#_____________________________________ Question 3) ________________________________________________
def compter(mot, flag):
	cpt_cons = 0
	cpt_voy = 0

	for lettre in mot: # rien ne vous empêche d'utiliser for i in range(0, len(mot)):
		if (lettre == 'a' or lettre == '...' or lettre == '..' or lettre == '...' or lettre == '....' or lettre == '....'):
			cpt_voy = cpt_voy + ...
		else:
			cpt_cons = cpt_cons + ...

	if flag == "voyelles":
		return .......
	elif flag == "consonnes":
		return .........
	else:
		return -1 # en général, un retour de -1 signifie que les choses ne se sont pas passées comme prévues

#_____________________________________ Question 4) ________________________________________________
def index(mot, lettre):
	index = -1
	i = 0
	while i < ......... and mot[i] != .......: # tant qu'on a pas atteint la fin du mot et qu'on a pas trouvé la lettre
		i = i + 1 # on passe à la lettre suivante
	if i != len(mot): # on n'a pas atteint la fin du mot donc la lettre a été trouvé
		index = i # on affecte alors son rang à index

	return index

# PROGRAMME PRINCIPAL -----------------------------------------------------------------------------
#_____________________________________ Question 1) ________________________________________________
prenom = .............

#_____________________________________ Question 2) ________________________________________________
print("Votre prénom est composé de " + str(compter_lettres(.............)) + " lettres.")

#_____________________________________ Question 3) ________________________________________________
print("Votre prénom est composé de " + str(compter(prenom, "consonnes")) + " consonnes et de " + str(compter(prenom, "voyelles")) + " voyelles.")

#_____________________________________ Question 4) ________________________________________________
lettre_a_chercher = .......................
index = index(prenom, lettre_a_chercher)
if index != -1:
	print("La lettre " + lettre_a_chercher + " se trouve à l'index " + str(index) + " dans votre prénom")
else:
	print("La lettre " + lettre_a_chercher + " n'existe pas dans votre prénom")
