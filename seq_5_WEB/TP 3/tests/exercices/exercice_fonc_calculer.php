<!DOCTYPE html>
<html>
    <head>
        <title>Exercice fonction calculer</title>
        <meta charset="utf-8"/>
    </head>
    <body>
        <p>
            <?php
            function calculer($nb_1,$oper,$nb_2){
                //addition
                if($oper == "+"){                
                    $resultat = $nb_1 + $nb_2;
                }

                //soustraction
                elseif($oper == "-"){
                    $resultat = $nb_1 - $nb_2;
                }

                //multiplication
                elseif($oper == "x" OR $oper == "*"){
                    $resultat = $nb_1 * $nb_2;
                }
                
                //division
                elseif($oper == "/"){
                    $resultat = $nb_1 / $nb_2;
                }

                return $resultat;
            }
            $jour = date('d');
            $mois = date('m');
            $annee = date('Y');
            $heure = date('H');
            $minute = date('i');

            echo 'Bonjour ! Nous sommes le '.$jour.'/'.$mois.'/'.$annee.' et il est '.$heure.' h '.$minute, '</br>';
            echo "Le résultat :", '</br>';
            echo calculer(3,"x",4);
            ?>
        </p>
    </body>
</html>