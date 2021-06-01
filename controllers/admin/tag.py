from run import app 
from flask import render_template,redirect,request
from flask_login import login_required

@app.route('/admin/tag',methods=['GET','POST'])
@login_required
def admin_tag_index():
    from run import db
    from models import Tag 
    tags=Tag.query.all()
    if request.method == 'POST':
         tag=Tag(
             name=request.form['name']
             
         )
         db.session.add(tag)
         db.session.commit()
         return redirect('/admin/tag')
    return render_template('admin/tag.html', tags=tags)