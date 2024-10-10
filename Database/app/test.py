import sqlite3

# Chemin vers la base de données
db_path = 'utilisateurs.db'

def display_users():
    # Connexion à la base de données
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Récupérer les utilisateurs
    cursor.execute("SELECT * FROM utilisateur")
    users = cursor.fetchall()

    # Afficher les informations des utilisateurs
    if users:
        print("Liste des utilisateurs :")
        for user in users:
            print(f"ID: {user[0]}, Nom: {user[1]}, Prénom: {user[2]}, Email: {user[3]}, Immatriculation: {user[4]}")
    else:
        print("Aucun utilisateur trouvé.")

    # Fermer la connexion
    conn.close()

if __name__ == '__main__':
    display_users()
