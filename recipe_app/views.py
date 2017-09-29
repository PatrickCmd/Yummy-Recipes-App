from flask import redirect, render_template, url_for, session, flash, \
                  request

from recipe_app import app

# import cl;ass objects
from classes.app import App
from classes.user import User
from classes.recipe_category import RecipeCategory

# creating App object
recipe_app = App()

# Global user objects
current_user = None
recipes_category = None

# index route
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """Renders index or home page

        Returns:
            an index page template
    """
    if request.method == 'POST':
        # getting form variables
        email = request.form['email']
        password = request.form['password']

        # signing in user
        global current_user
        current_user = User(email, password)

        # creating session
        session['id'] = recipe_app.signin_user(current_user)

        if session['id']:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            error = 'Wrong email or password combination'    
            return render_template('index.html', title='Home', error = error)
    return render_template('index.html', title='Home')

# dashboard view
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """Renders user's dashboard page

        Returns:
            dashboard page template for user
    """
    if 'id' not in session and 'logged_in' not in session:
        flash('You need to login to have access to your dashboard, \
            if not, login or checkout the link below', 'warning')
        return redirect(url_for('index'))
    elif session['id'] == False:
        flash('You need to login to have access to your dashboard, \
            if not, login or checkout the link below', 'warning')
        session.pop('id', None)
        return redirect(url_for('index'))

    global current_user

    if request.method == "POST":
        recipe_catname = request.form['category_name']
        recipe_catdesc = request.form['description']
        # Adding recipe category
        recipes_category = RecipeCategory(recipe_catname, 
                                           recipe_catdesc, 
                                           session['id'])
        if current_user.create_recipe_category(recipes_category):
            flash('You have successfully added recipe category', 
                   'success')
        else:
            flash('Recipe category already exists', 'danger')
        return redirect(url_for('dashboard'))

    # getting user details    
    user_found = [user for user in recipe_app.users 
                   if user.id == session['id']]
    current_user = user_found[0]
    recipe_categories = current_user.get_recipe_categories()
    return render_template('dashboard.html', title='Dashboard', 
                            user = current_user, 
                            categories = recipe_categories)

# signup view
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Renders signup page

        Returns:
            signup page template for user
    """
    if 'logged_in' in session:
        return redirect(url_for('index'))

    if request.method == 'GET':
        return render_template('signup.html', title='Sign Up')
    else:
        # getting form variables
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']

        # creating user object
        global current_user
        current_user = User(email, password, firstname, lastname)
        recipe_app.signup_user(current_user)
        flash('You have successfully created your account, \
               please login into your account', 'success')
    return redirect(url_for('index'))

# logout view
@app.route('/logout')
def logout():
    """Logs out a user"""
    session.pop('logged_in', None)
    session.pop('id', None)
    return redirect(url_for('index'))

