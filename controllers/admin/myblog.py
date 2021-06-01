from run import app 
from flask import render_template,redirect,request
import os 
from flask_login import login_required


@app.route('/admin/myblog',methods=['GET','POST'])
@login_required
def admin_myblog_index():
    from run import db
    from models import Tag,Blog
    blogs=Blog.query.all()
    tags=Tag.query.all()
    if request.method == 'POST':
        file=request.files['img']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        blog=Blog(
             title=request.form['title'],
             img=filename,
             content=request.form['content'],
             tags=request.form['selected-tag']
         )
        db.session.add(myexperience)
        db.session.commit()
        return redirect('/admin/myexperience')

    return render_template('admin/myblog.html',tags=tags)
   