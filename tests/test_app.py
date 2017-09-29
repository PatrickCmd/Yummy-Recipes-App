import unittest

from classes.app import App
from classes.user import User

class TestAppCase(unittest.TestCase):

    def setUp(self):
        self.app = App()
        self.user = User('pwalukagga@gmail.com', 'pato123', 'Patrick', 
                          'Walukagga')
    
    def test_signup_user_is_created(self):
        self.app.signup_user(self.user)
        self.assertEqual(len(self.app.users), 1)
        index = len(self.app.users) -1
        self.assertEqual(self.app.users[index].email, 
                         'pwalukagga@gmail.com')
        self.assertEqual(self.app.users[index].password, 'pato123')
        self.assertEqual(self.app.users[index].first_name, 'Patrick')
        self.assertEqual(self.app.users[index].last_name, 'Walukagga')
    
    def test_signup_user_with_same_email_already_exists(self):
        self.app.signup_user(self.user)
        self.user = User('pwalukagga@gmail.com', 'pat123', 'Rickson', 
                          'Walukagga')
        self.assertFalse(self.app.signup_user(self.user))
    
    def test_signup_user_returns_correct_id(self):
        self.app.signup_user(self.user)
        self.assertEqual(len(self.app.users), 1)
        self.user = User('henry@gmail.com', 'henry123', 'Henry', 
                          'Kato')
        self.app.signup_user(self.user)
        self.assertEqual(len(self.app.users), 2)
        self.user = User('henry@ymail.com', 'henry0009', 'Henry', 
                          'Mutunji')
        self.app.signup_user(self.user)
        self.assertEqual(len(self.app.users), 3)
    
    def test_signin_user_logins_successfully(self):
        self.app.signup_user(self.user)
        self.user = User('pwalukagga@gmail.com', 'pato123')
        self.assertEqual(self.app.signin_user(self.user), 1)

    def test_signin_user_login_fails_with_wrong_email_password(self):
        self.app.signup_user(self.user)
        self.user = User('pathen@gmail.com', 'pat1234')
        self.assertFalse(self.app.signin_user(self.user))

if __name__ == '__main__':
    unittest.main()