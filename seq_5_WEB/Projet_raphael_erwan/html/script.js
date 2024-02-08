let repertoire = ["Quillaud","0769125614","Detambel","0664934770"]

function ajouterNum(){
    // Récuperer les élements
    var quelNom = prompt("Quel est votre nom ?")
    var quelNumero = prompt("Quel est votre Numéro ?");

    // Ajouter au tableau
    repertoire.push(quelNom,quelNumero); 
}

function rechercherNum(){
    // Récuperer
    var nom = prompt("Entrer un nom de famille");
    var posNom = repertoire.indexOf(nom);
    var posNumero = posNom+1
    if (posNom != -1){
        document.getElementById("outputRechercher").innerHTML = repertoire[posNumero];
    }else{
        document.getElementById("outputRechercher").innerHTML = "Le nom que vous avez renseigné n'est pas dans le répertoire."
    }
}