function checkform() {
    var tousLesChamps = document.querySelectorAll('form[name="formulaire"] input');

    var totalNouveauxPlacements = 0;

    for (var i = 0; i < tousLesChamps.length; i++) {
        var champ = tousLesChamps[i];

        // Vérifiez les champs E_* pour qu'ils soient des nombres positifs
        if (champ.name.startsWith("E_")) {
            var valeurPlacement = champ.value.trim(); // Supprimez les espaces avant et après la valeur

            // Utilisez une expression régulière pour vérifier si la chaîne ne contient que des chiffres positifs
            if (!/^[0-9]+(\.[0-9]+)?$/.test(valeurPlacement) || parseFloat(valeurPlacement) < 0) {
                alert('Veuillez entrer une valeur numérique positive.');
                return false;
            }

            totalNouveauxPlacements += parseFloat(valeurPlacement);
        }
    }

    // Obtenez le fond disponible du joueur
    var fondJoueur = parseFloat(document.querySelector('[name="playerFond"]').value);

    // console.log(fondJoueur);

    // Obtenez tous les champs de placements supprimés
    var placementsSupprimes = document.querySelectorAll('form[name="formulaire"] input[type="checkbox"]:checked');

    // Calculez le total des placements supprimés
    var totalPlacementsSupprimes = 0;

    for (var j = 0; j < placementsSupprimes.length; j++) {
        totalPlacementsSupprimes += parseFloat(placementsSupprimes[j].value);
    }

    // Vérifiez si le capital après les changements est positif
    if (fondJoueur - totalNouveauxPlacements + totalPlacementsSupprimes < 0) {
        alert('Pas assez d\'argent pour réaliser tous les placements.');
        return false;
    }

    return true;
}


function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}



document.addEventListener("DOMContentLoaded", function() {


    var entreprisesDataArray = Object.values(cours_boursier_data);
    
    // Parcourez chaque graphique sur la page
    entreprisesDataArray.forEach(function(data, index) {
        // Récupérez les données stockées dans l'attribut data-cours-boursier
        var container = document.getElementById('chart-container-' + JSON.parse(data)[0].fields.entreprise);
        

        // Convertissez la chaîne JSON en tableau d'objets
        var coursBoursierData = JSON.parse(data);

        // Convertissez les données en un format adapté à Chart.js pour chaque entreprise
        var labels = coursBoursierData.map(function(entry) {
            return entry.fields.unite_temps;
        });

        var valeursBourse = coursBoursierData.map(function(entry) {
            return entry.fields.valeur_bourse;
        });


        // Configurez le graphique avec Chart.js pour chaque entreprise
        var canvasId = 'myChart-' + JSON.parse(data)[0].fields.entreprise;

        var ctx = container.querySelector('#' + canvasId).getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Valeur en Bourse',
                    data: valeursBourse,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 2,
                    backgroundColor: 'rgba(255, 165, 0, 0.2)',
                    fill: true
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        type: 'linear',
                        position: 'bottom',
                        grid: {
                            color: 'rgba(50, 50, 50, 1)' // Couleur du quadrillage en noir
                        },
                        ticks: {
                            color: 'rgba(50, 50, 50, 1)' // Couleur des étiquettes sur l'axe x en noir
                        }
                    },
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(50, 50, 50, 1)' // Couleur du quadrillage en noir
                        },
                        ticks: {
                            color: 'rgba(50, 50, 50, 1)' // Couleur des étiquettes sur l'axe y en noir
                        }
                    }
                },
                plugins: {
                    legend: {
                        labels: {
                            color: 'rgba(50, 50, 50, 1)' // Couleur de l'écriture du label de la légende en noir
                        }
                    }
                }
            }
        });
    });
});