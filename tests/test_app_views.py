"""Testing application view endpoints"""

import unittest
from flask import session

from recipe_app import app

class FlaskTestCase(unittest.TestCase):
    """Testing whether Flask app was setup correctly"""

    def setUp(self):
        self.tester = app.test_client(self)
    
    # index page loads correctly
    def test_index_loads(self):
        response = self.tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'YUMMY RECIPE APP' in response.data)

    # signup loads correctly
    def test_signup(self):
        response = self.tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'CREATE ACCOUNT', response.data)
    
    # signup works correctly
    def test_signup_user(self):
        response = self.tester.post(
            '/signup', 
            data = dict(email='pwalukagga@gmail.com', 
                         password='pato123', 
                         firstname='Patrick',
                         lastname='Walukagga'),
            follow_redirects=True
            )
        self.assertIn(b'You have successfully created your account, \
               please login into your account', response.data)

    # signin works correcty
    def test_signin_user(self):
        response_up = self.tester.post(
            '/signup', 
            data = dict(email='pwalukagga@gmail.com', 
                         password='pato123', 
                         firstname='Patrick',
                         lastname='Walukagga')
            )
        response_in = self.tester.post(
            '/index', data = dict(email='pwalukagga@gmail.com', 
                         password='pato123'),
            follow_redirects=True
        )
        self.assertIn(b'MY PROFILE', response_in.data)
    
    # dashboard loads correctly when user is logged in
    def test_dashboard(self):
        response_up = self.tester.post(
            '/signup', 
            data = dict(email='pwalukagga@gmail.com', 
                         password='pato123', 
                         firstname='Patrick',
                         lastname='Walukagga')
            )
        response_in = self.tester.post(
            '/index', data = dict(email='pwalukagga@gmail.com', 
                         password='pato123')
        )
        response = self.tester.get('/dashboard', 
                                    content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # dashboard doesnot load if user is not logged in
    def test_dashboard_not_logged_in(self):
        response = self.tester.get('/dashboard', 
                                    content_type='html/text',
                                    follow_redirects=True)
        self.assertIn(b'You need to login to have access to your dashboard, \
            if not, login or checkout the link below', response.data)

    # user creates recipe category
    def test_add_recipe_category(self):
        response_up = self.tester.post(
            '/signup', 
            data = dict(email='pwalukagga@gmail.com', 
                         password='pato123', 
                         firstname='Patrick',
                         lastname='Walukagga')
            )
        response_in = self.tester.post(
            '/index', data = dict(email='pwalukagga@gmail.com', 
                         password='pato123')
        )
        response = self.tester.post(
            '/dashboard',
            data = dict(category_name='Dinner', 
                        description='How to make dinner recipes'),
            follow_redirects=True
        )
        self.assertIn(b'You have successfully added recipe category', 
                       response.data)

if __name__ == '__main__':
    unittest.main()
