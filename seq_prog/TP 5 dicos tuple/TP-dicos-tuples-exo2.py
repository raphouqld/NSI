"""
Notions abordées :
	- fonctions de hachage
	- opérations sur les dictionnaires dictionnaires
	- tuple et retour multiple de fonctions

Exercice à réaliser :
	1) Ecrire une fonction afficher_comptes(pdico) qui affiche tous les couples user/password présents
	dans le dictionnaire. Les mots de passe devront évidemment ne pas avoir été stockés "en clair"
	
	2) Ecrire une fonction creer_compte(pdico) qui ajoute à pdico un élément clé/valeur = user/password
	demandé à l'utilisateur et où password est un mot de passe qui a été haché avant d'être ajouté.
	Coder alors la fonctionnalité numéro 3 du menu.

	3) Ecrire une fonction identifier(pdico) qui permet d'authentifier l'utilisateur et de coder la
	fonctionnalité numéro 4 du menu. On pourra écrire pour cela deux fonctions dont les signatures
	sont les suivantes :
	
	verifier_user(pdico, puser)
    	|- ENTREES : un dictionnaire et une chaîne
    	|- SORTIES : un booléen True ou False indiquant si puser est dans pdico

	verifier_password(pdico, puser, ppassword)
    	|- ENTREES : un dictionnaire et deux chaînes puser et ppassword
    	|- SORTIES : un booléen indiquant si le mot de passe est correct
	
Remarques :
		a) le dictionnaire est pré-rempli de comptes pour les tests. Les mots de passe hachés avec
		l'algorithme md5 sont les suivants : alice -> azerty ; bob -> 12345 ; carol -> motdepasse
		b) Attention, à chaque fois que le programme est relancé, vous perdez tous les comptes saisis
		sauf alice, bob et carol bien sûr
"""

# IMPORT ==========================================================================================


# FONCTIONS =======================================================================================

# PROGRAMME PRINCIPAL =============================================================================
# les mots de passe sont stockés cryptés et non en clair dans le dictionnaire
dicopass = {\
			"alice"	: "ab4f63f9ac65152575886860dde480a1",\
			"bob" 	: "827ccb0eea8a706c4c34a16891f84e7b",\
			"carol" : "b6edd10559b20cb0a3ddaeb15e5267cc"\
			}

while(prog_is_running):
	choix = input("Voulez-vous sortir de cette boucle infinie : ")
	if choix.lower() == "oui":
		prog_is_running = False
	else:
		print("Boucle en cours...")

print("Boucle stoppée !!!")
