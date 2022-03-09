from enum import unique
from flask import render_template,request,redirect,url_for,abort
from sqlalchemy import null

from app import email
from . import main
from flask_login import login_required
from ..models import User
from .forms import UpdateProfile
from .. import db,photos
from datetime import datetime


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique=True, nullable= False)
    email = db.Column (db.Strin)
    pass_secure = db.Column(db.String(255), nullable=False)
    profile_pic_path = db.Column(db.String())
    bio =db.Column(db.String(255))



@main.route('/user/<uname>/update',methods = ['GET','POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)    


@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


