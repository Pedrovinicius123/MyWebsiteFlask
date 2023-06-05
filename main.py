from flask import render_template, redirect, url_for
from flask_migrate import Migrate
from blupr import bp
from scriptpy import app
from database import db
import os

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

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
