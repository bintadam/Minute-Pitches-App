from enum import unique
from operator import index

from sqlalchemy.orm import backref
from . import db
from flask_login import UserMixin, current_user
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime, time

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)




class User(UserMixin,db.Model):

    '''class user with its properties'''

    __tablename__ = 'users'

    #nullable = False tells SQLAlchemy to create the column as NOT NULL

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique=True,nullable = False)
    email = db.Column(db.String(255),unique=True,nullable = False)
    pass_secure = db.Column(db.String(255),nullable = False)
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))


    post = db.relationship('Pitch', backref = 'user', lazy = 'dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    upvote = db.relationship('Upvote', backref = 'user', lazy = 'dynamic')
    downvote = db.relationship('Downvote', backref = 'user', lazy = 'dynamic')

    
    @property
    def password(self):
        raise AttributeError('You can not access the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f'User {self.username}'



class Pitch(db.Model):
    '''class pitch and its properties'''

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch = db.Column(db.Text(), nullable = False)
    time_posted = db.Column(db.DateTime, default = datetime.utcnow)
    category_of_the_pitch = db.Column(db.String(150), index = True, nullable = False)
    comments = db.relationship('Comment',backref='pitch',lazy='dynamic')
    upvote = db.relationship('Upvote', backref = 'pitch', lazy = 'dynamic')
    downvote = db.relationship('Downvote', backref = 'pitch', lazy = 'dynamic')



    @classmethod
    def fetch_pitches(cls, id):
        pitches = Pitch.query.order_by(post_id= id).desc().all()
        return pitches

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def delete_pitch(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Pitch {self.pitch}'



class Comment(db.Model):
    '''class comment and its properties'''

    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text(), nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_comments(cls,id):
        comments = Comment.query.filter_by(post_id=id).all()

        return comments

    def __repr__(self):
        return f'comment:{self.comment}'

class Upvote(db.Model):

    __tablename__ = 'upvotes'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_by_post(cls,id):
        upvote_by_post=Upvote.query.filter_by(post_id=id).all()
        return upvote_by_post

    def __repr__(self) -> str:
        return f'Upvote{self.user_id}:{self.post_id}'

class Downvote(db.Model):

    __tablename__ = 'downvotes'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_downvotes(cls,id):
        downvote = Downvote.query.filter_by(post_id = id).all()
        return downvote

    def __repr__(self) -> str:
        return f'{self.user_id}:{self.post_id}'





    

