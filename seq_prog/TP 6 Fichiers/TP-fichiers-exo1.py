"""
Exercice à réaliser :
	1) Ecrire une fonction lire_dico(pnomfic) qui crée un dictionnaire vide et le remplit du contenu
	du fichier passé en paramètre correctement stocké sous la forme clé/valeur.
	lire_dico(pnomfic)
		|- ENTREES : pnomfic est de type str
		|- SORTIES : un dictionnaire de couple user/password
	Lire ce fichier à chaque démarrage de l'application pour charger le dictionnaire des comptes.

	2) Ecrire une fonction enregister_dico(pnomfic, pdico) qui stocke les couples clé/valeur de pdico
	dans le fichier pnomfic. Faire en sorte d'enregistrer ce dictionnaire lorsque l'utilsateur quitte
	le programme afin d'assurer la persistance des données.
	enregistrer_dico(pnomfic, pdico)
		|- ENTREES : pnomfic est de type str, pdico est de type dictionnaire
		|- SORTIES : rien

REMARQUE IMPORTANTE : l'accès en écriture au fichier comptes.txt est dangereuse car vous pouvez perdre
toutes les données qui y sont stockées. Pensez avant exécution du programme à vérifier que son contenu
se présente correctement et après chaque exéction, vérifier que les données se sont enregistrées tel
que vous le souhaitiez. Gardez donc une copie de ce fichier pour restaurer son contenu si nécessaire
avant ou après chaque exécution.
"""

# IMPORT =========================================================================================
import hashlib

# FONCTIONS =======================================================================================
def afficher_menu():
	print("")
	print("{:*^50}".format(" MENU "))
	print("* {:<46} *".format("1 - Afficher le hash d'une chaîne"))
	print("* {:<46} *".format("2 - Afficher les comptes utilisateurs"))
	print("* {:<46} *".format("3 - Créer un compte"))
	print("* {:<46} *".format("4 - S'identifier"))
	print("* {:<46} *".format("5 - Quitter"))
	_choix =  input("* Votre choix : ")
	print("")
	return _choix

def hacher(pmot):
	return hashlib.md5(pmot.encode()).hexdigest()

def afficher_comptes(pdico):
	print("{:-^50}".format(" Liste des comptes utilisateurs "))
	print("")
	for k, v in pdico.items():
		print("Utilsateur : " + k)
		print("Mot de passe : " + v)
		print("")

def creer_compte(pdico):
	print("{:-^50}".format(" Créer un compte "))
	print("")
	_user, _password = saisir_user_password() # on saisit les informations du compte
	pdico[_user] = _password # et on l'ajoute au dictionnaire
	print("Compte créé avec succès...")

def saisir_user_password():
	_user = input("Entrer un nom utilisateur : ")
	_password = input("Entrer un mot de passe : ")
	return (_user, hacher(_password))

def verifier_user(pdico, puser):
	if puser in pdico:
		return True
	return False

def verifier_password(pdico, puser, ppassword):
	if pdico[puser] == ppassword:
		return True
	else:
		return False

def identifier(pdico):
	print("{:-^50}".format(" Identification "))
	print("")
	_user = input("Nom utilisateur : ")
	if verifier_user(pdico, _user):
		_password = input("Mot de passe : ")
		if verifier_password(pdico, _user, hacher(_password)):
			print("Authentification réussie... Bienvenue " + _user)
		else:
			print("Mot de passe incorrect !!!")
	else:
		print("Vous n'êtes pas un utilisateur enregistré.")

def lire_dico(pnomfic):
	pass

def enregistrer_dico(pnomfic, pdico):
	pass

# PROGRAMME PRINCIPAL =============================================================================
dicopass = lire_dico("comptes.txt") # on lit notre fichier à chaque démarrage

prog_is_running = True # une fois affecté à False, le programme s'arrête
while(prog_is_running):
	choix = afficher_menu()
	if choix == "1":
		mot = input("Saisir un mot :")
		print("Le hash md5 du mot saisi est : " + hacher(mot))
	elif choix == "2":
		afficher_comptes(dicopass)
	elif choix == "3":
		creer_compte(dicopass)
	elif choix == "4":
		identifier(dicopass)
	elif choix == "5":
		enregistrer_dico("comptes.txt", dicopass)
		prog_is_running = False
	else:
		print("Choix non valide")

print("Vous vous êtes déconnecté. A bientôt.")