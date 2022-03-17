from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required,Email,EqualTo

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Job','Job'),('Advertisement','Advertisement')],validators=[Required()])
    post = TextAreaField('write your pitch here...', validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Care to leave a comment here?',validators=[Required()])
    submit = SubmitField('Post Comment')
