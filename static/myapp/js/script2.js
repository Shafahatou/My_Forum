// script2.js

// Fonction pour changer la couleur de fond au survol d'un élément
document.addEventListener('DOMContentLoaded', function() {
    let elements = document.getElementsByClassName('hover-change-color');
    for (let element of elements) {
        element.addEventListener('mouseover', function() {
            this.style.backgroundColor = 'lightblue';
        });
        element.addEventListener('mouseout', function() {
            this.style.backgroundColor = '';
        });
    }
});

// Exemple de fonction JavaScript
function logMessage(message) {
    console.log(message);
}
