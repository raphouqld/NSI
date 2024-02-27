let repertoire = ["Raphaël","0769125614","Erwan","0664934770"]

function ajouterNum(){
    // Récuperer les élements
    var quelNom = prompt("Quel est votre nom ?")
    var quelNumero = prompt("Quel est votre Numéro ?");

    // Ajouter au tableau
    repertoire.push(quelNom,quelNumero); 
}

function rechercherNum(){
    // Récuperer
    var nom = prompt("Entrer un nom");
    var posNom = repertoire.indexOf(nom);
    var posNumero = posNom+1
    if (posNom != -1){
        document.getElementById("outputRechercher").innerHTML = "Le numéro de "+nom+" est "+ repertoire[posNumero];
    }else{
        document.getElementById("outputRechercher").innerHTML = "Le nom que vous avez renseigné n'est pas dans le répertoire."
    }
}

function changerTheme(){
    var lienCSS = document.getElementById('lienCSS'); // Obtient l'élément link qui lie le fichier CSS
    var nomFichierCSS = lienCSS.getAttribute('href'); // Obtient le nom du fichier CSS actuellement lié

    // Détermine quel thème est actuellement appliqué
    if (nomFichierCSS === 'style_light.css') {
        lienCSS.setAttribute('href', 'style_dark.css'); // Change vers le thème sombre
    } else {
        lienCSS.setAttribute('href', 'style_light.css'); // Change vers le thème clair
    }
}