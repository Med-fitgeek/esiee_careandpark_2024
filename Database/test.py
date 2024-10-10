import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('utilisateurs.db')
cursor = conn.cursor()

# Vérifier les tables
cursor.execute("SELECT * FROM utilisateur;")
tables = cursor.fetchall()
print(tables) 

conn.close()
