from run import app 
from flask import render_template,redirect,request
from flask_login import login_required

@app.route('/admin/experience',methods=['GET','POST'])
@login_required
def admin_experience_index():
    from run import db
    from models import Experience 
    experiences=Experience.query.all()
    if request.method == 'POST':
         experience=Experience(
             job_title=request.form['job_title'],
             company=request.form['company'],
             job_date=request.form['job_date'],
             job_content=request.form['job_content']
         )
         db.session.add(experience)
         db.session.commit()
         return redirect('/admin/experience')
    return render_template('admin/experience.html',experiences=experiences)

@app.route('/deleteexp/<int:id>')
def deleteexp(id):
    from run import db
    from models import Experience 
    deleteexp=Experience.query.get_or_404(id)

    try:
        db.session.delete(deleteexp)
        db.session.commit()
        return redirect("/admin/experience")
    except:
        return "sehv oldu"

@app.route('/updateexp/<int:id>', methods=["GET", "POST"])
def update_exp(id):
    from run import db
    from models import Experience 
    updateexp=Experience.query.get_or_404(id)
    if request.method=="POST":
        updateexp.job_title = request.form['job_title']
        updateexp.company = request.form['company']
        updateexp.job_date = request.form['job_date']
        updateexp.job_content = request.form['job_content']
       
        try:
            db.session.commit()
            return redirect("/admin/experience")
        except:
            return "Sehvoldu"

    return render_template ("/admin/updateexp.html", updateexp=updateexp)