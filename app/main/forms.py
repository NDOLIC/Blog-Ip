from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Required, Email, EqualTo
from ..models import User, Post
from wtforms import ValidationError

class PostForm(FlaskForm):
    content = TextAreaField(validators=[Required()])
    submit = SubmitField('Submit')
