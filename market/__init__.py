from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app  = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fsxmaxudgsmval:5b68ae96554d15f27cc9046c352f219cb63295d58f82b223d5f25f14c15eec23@ec2-54-161-255-125.compute-1.amazonaws.com:5432/dfpvre1jpjtqek'
app.config['SECRET_KEY'] = '86eb8a7b4678de643546cbe5'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"


from market import routes
