let repertoire = ["raphael","0769125614","erwan","0664934770"]

function ajouterNum(){
    // Récuperer les élements
    var quelNom = prompt("Quel est votre nom ?")
    quelNom.toLowerCase(); // Mettre en minuscule
    var quelNumero = prompt("Quel est votre Numéro ?");

    // Ajouter au repertoire
    repertoire.push(quelNom,quelNumero); 
}

function rechercherNum(){
    // Récuperer
    var nom = prompt("Entrer un nom");
    nom.toLowerCase(); // Mettre en minuscule
    var posNom = repertoire.indexOf(nom);
    var posNumero = posNom+1

    // Chercher le numero dans le repertoire
    if (posNom != -1){
        document.getElementById("outputRechercher").innerHTML = "Le numéro de "+nom+" est "+ repertoire[posNumero];
    }else{
        document.getElementById("outputRechercher").innerHTML = "Le nom que vous avez renseigné n'est pas dans le répertoire."
    }
}

function changerTheme(){
    var lienCSS = document.getElementById('lienCSS');
    var nomFichierCSS = lienCSS.getAttribute('href');

    if (nomFichierCSS === 'style_light.css') {
        lienCSS.setAttribute('href', 'style_dark.css'); // Change vers le thème sombre
    }
    else if (nomFichierCSS === 'style_dark.css') {
        lienCSS.setAttribute('href', 'style_matrix.css'); // Change vers le thème matrix
    }
    else if (nomFichierCSS === 'style_matrix.css') {
        lienCSS.setAttribute('href','style_space.css'); // Change vers le thème espace
    }
    else if (nomFichierCSS === 'style_space.css') {
        lienCSS.setAttribute('href','style_light.css'); // Change vers le thème clair
    }
}