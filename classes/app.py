"""Class that creates and signs in user to the application"""

class App(object):
    """create user object and sign in user"""

    def __init__(self):
        self.app_users = []
    
    def signup_user(self, user):
        """creates user for the application

            args:
                user->user object
        """
        
        # check if user already exists
        if [existing_user for existing_user in self.app_users 
             if existing_user.email == user.email]:
            return False

        if self.app_users:
            id = self.app_users[len(self.app_users) - 1].id + 1
            user.id = id
        else:
            user.id = 1
        self.app_users.append(user)
        return user.id

    def signin_user(self, user):
        """logins in user to the dashboard

            args:
                user->user object
            Returns:
                True if user exists
                False if user does not exist or user creditials are wrong
        """
        
        if [existing_user for existing_user in self.app_users 
            if existing_user.email == user.email and 
              existing_user.password == user.password]:
            return True
        return False
