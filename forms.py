from ast import Pass
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets import TextArea

class SignupForm(FlaskForm):
    name=StringField('nombre', validators=[DataRequired(), Length(max=25)])
    password=PasswordField('contra', validators=[DataRequired()])
    email=StringField('email', validators=[DataRequired(), Email()])
    remember_me = BooleanField('recuerdame')
    submit=SubmitField('envio_formulario')

class PostForm(FlaskForm):
    title = StringField('titulo', validators=[DataRequired(), Length(max=128)])
    title_slug  = StringField('titulo slug', validators=[Length(max=128)])
    content = StringField('contenido', widget=TextArea())
    submit= SubmitField('enviar')

class LoginForm(FlaskForm):
    email=StringField('email', validators=[DataRequired()])    
    password=PasswordField('contra', validators=[DataRequired()])
    submit=SubmitField('envio_formulario')
    remember_me = BooleanField('recuerdame')