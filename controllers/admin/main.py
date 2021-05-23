# run.py icersindeki app
from run import app 
from flask import abort,render_template,redirect,request,url_for, session, g
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_required,login_user, current_user, logout_user
        

@app.before_request
def before_request():
    g.user = current_user

@app.route('/admin')
@login_required
def admin_index():
    from run import db
    from models import LoginForm,User
    form = LoginForm()
    return render_template ("admin/login.html",form=form)

@app.route('/admin/login' , methods=['GET',"POST"])
def login_index():
    from run import db
    from models import LoginForm,User
    form =LoginForm()
    if form.validate_on_submit():
        users = User.query.all()
        user = list(filter(lambda users: users.username == form.username.data, users))[0]
        if user:
                if check_password_hash(user.password,form.password.data):
                    session['user_id'] = user.id
                    g.user = user
                    login_user(user)
                    return redirect(url_for('dashboard'))
                else:
                    return 'Invalid username or Password'
    return render_template ("admin/login.html",form=form)

       

@app.route('/admin/signup',methods=['GET',"POST"])
def signup_index():
    from run import db
    from models import RegisterForm,User
    form=RegisterForm()
    if form.validate_on_submit():
        hashed_password=generate_password_hash(form.password.data,method='sha256')
        new_user=User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return '<h1>New user has ben created</h1>'
        #return '<h1>'+ form.username.data + ' ' + form.email.data + ' ' + form.password.data +'</h1>'
    return render_template ("admin/signup.html",form=form)

@app.route('/admin/dashboard')
@login_required
def dashboard():
    return render_template ("admin/dashboard.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/admin/login')