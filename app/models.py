from enum import unique
from operator import index
from unicodedata import category
from . import db

from sqlalchemy.orm import backref
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from datetime import datetime, time


class User(UserMixin,db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255),index = True)
  email = db.Column(db.String(255),unique = True,index = True)
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  password_hash = db.Column(db.String(255))



  def __repr__(self):
      return f'User {self.username}'



class Pitches(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category_of_the_pitch = db.Column(db.String(150), index = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pitch = db.Column (db.text(), nullable= False)
    comments = db.relationship('Comment', backref='pitch', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable=False)

    def save_comment (self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_comments(cls, id):
        comments = Comment.query.filter_by(post_id=id) .all()
    
    def __repr__(self):
        return f"Comment('{self.comment}', '{self.user_id}')"           


class PostLike(db.Model):
     __tablename__ = 'post_like'

     id = db.Column(db.Integer, primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     post_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

     def save_postlike(self):
         db.session.add(self)
         db.session.commit()

     
     @classmethod
     def fetch_postlike(cls, id):
        comments = PostLike.query.filter_by(post_id=id) .all()    


     def __repr__(self):
        return f"Comment('{self.comment}', '{self.user_id}')"      