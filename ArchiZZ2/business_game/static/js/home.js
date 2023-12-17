function checkform() {
    var tousLesChamps = document.querySelectorAll('form[name="formulaire"] input');

    var totalNouveauxPlacements = 0;

    for (var i = 0; i < tousLesChamps.length; i++) {
        var champ = tousLesChamps[i];

        // Vérifiez les champs E_* pour qu'ils soient des nombres positifs
        if (champ.name.startsWith("E_")) {
            var valeurPlacement = parseFloat(champ.value);

            if (isNaN(valeurPlacement) || valeurPlacement < 0) {
                alert('Tous les champs de nouveaux placements doivent être des nombres positifs.');
                return false;
            }

            totalNouveauxPlacements += valeurPlacement;
        }
    }

    // Obtenez le capital du joueur
    var capitalJoueur = parseFloat(document.querySelector('[name="playerCapital"]').value);

    // Obtenez tous les champs de placements supprimés
    var placementsSupprimes = document.querySelectorAll('form[name="formulaire"] input[type="checkbox"]:checked');

    // Calculez le total des placements supprimés
    var totalPlacementsSupprimes = 0;

    for (var j = 0; j < placementsSupprimes.length; j++) {
        totalPlacementsSupprimes += parseFloat(placementsSupprimes[j].value);
    }

    // Vérifiez si le capital après les changements est positif
    if (capitalJoueur - totalNouveauxPlacements + totalPlacementsSupprimes < 0) {
        alert('Pas assez d\'argent pour réaliser tous les placements.');
        return false;
    }

    return true;
}
