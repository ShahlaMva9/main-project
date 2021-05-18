# run.py icersindeki app
from run import app,send_file,db
from flask import render_template,redirect,request

@app.route('/')
def main_index():
    from models import Persoinfo,Experience,Education,Skill,Myexperience,Image
    print("***********************************************************")
    experiences=Experience.query.all()
    persoinfos=Persoinfo.query.all()
    educations=Education.query.all()
    skills=Skill.query.all()
    myexperiences=Myexperience.query.all()
    images=Image.query.all()
    return render_template ("app/index.html",persoinfos=persoinfos,experiences=experiences,educations=educations,skills=skills,myexperiences=myexperiences,images=images)

# download file

@app.route('/download')
def download_file():
    p="static/app/assets/output.png"
    return send_file(p,as_attachment=True)

