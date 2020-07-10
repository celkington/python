# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = '8a74d6b55af7824f00b861cf3b445fbe' # A secret key signs cookies when a user visits the site and therefore prevents cookie tampering
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskapp import routes
