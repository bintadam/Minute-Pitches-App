from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField,ValidationError
from wtforms.validators import Required, Email, EqualTo


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title = StringField ('Title', validators=[Required()])
    post = TextAreaField ('pitch')
    category = SelectField('Category', choices=[('Shuqul', 'Shuqul')('Camal' 'Camal')('Xayasin' 'Xayasin')], validators=[Required()])
    submit  = SubmitField('Post')  


class AddCommentForm(FlaskForm):
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Post')    