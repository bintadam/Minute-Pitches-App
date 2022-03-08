from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField,ValidationError
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')