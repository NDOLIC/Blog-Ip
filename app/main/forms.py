# from flask_wtf import FlaskForm
# from wtforms import StringField,TextAreaField,SubmitField
# from wtforms.validators import Required

# class ReviewForm(FlaskForm):

#     title = StringField('Review title',validators=[Required()])
#     review = TextAreaField('Movie review', validators=[Required()])
#     submit = SubmitField('Submit')
# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Required, Email, EqualTo
from ..models import User, Post
from wtforms import ValidationError

class PostForm(FlaskForm):
    body = TextAreaField(validators=[Required()])
    submit = SubmitField('Submit')
