// Fonction pour initialiser la carte pour les utilisateurs
function initUserMap() {
    // Initialiser la carte centrée sur une position donnée (exemple : Paris)
    var map = L.map('map').setView([48.8566, 2.3522], 13);

    // Ajouter une couche de tuiles OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Stocker les markers pour pouvoir les supprimer lors de la mise à jour
    window.userMarkers = [];

    // Fonction pour mettre à jour les markers
    function updateMarkers() {
        fetch('/api/parking_data')
            .then(response => response.json())
            .then(data => {
                // Supprimer les anciens markers
                window.userMarkers.forEach(marker => map.removeLayer(marker));
                window.userMarkers = [];

                data.forEach(spot => {
                    var marker = L.marker([spot.latitude, spot.longitude]).addTo(map);
                    var status = spot.occupied ? 'Occupé' : 'Disponible';
                    var popupContent = `<b>${spot.name}</b><br>Status: ${status}<br>Type: ${spot.type}`;
                    marker.bindPopup(popupContent);
                    window.userMarkers.push(marker);
                });
            })
            .catch(error => console.error('Erreur:', error));
    }

    // Initialisation des markers
    updateMarkers();

    // Mettre à jour toutes les 10 secondes
    setInterval(updateMarkers, 10000);
}

// Fonction pour initialiser la vue pour les agents municipaux
function initAgentView() {
    function updateTable() {
        fetch('/api/parking_data')
            .then(response => response.json())
            .then(data => {
                var tbody = document.querySelector('#parking-table tbody');
                tbody.innerHTML = ''; // Vider le tableau

                data.forEach(spot => {
                    var row = document.createElement('tr');

                    var cellId = document.createElement('td');
                    cellId.textContent = spot.id;
                    row.appendChild(cellId);

                    var cellName = document.createElement('td');
                    cellName.textContent = spot.name;
                    row.appendChild(cellName);

                    var cellType = document.createElement('td');
                    cellType.textContent = spot.type;
                    row.appendChild(cellType);

                    var cellOccupied = document.createElement('td');
                    cellOccupied.textContent = spot.occupied ? 'Oui' : 'Non';
                    row.appendChild(cellOccupied);

                    var cellUpdate = document.createElement('td');
                    cellUpdate.textContent = spot.last_update || 'N/A';
                    row.appendChild(cellUpdate);

                    tbody.appendChild(row);
                });
            })
            .catch(error => console.error('Erreur:', error));
    }

    // Initialisation du tableau
    updateTable();

    // Mettre à jour toutes les 10 secondes
    setInterval(updateTable, 10000);
}
