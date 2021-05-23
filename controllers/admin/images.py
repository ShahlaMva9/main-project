from run import app 
from flask import render_template,redirect,request
import os 
from flask_login import login_required
@login_required
@app.route('/admin/images', methods=['GET','POST'])
def admin_images_index():
    from run import db
    from models import Image
    images=Image.query.all() 
    if request.method=='POST':
        file=request.files['image']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        image=Image(
            image=filename
        )
        db.session.add(image)
        db.session.commit()
        return redirect('/admin/images')
    return render_template('admin/images.html',images=images)


@app.route('/deleteimg/<int:id>')
def deleteimg(id):
    from run import db
    from models import Image
    deleteimg=Image.query.get_or_404(id)

    try:
        db.session.delete(deleteimg)
        db.session.commit()
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],deleteimg.image))
        return redirect("/admin/images")
    except:
        return "sehv oldu"

@app.route('/updateimg/<int:id>', methods=["GET", "POST"])
def update_img(id):
    from run import db
    from models import Image 
    updateimg=Image.query.get_or_404(id)
    if request.method=="POST":
        file=request.files['image']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        updateimg.image=filename
       
        try:
            db.session.commit()
           
            return redirect("/admin/images")
        except:
            return "Sehvoldu"

    return render_template ("/admin/updateimg.html", updateimg=updateimg)