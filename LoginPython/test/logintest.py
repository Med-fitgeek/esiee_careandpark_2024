import unittest
from app import app

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_page_loads(self):
        """Test if the login page renders successfully"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Connexion', response.data)

    def test_valid_login(self):
        """Test if login is successful with correct credentials"""
        response = self.app.post('/login', data={
            'username': 'admin',
            'password': 'password123'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Connexion r\xc3\xa9ussie. Bienvenue!', response.data)

    def test_invalid_login(self):
        """Test login failure with incorrect credentials"""
        response = self.app.post('/login', data={
            'username': 'wrong_user',
            'password': 'wrong_password'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

        # Check for the correct error message in the HTML response
        self.assertTrue("Erreur : Nom d&#39;utilisateur ou mot de passe incorrect." in response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
