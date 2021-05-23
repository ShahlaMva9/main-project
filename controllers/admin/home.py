from run import app
from flask import render_template,redirect,request
from flask_login import login_required
# from run import db 
@app.route('/admin/home',methods=["GET","POST"])
@login_required
def admin_home_index():
    return render_template ("admin/home.html")