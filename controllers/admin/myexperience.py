from run import app 
from flask import render_template,redirect,request
from flask_login import login_required

@app.route('/admin/myexperience',methods=['GET','POST'])
@login_required
def admin_myexperience_index():
    from run import db
    from models import Myexperience 
    myexperiences=Myexperience.query.all()
    if request.method == 'POST':
         myexperience=Myexperience(
             experience_year=request.form['experience_year'],
             doneproject=request.form['doneproject'],
             happycustomers=request.form['happycustomers']
            
         )
         db.session.add(myexperience)
         db.session.commit()
         return redirect('/admin/myexperience')
    return render_template('admin/myexperience.html', myexperiences=myexperiences)


@app.route('/deletemyexp/<int:id>')
def deletemyexp(id):
    from run import db
    from models import Myexperience 
    deletemyexp=Myexperience.query.get_or_404(id)

    try:
        db.session.delete(deletemyexp)
        db.session.commit()
        return redirect("/admin/myexperience")
    except:
        return "sehv oldu"

@app.route('/updatemyexp/<int:id>', methods=["GET", "POST"])
def update_myexp(id):
    from run import db
    from models import Myexperience 
    updatemyexp=Myexperience.query.get_or_404(id)
    if request.method=="POST":
        updatemyexp.experience_year = request.form['experience_year']
        updatemyexp.doneproject = request.form['doneproject']
        updatemyexp.happycustomers = request.form['happycustomers']
      
       
        try:
            db.session.commit()
            return redirect("/admin/myexperience")
        except:
            return "Sehvoldu"

    return render_template ("/admin/updatemyexp.html", updatemyexp=updatemyexp)