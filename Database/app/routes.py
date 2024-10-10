from flask import Blueprint, render_template, request
import sqlite3

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Chemin vers la base de données
    db_path = 'utilisateurs.db'

    # Connexion à la base de données
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM utilisateur")
        utilisateurs = cursor.fetchall()

    return render_template('index.html', utilisateurs=utilisateurs)

@main.route('/add', methods=['POST'])
def add_utilisateur():
    nom = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    immatriculation = request.form['immatriculation']

    # Chemin vers la base de données
    db_path = 'utilisateurs.db'

    # Connexion à la base de données
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO utilisateur (nom, prenom, email, immatriculation) VALUES (?, ?, ?, ?)", 
                       (nom, prenom, email, immatriculation))
    
    return index()
