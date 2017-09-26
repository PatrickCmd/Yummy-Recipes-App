from flask import redirect, render_template, url_for, session, flash, \
                  request

from recipe_app import app

# import cl;ass objects
from classes.app import App
from classes.user import User

# creating App object
recipe_app = App()

# Global user objects
current_user = None

# index route
@app.route('/')
@app.route('/index')
def index():
    """Renders index or home page

        Returns:
            an index page template
    """
    return render_template('index.html', title='Home')

# dashboard view
@app.route('/dashboard')
def dashboard():
    """Renders user's dashboard page

        Returns:
            dashboard page template for user
    """
    return render_template('dashboard.html', title='Dashboard')

# signup view
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Renders signup page

        Returns:
            signup page template for user
    """

    if request.method == 'GET':
        return render_template('signup.html', title='Sign Up')
    else:
        print(request.form)
        # getting form variables
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
    
