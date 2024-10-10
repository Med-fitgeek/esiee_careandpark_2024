from app import create_app

# Créer une instance de l'application
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
