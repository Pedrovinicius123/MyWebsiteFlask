from flask import Blueprint, render_template
from wtforms import StringField, EmailField, IntegerField, PasswordField
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
    return 'Ok'
  
  errors = [{
    'field' : key,
    'message' : form.errors[key],
  } for key in form.errors.keys()] if form.errors else []

  alert = [field['message'] for field in errors]
  
  return render_template('create.html', form=form, errors=errors, alert=alert)
