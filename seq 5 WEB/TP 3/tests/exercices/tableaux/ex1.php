<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Exercice 1</title>
    </head>
    <body>
        <p>
            <?php
            $prenoms = array(
                'François',
                'Michel',
                'Nicole',
                'Véronique',
                'Benoît');
            
            for($nb=0;$nb<=4;$nb++){
                echo $prenoms[$nb], '</br>';
            }
            ?>
        </p>
    </body>
</html>