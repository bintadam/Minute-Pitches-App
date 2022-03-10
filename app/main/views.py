from flask import render_template,request,redirect,url_for,abort

from . import main
from flask_login import login_required, current_user
from ..models import User, Pitches, Comment
from .forms import UpdateProfile, PitchForm, AddCommentForm
from .. import db,photos


@main.route('/')
def index():
    pitches = Pitches.query.all()
    job = Pitches.query.filter_by(category = 'Job').all() 
    event = Pitches.query.filter_by(category = 'Events').all()
    advertisement = Pitches.query.filter_by(category = 'Advertisement').all()
    return render_template('index.html', job = job,event = event, pitches = pitches,advertisement= advertisement)


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


@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if new_amal.validate_on_submit():
        title = new_amal.title.data
        post = new_amal.post.data
        category = new_amal.category.data
        user_id = current_user
        new_amal = Pitches(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        db.session.add(new_amal)
        return redirect(url_for('main.index'))
        
    return render_template('newPitch.html', form = form)   



@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = AddCommentForm()
    pitch = Pitches.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)     










