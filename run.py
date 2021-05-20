from flask import Flask,send_file,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
UPLOAD_FOLDER='static/uploads'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_.db"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import *
from controllers.app.main import *
from controllers.admin.main import *
from controllers.admin.persinfo import *
from controllers.admin.experience import *
from controllers.admin.education import *
from controllers.admin.skill import *
from controllers.admin.myexperience import *
from controllers.admin.images import *
from controllers.admin.socialprof import *



if __name__=='__main__':
    app.run(debug=True)
