<!DOCTYPE html>
<html>
    <head>
        <title>Test 2</title>
        <meta charset="utf-8"/>
    </head>
    <body>
        <p>
            <?php
            $nombre_lignes=1;

            while($nombre_lignes <= 100){
                echo 'Ceci est la ligne n°'.$nombre_lignes.'<br/>';
                $nombre_lignes++;
            }
            ?>
        </p>
    </body>
</html>