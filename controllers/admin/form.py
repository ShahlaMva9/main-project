from run import app 
from flask import render_template,redirect,request, jsonify
from flask_login import login_required

@app.route('/admin/form',methods=['POST'])
def admin_form_index():
    from run import db
    from models import Message
    messages=Message.query.all()
    if request.method=='POST':
        message=Message(
            user_name = request.form["user_name"],
            user_email = request.form["user_email"],
            user_comment = request.form["user_comment"]
                )
        db.session.add(message)
        db.session.commit()
        data = {'name': 'nabin khadka'}
        return ('', 200)
    

@app.route('/deletemessage/<int:id>')
def deletemessage(id):
    from run import db
    from models import Message 
    deletemessage=Message.query.get_or_404(id)

    try:
        db.session.delete(deletemessage)
        db.session.commit()
        return redirect("/admin/form")
    except:
        return "sehv oldu"