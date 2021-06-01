# run.py icersindeki app
from run import app,send_file,db
from flask import render_template,redirect,request

@app.route('/')
def main_index():
    from models import Persoinfo,Experience,Education,Skill,Myexperience,Image,SocialIcon
    print("***********************************************************")
    experiences=Experience.query.all()
    persoinfos=Persoinfo.query.all()
    educations=Education.query.all()
    skills=Skill.query.all()
    myexperiences=Myexperience.query.all()
    images=Image.query.all()
    social_icons=SocialIcon.query.all()
    
    return render_template ("app/index.html",persoinfos=persoinfos,experiences=experiences,educations=educations,skills=skills,myexperiences=myexperiences,images=images,social_icons=social_icons)

# download file

@app.route('/download')
def download_file():
    p="static/app/assets/output.png"
    return send_file(p,as_attachment=True)

@app.route('/blog')
def blog_index():
     return render_template ("app/blog.html")

@app.errorhandler(404)

# inbuilt function which takes error as parameter
def not_found(e):

# defining function
    return render_template("404.html")