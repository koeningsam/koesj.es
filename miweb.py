from email.message import EmailMessage
from unicodedata import name
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import parse_qs
from flask import Flask, render_template, url_for, request, redirect
import os
from forms import SignupForm, PostForm, LoginForm
#from flask_login import LoginManager, current_user, login_user, logout_user, login_required
#from models import User

miweb=Flask(__name__)

miweb.config['SECRET KEY']= 'veyronkoeningregeraagerachirionmaseratilamborghini123456789¡º123456789asno'

miweb.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:maserati@localhost:5432/miwebflask'

miweb.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

'''login_manager=LoginManager(miweb)

login_manager.login_view='login'

db=SQLAlchemy(miweb)'''

@miweb.route('/')
@miweb.route('/inicio')
def inicio():

    return render_template('indice.html')

@miweb.route('/links')
def links():

    return render_template('links.html')

@miweb.route('/contactos')
def contactos():

    return render_template('contactos.html')


'''@miweb.route('/registro', methods=["GET", "POST"])
def registro():
    form=SignupForm()

    error=None

    if form.validate_on_submit:

        nombre= form.name.data
        email= form.email.data
        password= form.password.data

        user=User.get_by_email(email)

        if user is not None:
            error=f'el email {email} ya existe'
        else:
            user=User(nombre=nombre, email=email)
            user.set_password(password)
            user.save
            
            login_user(user, remember=True)

            return redirect(url_for('inicio'))
    
    return render_template('registro.html', form=form)

@miweb.route('/iniciar', methods=["GET", "POST"])
def iniciar():

    if current_user.is_authenticated:
        return redirect(url_for('inicio'))

    form=LoginForm()

    if form.validate_on_submit():
        user=User.get_by_email(form.email.data)

        if user is not None and (user.check_password(form.password.data)==form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page=request.args.get("next")
            if not next_page:
                next_page=url_for("inicio")
            return redirect(next_page)

    return render_template('iniciar.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))

@miweb.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('inicio'))'''


@miweb.route('/links1')
def links1():

    return render_template('links1.html')



if __name__=='__main__':

    os.environ['FLASK_ENV']='development'
    miweb.run(debug=True)
