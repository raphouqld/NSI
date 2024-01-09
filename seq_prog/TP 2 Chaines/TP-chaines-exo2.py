# DEFINITIONS DES FONCTIONS -----------------------------------------------------------------------
#_____________________________________ Question 3) ________________________________________________
def remplacer(mot, ........, .........):
	ch = ""
	for lettre in mot:
		if lettre == l1: # si c'est la lettre à remplacer, on concatène l2
			ch = ch + l2
		else:
			ch = ch + lettre # sinon on concatène la lettre elle-même (on la copie)
	return ch


#_____________________________________ Question 3) ________________________________________________
def inverser(...........):
	ch = ""
	for i in range(len(mot) - 1, -1, -1): # parcours inversé : attention à l'index
		ch = ch + mot[i] # ici index appartient [len(mot) - 1; -1[ donc départ sur la dernière lettre du mot et fin sur l'index 0
	return ..............

#_____________________________________ Question 4) ________________________________________________
def est_palindrome(..........):
	if mot == inverser(mot):
		return True
	else:
		return False

# PROGRAMME PRINCIPAL -----------------------------------------------------------------------------
#_____________________________________ Question 1) ________________________________________________
mot = ..........



#_____________________________________ Question 2) ________________________________________________
print("Mot modifié : " + remplacer(...., '.....', '.......'))

#_____________________________________ Question 3) ________________________________________________
print("Mot avec effet miroir : " + ....................)

#_____________________________________ Question 4) ________________________________________________
if est_palindrome(mot):
	print(.............. + " est un palindrome")
else:
	print(.............. + " n'est pas un palindrome")