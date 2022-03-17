from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from ..models import User, Pitch, Comment, Upvote, Downvote
from .. import db,photos
from flask_login import login_required, current_user
from .forms import PitchForm, UpdateProfile, CommentForm

@main.route('/')
def main_page():
    '''this is my main page where a user will either login or register to access the site'''

    return redirect(url_for('auth.login'))

@main.route('/login')
def landing_page():
    title = 'Mathwiti | Login'
    return render_template('index.html', title = title)

@main.route('/profile')
def profile_page():
    title = 'Mathwiti | Profile'
    return render_template('profile/profile.html', title = title)

@main.route('/job')
def job_page():
    title = 'Mathwiti | Job'
    pitch = Pitch.query.filter_by(category_of_the_pitch = 'Job').all()
    return render_template('job_page.html', title = title, pitch=pitch)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    title = 'Mathwiti | Create Pitch'
    job_new = PitchForm()
    if job_new.validate_on_submit():
        kichwa = job_new.title.data
        post = job_new.post.data
        category = job_new.category.data
        owner_id = current_user
        new_job = Pitch(user_id=current_user._get_current_object().id,pitch=post,category_of_the_pitch=category)
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('main.profile_page'))
    return render_template('newPitch.html', title = title,job_new=job_new)

@main.route('/advert')
def advert():
    title = "Mathwiti | Advertisements"
    pitch = Pitch.query.filter_by(category_of_the_pitch = 'Advertisement').all()
    return render_template("advertisment.html", title= title, pitch=pitch)

