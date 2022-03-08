from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, RegistrationForm
from ..import db
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)    