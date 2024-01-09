"""
Notions abordées :
	- fonctions de hachage
	- tuple et retour multiple de fonctions

Exercice à réaliser :
	1) Ecrire une fonction afficher_menu() qui produit l'affichage suivant et qui renvoit le choix
	de l'utilisateur :
	********************** MENU **********************
	* 1 - Afficher le hash d'une chaîne              *
	* 2 - Afficher les comptes utilisateurs          *
	* 3 - Créer un compte                            *
	* 4 - S'identifier                               *
	* 5 - Quitter                                    *
	* Votre choix : 

	2) Ecrire une fonction hacher(pmot) qui renvoit le hash md5 du mot passé en paramètre et coder
	ainsi la fonctionnalité numéro 1 du menu.

	3) Ecrire une fonction saisir_user_password() qui demande à l'utilisateur de saisir son nom utilisateur
	ainsi que son mot de passe et dont la signature est la suivante :
	saisir_user_password()
		|- ENTREES : rien
		|- SORTIES : un tuple de la forme (nom_utilisateur, mot_de_passe_haché)
	Pensez à la tester, elle sera nécessaire dans l'exercice suivant.

Remarques :
		a) Il existe plusieurs algorithmes de hachage (md5, sha256, ...) qui génèrent chacun des
		hash plus ou moins robuste. Testez si nécessaire avec hashlib.sha256()
		-> voir doc : https://docs.python.org/fr/3.8/library/hashlib.html?highlight=hashlib#module-hashlib

		b) Pensez à tester vos fonctions via un print par exemple afin de vérifier qu'elles
		fonctionnent correctement.

		c) Vous devez mettre en place un menu qui s'affiche TANT QUE le choix utilisateur n'est pas
		un choix valide.

		d) Afin de rendre un code plus lisible, on a déjà vu dans un précédent TP que les paramètres
		de fonction peuvent être préfixés de la lettre p. De même, les variables locales à une fonction,
		c'est-à-dire les variables manipulées uniquement par la fonction elle-même peuvent être préfixées d'un
		underscore, par ex., _user. Tout ceci n'est bien sûr pas une obligation.
"""

# IMPORT ==========================================================================================


# FONCTIONS =======================================================================================


# PROGRAMME PRINCIPAL =============================================================================
prog_is_running = True # une fois affecté à False, le programme s'arrête

while(prog_is_running):
	choix = input("Voulez-vous sortir de cette boucle infinie : ")
	if choix.lower() == "oui":
		prog_is_running = False
	else:
		print("Boucle en cours...")

print("Boucle stoppée !!!")
