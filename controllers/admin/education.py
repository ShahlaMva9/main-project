from run import app 
from flask import render_template,redirect,request

@app.route('/admin/education',methods=['GET','POST'])
def admin_education_index():
    from run import db
    from models import Education 
    educations=Education.query.all()
    if request.method == 'POST':
         education=Education(
             education_title=request.form['education_title'],
             university_name=request.form['university_name'],
             education_date=request.form['education_date'],
             education_content=request.form['education_content']
         )
         db.session.add(education)
         db.session.commit()
         return redirect('/admin/education')
    return render_template('admin/education.html',educations=educations)
@app.route('/deleteedu/<int:id>')
def deleteedu(id):
    from run import db
    from models import Education 
    deleteedu=Education.query.get_or_404(id)

    try:
        db.session.delete(deleteedu)
        db.session.commit()
        return redirect("/admin/education")
    except:
        return "sehv oldu"

@app.route('/updateedu/<int:id>', methods=["GET", "POST"])
def update_edu(id):
    from run import db
    from models import Education 
    updateedu=Education.query.get_or_404(id)
    if request.method=="POST":
        updateedu.education_title = request.form['education_title']
        updateedu.university_name = request.form['university_name']
        updateedu.education_date = request.form['education_date']
        updateedu.education_content = request.form['education_content']
       
        try:
            db.session.commit()
            return redirect("/admin/education")
        except:
            return "Sehvoldu"

    return render_template ("/admin/updateedu.html", updateedu=updateedu)