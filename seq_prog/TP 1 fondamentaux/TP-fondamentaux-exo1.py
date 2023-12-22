print("** TP sur les fondamentaux du langage et les tests conditionnels **")
"""
# tester ces quelques lignes avant d'attaquer l'exercice.
JE_SUIS_UNE_CHAINE = "je suis une chaîne de caractères"
JE_SUIS_UN_ENTIER = 1
JE_SUIS_UN_FLOTTANT = 1.0 # car dans mon écriture, il y a un point et pas une virgule !!!
print(type(JE_SUIS_UNE_CHAINE))
print(type(JE_SUIS_UN_ENTIER))
print(type(JE_SUIS_UN_FLOTTANT))
"""


# _______________________________ Question 1) _____________________________________________________
# saisie du nom
nom = input("Quel est votre nom?")

# saisie du prénom et affichage du message de bienvenue
prenom = input("Quel est votre prénom ?")
print("Bonjour,", prenom, nom, "!")




# _______________________________ Question 2) _____________________________________________________
# saisie des moyennes des trois trimestres
moyT1 = float(input("Votre moyenne du 1er trimestre est de : "))
moyT2 = float(input("Votre moyenne du 2ème trimestre est de : "))
moyT3 = float(input("Votre moyenne du 3ème trimestre est de : "))

# calcul de la moyenne générale
moyenne = (moyT1+moyT2+moyT3)/3

#Affichage de la moyenne
#print("Votre moyenne de l'année est :", moyenne)

# _______________________________ Question 3) _____________________________________________________
# affichage de la moyenne générale
print("Votre moyenne générale est de : ", moyenne)
# affichage des informations complémentaires
if moyenne > 18 :
    print("Bravo",prenom,nom,", vous avez les félicitations du jury !")
elif moyenne > 16 :
    print("Bravo",prenom,nom,", vous avez la mention très bien !")
elif moyenne > 14 :
    print("Bravo",prenom,nom,", vous avez la mention bien !")
elif moyenne > 12 :
    print("Bravo",prenom,nom,", vous avez la mention assez bien !")
elif moyenne > 10 :
    print("Bravo",prenom,nom,", vous avez votre bac !")
elif moyenne > 8 :
    print(prenom,nom,", vous pouvez passer au rattrapage.")
else :
    print("Désolé",prenom,nom,"vous n'avez pas le bac. Il faudra mieux travailler l'année prochaine !")
