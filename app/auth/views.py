from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from ..models import User
from .forms import LoginForm, RegistrationForm
from ..import db
from ..email import mail_message
from . import auth


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = LoginForm.email.data).first()
        if user is not None and user.verify_password(LoginForm.password.data):
            login_user(user,LoginForm.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Minutes-Pitches | login"
    return render_template('auth/login.html',LoginForm = LoginForm,title=title)



@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        user.save_u()
        mail_message("Welcome to Minute-Pitches","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',RegistratioForm = form)    



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))    