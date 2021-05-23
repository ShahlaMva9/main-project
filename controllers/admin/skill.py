from run import app 
from flask import render_template,redirect,request
from flask_login import login_required

@app.route('/admin/skill',methods=['GET','POST'])
@login_required
def admin_skill_index():
    from run import db
    from models import Skill 
    skills=Skill.query.all()
    if request.method == 'POST':
         skill=Skill(
             skill_name=request.form['skill_name'],
             skill_rate1=request.form['skill_rate1'],
             skill_rate2=request.form['skill_rate2'],
             skill_rate3=request.form['skill_rate3'],
             skill_rate4=request.form['skill_rate4'],
             skill_rate5=request.form['skill_rate5']

         )
         db.session.add(skill)
         db.session.commit()
         return redirect('/admin/skill')
    return render_template('admin/skill.html',skills=skills)
@app.route('/deleteskill/<int:id>')
def deleteskill(id):
    from run import db
    from models import Skill 
    deleteskill=Skill.query.get_or_404(id)

    try:
        db.session.delete(deleteskill)
        db.session.commit()
        return redirect("/admin/skill")
    except:
        return "sehv oldu"

@app.route('/updateskill/<int:id>', methods=["GET", "POST"])
def update_skill(id):
    from run import db
    from models import Skill 
    updateskill=Skill.query.get_or_404(id)
    if request.method=="POST":
        updateskill.skill_name = request.form['skill_name']
        updateskill.skill_rate1 = request.form['skill_rate1']
        updateskill.skill_rate2 = request.form['skill_rate2']
        updateskill.skill_rate3 = request.form['skill_rate3']
        updateskill.skill_rate4 = request.form['skill_rate4']
        updateskill.skill_rate5 = request.form['skill_rate5']
        
        try:
            db.session.commit()
            return redirect("/admin/skill")
        except:
            return "Sehvoldu"

    return render_template ("/admin/updateskill.html", updateskill=updateskill)
 