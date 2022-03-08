from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


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


