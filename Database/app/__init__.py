from flask import Flask
import sqlite3

def create_app():
    app = Flask(__name__)
    
    db_path = 'utilisateurs.db'

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateur (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            immatriculation TEXT NOT NULL
        )
        ''')

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
