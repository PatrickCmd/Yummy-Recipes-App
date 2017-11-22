from flask import redirect, render_template, url_for, session, flash, \
                  request

from recipe_app import app

# import class objects
from classes.app import App
from classes.user import User
from classes.recipe_category import RecipeCategory
from classes.recipe import Recipe

# creating App object
recipe_app = App()

# Global user objects
current_user = None
recipes_category = None
recipe = None

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
        print(session['id'])

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

# single recipe category view
@app.route('/recipe_category/<categoryname>')
def recipe_category(categoryname):
    """Renders template for single recipe category

        args:
            name->Recipe category name
    """
    if 'id' not in session and 'logged_in' not in session:
        flash('You need to login to have access to your dashboard, \
            if not, login or checkout the link below', 'warning')
        return redirect(url_for('index'))

    user = [user for user in recipe_app.users 
             if user.id == session['id']]
    recipecategory = user[0].get_single_category(categoryname)
    
    return render_template('single_category.html', 
                            category=recipecategory, 
                            name=categoryname)

# edit recipe category view
@app.route('/edit_recipe_category/<categoryname>', methods=['POST'])
def edit_recipe_category(categoryname):
    """Edits recipe category 

       args:
            categoryname->name of category to be edited
    """
    if 'id' not in session and 'logged_in' not in session:
        flash('You need to login to have access to your dashboard, \
            if not, login or checkout the link below', 'warning')
        return redirect(url_for('index'))

    user = [user for user in recipe_app.users 
             if user.id == session['id']]
    if request.method == 'POST':
        category_name = request.form['category_name']
        description = request.form['description']
    edited_category = user[0].edit_recipe_category(categoryname, 
                                                    category_name,
                                                    description)
    flash('Category has been updated', 'success')
    return redirect(url_for('recipe_category', 
                            categoryname=edited_category[0].name))
    

# delete recipe category view
@app.route('/delete_recipe_category/<categoryname>')
def delete_recipe_category(categoryname):
    """Deletes recipe category 

       args:
            categoryname->name of category to be deleted 
    """
    if 'id' not in session and 'logged_in' not in session:
        flash('You need to login to have access to your dashboard, \
            if not, login or checkout the link below', 'warning')
        return redirect(url_for('index'))

    user = [user for user in recipe_app.users 
             if user.id == session['id']]
    if user[0].delete_recipe_category(categoryname):
        flash("You have delete recipe category", "danger")
    return redirect(url_for('dashboard'))

# Add recipe into category
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    """Add recipes to recipe category"""

    if 'id' not in session and 'logged_in' not in session:
        flash('You need to login to have access to your dashboard, \
            if not, login or checkout the link below', 'warning')
        return redirect(url_for('index'))

    if request.method == 'POST':
        category_name = request.form['category_name']
        recipe_name = request.form['recipe_name']
        ingredients = request.form['ingredients']
        description = request.form['description']

        user = [user for user in recipe_app.users 
                if user.id == session['id']]
        
        category = user[0].get_single_category(category_name)
        recipe = Recipe(recipe_name, description, ingredients)
        if user[0].add_recipe(category, recipe):
            return redirect(url_for('recipe_category', 
                                     categoryname=category_name))        

# get single recipe view
@app.route('/recipe/<recipename>')
def get_recipe(recipename):
    """Returns single recipe

       args:
            recipename->name of recipe item
    """
    if 'id' not in session and 'logged_in' not in session:
        flash('You need to login to have access to your dashboard, \
            if not, login or checkout the link below', 'warning')
        return redirect(url_for('index'))

    user = [user for user in recipe_app.users 
             if user.id == session['id']]
    category = [category for category in user[0].recipe_categories 
                 if category.user_id == session['id']]
    recipe = user[0].get_single_recipe_from_category(category[0], 
                                                     recipename)
    return render_template('recipe.html', recipe=recipe)

# edit recipe item
@app.route('/recipe/<recipename>', methods=['POST'])
def edit_recipe(recipename):
    """Returns single recipe

       args:
            recipename->name of recipe item
    """
    if 'id' not in session and 'logged_in' not in session:
        flash('You need to login to have access to your dashboard, \
            if not, login or checkout the link below', 'warning')
        return redirect(url_for('index'))

    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        ingredients = request.form['ingredients']
        description = request.form['description']

    user = [user for user in recipe_app.users 
             if user.id == session['id']]
    category = [category for category in user[0].recipe_categories 
                 if category.user_id == session['id']]
    
    if user[0].edit_recipe_in_category(category[0], recipename, 
                                        recipe_name, 
                                        description, 
                                        ingredients):
        flash("Recipe updated successfully", "success")
        return redirect(url_for('recipe_category', 
                                categoryname=category[0].name))
    

# delete recipe from category
@app.route('/delete_recipe/<recipename>')
def delete_recipe(recipename):
    """Delete recipe from category

        args:
            recipename->name of recipe item
    """
    if 'id' not in session and 'logged_in' not in session:
        flash('You need to login to have access to your dashboard, \
            if not, login or checkout the link below', 'warning')
        return redirect(url_for('index'))
    
    user = [user for user in recipe_app.users 
             if user.id == session['id']]
    category = [category for category in user[0].recipe_categories 
                 if category.user_id == session['id']]
    if user[0].delete_recipe_from_category(category[0],
                                           recipename):
        flash("You have deleted recipe item", "danger")
        return redirect(url_for('recipe_category', 
                                categoryname=category[0].name))

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

