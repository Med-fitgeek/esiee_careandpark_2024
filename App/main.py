from flask import Flask, render_template, jsonify
import random
import datetime

app = Flask(__name__)

# Générer des données fictives pour de nombreuses places de parking
def generate_parking_spots(num_spots):
    base_lat = 48.8566  # Latitude de Paris
    base_lon = 2.3522   # Longitude de Paris
    parking_spots = []
    for i in range(1, num_spots + 1):
        # Générer des positions légèrement différentes pour simuler différents emplacements
        latitude = base_lat + random.uniform(-0.02, 0.02)
        longitude = base_lon + random.uniform(-0.02, 0.02)
        occupied = random.choice([True, False])
        vehicle_type = random.choice(["Véhicule électrique", "Véhicule non électrique", "Scooter électrique", "Trotinette électrique"])
        parking_spots.append({
            "id": i,
            "name": f"Parking {chr(64 + (i % 26) or 26)}{i // 26 if i > 26 else ''}",
            "latitude": latitude,
            "longitude": longitude, 
            "occupied": occupied, 
            "type": vehicle_type,
            "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return parking_spots

# Initialiser avec 50 places de parking
parking_spots = generate_parking_spots(50)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agent')
def agent():
    return render_template('agent.html')

@app.route('/api/parking_data')
def get_parking_data():
    # Simuler des changements aléatoires dans l'occupation des places de parking
    for spot in parking_spots:
        spot['occupied'] = random.choice([True, False])
        # Mettre à jour l'heure de dernière mise à jour
        spot['last_update'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(parking_spots)

if __name__ == '__main__':
    app.run(debug=True)
