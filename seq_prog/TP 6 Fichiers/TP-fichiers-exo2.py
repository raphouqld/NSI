"""
Notions étudiées :
	- lecture de fichier CSV
	- chargement du contenu d'un fichier CSV en mémoire
	- formatage de chaînes de caractères
	- manipulation de listes de tuples

Exercice à réaliser :
	1) Après avoir observé la structure et la nature des données contenues dans le fichier data.csv,
	écrire une fonction afficher_fichier(pnomfic) qui extrait, formate et affiche ces données :
	afficher_fichier(pnomfic)
		ENTREES : pnomfic est de type str
		SORTIES : rien
	Aide : On pourra utiliser les abbréviations suivantes pour les intitulés de chaque colonne lors
	de l'affichage : 
			- DEP : numéro de département
			- LIBDEP : libellé du département
			- TN19 : taux de natalité (pour mille) en 2019
			- AGE19 : âge moyen de la mère en 2019
			- NAISS18 : nombre de naissances en 2018

	2) Ecrire une fonction charger_fichier(pnomfic, pliste) qui charge le contenu du fichier nommé
	pnomfic dans la variable pliste et où chaque élément de la liste est un tuple de la forme
	(DEP, LIBDEP, TN19, AGE19, NAISS18).
	charger_fichier(pnomfic, pliste)
    	ENTREES : pnomfic est de type str, pliste est une liste de tuples
    	SORTIES : rien

	3) Ecrire une fonction calculer_total_naissance(pliste) qui calcule er renvoit le nombre total
	de naissances en France en 2018 :
	calculer_total_naissance(pliste)
    	ENTREES : pliste est une liste de tuples
    	SORTIES : un entier représentant le nombre total de naissances en France 2018

	3) Ecrire deux fonctions permettant respectivement de déterminer le département ayant le plus fort
	et le plus faible taux de natalité en 2019 :
	taux_natalite_max(pliste)
		ENTREES : pliste est une liste de tuples
    	SORTIES : le nom du département ayant le taux de natalité le plus fort

    taux_natalite_min(pliste)
		ENTREES : pliste est une liste de tuples
    	SORTIES : le nom du département ayant le taux de natalité le plus faible

Remarque : vous pouvez changer comme bon vous semble le nom des fonctions et des variables mais tâchez
de structurer votre code du mieux possible et de la manière la plus lisible possible.
"""

# FONCTIONS =======================================================================================
def afficher_fichier(pnomfic):
	pass

def charger_fichier(pnomfic, pliste):
	pass

def calculer_total_naissance(pliste):
	pass

def taux_natalite_max(pliste):
	pass

def taux_natalite_min(pliste):
	pass

# PROGRAMME PRINCIPAL =============================================================================
lst_data = [] # liste d'enregistrements stockés sous la forme de tuples
afficher_fichier("data.csv")
charger_fichier("data.csv", lst_data)
