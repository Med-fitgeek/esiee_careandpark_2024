from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "votre_cle_secrete"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password123':
        # Pass success message to template
        return render_template('login.html', message="Connexion réussie. Bienvenue!")
    else:
        # Pass error message to template
        return render_template('login.html', error="Erreur : Nom d'utilisateur ou mot de passe incorrect.")

if __name__ == '__main__':
    app.run(debug=True)
