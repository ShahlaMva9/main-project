from run import app 
from flask import render_template,redirect,request
from flask_login import login_required
@app.route('/admin/socialprof',methods=["GET","POST"])
@login_required
def admin_socialicon_index():
    from run import db
    from models import SocialIcon   
    social_icons=SocialIcon.query.all()
    if request.method=="POST":
        social_icon=SocialIcon(
            contact_title=request.form['contact_title'],
            contact_info=request.form['contact_info'],
            contact_icon=request.form['contact_icon'],
            socialIcon=request.form['socialIcon']
        )
        db.session.add(social_icon)
        db.session.commit()
        return redirect("/admin/socialprof")
    return render_template ("admin/socialprof.html" ,social_icons=social_icons)

@app.route('/deletesocialicon/<int:id>')
def deletesocialicon(id):
    from run import db
    from models import SocialIcon 
    deletesocialicon=SocialIcon.query.get_or_404(id)

    try:
        db.session.delete(deletesocialicon)
        db.session.commit()
        return redirect("/admin/socialprof")
    except:
        return "sehv oldu"
    

@app.route('/updatesocialicon/<int:id>', methods=["GET", "POST"])
def update_social_icon(id):
    from run import db
    from models import SocialIcon 
    updatesocialicon=SocialIcon.query.get_or_404(id)
    if request.method=="POST":
        updatesocialicon.contact_title = request.form['contact_title']
        updatesocialicon.contact_info = request.form['contact_info']
        updatesocialicon.contact_icon = request.form['contact_icon']
        updatesocialicon.socialIcon = request.form['socialIcon']
      
        try:
            db.session.commit()
            return redirect("/admin/socialprof")
        except:
            return "Sehvoldu"

    return render_template ("/admin/updatesocialicon.html", updatesocialicon=updatesocialicon)
 