from flask import Flask,send_file,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired ,Email,Length
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager
from models import *

app=Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

UPLOAD_FOLDER='static/uploads'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_.db"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SECURE_KEY']='mysecret'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

from controllers.app.main import *
from controllers.admin.main import *
from controllers.admin.persinfo import *
from controllers.admin.experience import *
from controllers.admin.education import *
from controllers.admin.skill import *
from controllers.admin.myexperience import *
from controllers.admin.images import *
from controllers.admin.socialprof import *
from controllers.admin.home import *

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/admin/login')

db.create_all()

if __name__=='__main__':
    app.run(debug=True)
