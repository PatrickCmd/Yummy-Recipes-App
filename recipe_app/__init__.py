import os
from flask import Flask

# flask app object
app = Flask(__name__)
# secret key
app.secret_key = os.urandom(24)

# application views
from recipe_app import views
