from run import app
from flask import render_template,redirect,request
from flask_login import login_required
# from run import db 
@app.route('/admin/persinfo',methods=["GET","POST"])
@login_required
def admin_persinfo_index():
    from run import db
    from models import Persoinfo   
    persoinfos=Persoinfo.query.all()
    if request.method=="POST":
        persoinfo=Persoinfo(
            pers_info_title=request.form['pers_info_title'],
            pers_info_content=request.form['pers_info_content']
        )
        db.session.add(persoinfo)
        db.session.commit()
        return redirect("/admin/persinfo")
    return render_template ("admin/persinfo.html" ,persoinfos=persoinfos)
@app.route('/delete/<int:id>')
def delete(id):
    from run import db
    from models import Persoinfo 
    persoinfodelete=Persoinfo.query.get_or_404(id)

    try:
        db.session.delete(persoinfodelete)
        db.session.commit()
        return redirect("/admin/persinfo")
    except:
        return "sehv oldu"

@app.route('/updatepersinfo/<int:id>', methods=["GET", "POST"])
def update_persinfo(id):
    from run import db
    from models import Persoinfo 
    persoinfoupdate=Persoinfo.query.get_or_404(id)
    if request.method=="POST":
        persoinfoupdate.pers_info_title = request.form['pers_info_title']
        persoinfoupdate.pers_info_content = request.form['pers_info_content']
      
        
        try:
            db.session.commit()
            return redirect("/admin/persinfo")
        except:
            return "Sehvoldu"

    return render_template ("/admin/updatepersinfo.html", persoinfoupdate=persoinfoupdate)
 