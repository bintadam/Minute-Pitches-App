from flask import render_template,request,redirect,url_for,abort, flash

from . import main
from flask_login import login_required, current_user
from ..models import User, Pitches, Comment
from .forms import UpdateProfile, PitchForm, AddCommentForm
from .. import db,photos


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



@main.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
@login_required
def new_pitch(post_id):
    title = 'minutePitches'
    new_job= PitchForm()
    if new_job.validate_on_submit():
        head = new_job.title.data
        post = new_job.post.data
        category = new_job.category.data
        owner_id = current_user

        new_shaqo = Pitches(user_id= current_user._get_current_object().id, pitch=post, category_of_the_pitch= category)
        db.session.add(new_shaqo)
        db.session.commit()
    
        return redirect(url_for("main", profile_page))
    return render_template("newPitch.html", title="title", new_job=new_shaqo)





@main.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
@login_required
def comment_post(post_id):
    form = AddCommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data, article=Pitches.id)
        db.session.add(comment)
        db.session.commit()
        flash("Your comment has been added to the post", "success")
        return redirect(url_for("post", post_id=Pitches.id))
    return render_template("comment_post.html", title="Comment Post", form=form)

