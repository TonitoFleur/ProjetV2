// Fonction permettant de charger l'html avant d'exécuter le js
$(document).ready(function() {
  // fonction s'executant a chaque fois qu'une touche est relachée dans le champs mdp
  $('#password').on('keyup', function() {
    var password = $(this).val();
    var lowerCaseLetters = /[a-z]/g;
    var upperCaseLetters = /[A-Z]/g;
    var numbers = /[0-9]/g;

    // Vérifier et mettre a jour les conditions du mdp
    var lowerCasePassed = password.match(lowerCaseLetters) ? true : false;
    var upperCasePassed = password.match(upperCaseLetters) ? true : false;
    var numberPassed = password.match(numbers) ? true : false;

    if (lowerCasePassed) {
      $('#lowercase').css('color', 'green');
    } else {
        $('#lowercase').css('color', 'red');
    }

    if (upperCasePassed) {
      $('#uppercase').css('color', 'green');
    } else {
        $('#uppercase').css('color', 'red');
    }

    if (numberPassed) {
      $('#number').css('color', 'green');
    } else {
        $('#number').css('color', 'red');
    }
  });
});