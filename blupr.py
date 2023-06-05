from flask import Blueprint, render_template, request
from wtforms import StringField, EmailField, IntegerField, PasswordField
from scriptpy import app
from database import db
from models import User
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, EqualTo

class CreateForm(FlaskForm):
  username = StringField('Your name: ', validators=[InputRequired()])
  email = EmailField('Your email: ', validators=[InputRequired()])
  age = IntegerField('Your age: ', validators=[InputRequired()])
  password = PasswordField('Your password:', validators=[InputRequired(), EqualTo('password_confirm', message='Passwords do not match')])
  password_confirm = PasswordField('Confirm password', validators=[InputRequired()])



bp = Blueprint('usuarios', __name__, template_folder='templates')

@bp.route('/create', methods=['GET', 'POST'])
def blueprint():

  form = CreateForm()  
  
  if form.validate_on_submit():
    pass
  
  errors = [{
    'field' : key,
    'message' : form.errors[key],
  } for key in form.errors.keys()] if form.errors else []  
  
  alert = [field['message'] for field in errors]

  if request.method == 'GET':
    return render_template('create.html', form=form, errors=errors, alert=alert)

  if request.method == 'POST':
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User(username, email, password)
    
    db.create_all()
    db.session.add(user)
    db.session.commit()

    return f'{user}'

@bp.route('/recovery')
def login():

  db.create_all()
  
  users = User.query.all()

  return render_template('recovery.html', users=users)