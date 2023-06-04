from flask import Flask, render_template, redirect, url_for
from flask_migrate import Migrate
from database import db
from blupr import bp
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp, url_prefix='/usuarios')

Migrate(app, db)

@app.route('/')
def startpage():
  return render_template('index.html')

@app.route('/usuarios/login')
def login():
  return render_template('login.html')


app.run(host='0.0.0.0', port=81, debug=True)
