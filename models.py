from run import db
from wtforms import SelectField
from flask_wtf import FlaskForm
from flask_login import UserMixin
from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired ,Email
class Persoinfo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    pers_info_title=db.Column(db.String(50))
    pers_info_content=db.Column(db.String(50))
    
    

class Experience(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    job_title=db.Column(db.String(50))
    company=db.Column(db.String(50))
    job_date=db.Column(db.String(50))
    job_content=db.Column(db.String(250))

class Education(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    education_title=db.Column(db.String(50))
    university_name=db.Column(db.String(50))
    education_date=db.Column(db.String(50))
    education_content=db.Column(db.String(250))
class Skill(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skill_name=db.Column(db.String(50))
    skill_rate1=db.Column(db.String(50))
    skill_rate2=db.Column(db.String(50))
    skill_rate3=db.Column(db.String(50))
    skill_rate4=db.Column(db.String(50))
    skill_rate5=db.Column(db.String(50))

class Myexperience(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    experience_year=db.Column(db.String(50))
    doneproject=db.Column(db.String(50))
    happycustomers=db.Column(db.String(50))

class Image(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    image=db.Column(db.String(100))
class SocialIcon(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contact_title=db.Column(db.String(50))
    contact_info=db.Column(db.String(50))
    contact_icon=db.Column(db.String(50))
    socialIcon=db.Column(db.String(50))
class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True)
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(80))

class LoginForm(FlaskForm):
    username=StringField('username',validators=[InputRequired()])
    password=PasswordField('password',validators=[InputRequired()])
    remember=BooleanField('remember me')
class RegisterForm(FlaskForm):
    email=StringField('email',validators=[InputRequired()])
    username=StringField('username',validators=[InputRequired()])
    password=PasswordField('password',validators=[InputRequired()])
