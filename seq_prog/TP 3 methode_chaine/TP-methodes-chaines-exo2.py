# FONCTIONS =======================================================================================
def formater(pclassement):
	lignes = pclassement.splitlines()
	print("{:-^.......}".format(""))
	entete = True
	for ligne in lignes:
		items = ligne.split(";")
		if not(entete):
			ratio = int(items[...])/int(items[...])
			str_ratio = "{:....}".format(.....)
		else:
			str_ratio = "Ratio"
		print("| {:>2} | {:<12} | {:>3} | {:>3} | {:>3} | {:>3} | {:>3} | {:>....} | {:>.....} | {:>...} | {:>...} |".format(items[0], items[1], items[2],\
																										items[3], items[4], items[5],\
																										items[6], items[7], items[8],\
																										items[9], str_ratio))
		if entete:
			print("{:-^78}".format(""))
			entete = False

	print("{:-^78}".format(""))

# PROGRAMME PRINCIPAL =============================================================================
classement = 	";Equipe;Pts;J;G;N;P;Bp;Bc;Diff\n"\
				"1;Paris SG;68;27;22;2;3;75;24;+51\n"\
				"2;Marseille;56;28;16;8;4;41;29;+12\n"\
				"3;Rennes;50;28;15;5;8;38;24;+14\n"\
				"4;Lille;49;28;15;4;9;35;27;+8\n"\
				"5;Reims;41;28;10;11;7;26;21;+5\n"\
				"6;Nice;41;28;11;8;9;41;38;+3\n"\
				"7;Lyon;40;28;11;7;10;42;27;+15\n"\
				"8;Montpellier;40;28;11;7;10;35;34;+1\n"\
				"9;Monaco;40;28;11;7;10;44;44;0\n"\
				"10;Angers;39;28;11;6;11;28;33;-5\n"

formater(classement)
