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
  comments = db.relationship('Comment', backref='user', lazy='dynamic')
  PostLike = db.relationship('PostLike', backref='user', lazy='dynamic')
  PostDisLike = db.relationship('PostDisLike', backref='user', lazy='dynamic')

  @property
  def set_password(self):
      raise AttributeError('You cannot read the password attribute')

  @set_password.setter
  def password(self, password):
      self.secure_password = generate_password_hash(password)

  
  def verify_password(self, password):
      return check_password_hash(self.secure_password,password) 
  
  def save_u(self):
      db.session.add(self)
      db.session.commit()

  def delete(self):
      db.session.delete(self)
      db.session.commit()
  
  def __repr__(self):
      return f'User {self.username}'

  def __repr__(self):
      return f'User {self.username}'


class Pitches(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category = db.Column(db.String(150), index = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post = db.Column(db.Text(), nullable= False)
    comments = db.relationship('Comment', backref='pitches', lazy='dynamic')
    PostLike = db.relationship('PostLike', backref='pitches', lazy='dynamic')
    PostDisLike = db.relationship('PostDisLike', backref='pitches', lazy='dynamic')
    
    @classmethod
    def fetch_pitches(cls, id):
        pitches = Pitches.query.filter_by(post_id=id) .desc() .all()
        return pitches


    def save_p(self):
        db.session.add(self)
        db.session.commit()
    

    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
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
     user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
     pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

     def save_postlike(self):
         db.session.add(self)
         db.session.commit()

     
     @classmethod
     def fetch_postlike(cls, id):
        comments = PostLike.query.filter_by(post_id=id) .all()    


     def __repr__(self):
        return f"Comment('{self.comment}', '{self.user_id}')"      



class PostDisLike(db.Model):
     __tablename__ = 'post_dislike'

     id = db.Column(db.Integer, primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
     pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

     def save_postdislike(self):
         db.session.add(self)
         db.session.commit()

     
     @classmethod
     def fetch_postlike(cls, id):
        comments = PostDisLike.query.filter_by(post_id=id) .all()    


     def __repr__(self):
        return f"Comment('{self.comment}', '{self.user_id}')"              



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)        