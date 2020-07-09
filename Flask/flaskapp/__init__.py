# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = '8a74d6b55af7824f00b861cf3b445fbe' # A secret key signs cookies when a user visits the site and therefore prevents cookie tampering
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskapp import routes
