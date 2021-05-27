from run import app 
from flask import render_template,redirect,request
import os 
from flask_login import login_required


@app.route('/admin/myblog',methods=['GET','POST'])
@login_required
def admin_myblog_index():
    from run import db
    from models import Myblog,Tag,tags 
    myblogs=Myblog.query.all()
    if request.method == 'POST':
        file=request.files['img']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        myblog = Myblog(
             title=request.form['title'],
             img=filename,
             content=request.form['content'],
             link=request.form['content'],
             tags=request.form['tags'],
             comment=request.form['comment']
         )
        db.session.add(myblog)
        db.session.commit()
        return redirect('/admin/myblog')
    return render_template('admin/myblog.html',myblogs=myblogs)
   