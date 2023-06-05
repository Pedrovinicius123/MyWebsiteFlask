from database import db

class User(db.Model):

  __tablename__ = 'users'
  
  id = db.Column('ID', db.Integer, primary_key=True)
  username = db.Column(db.String(100))
  email = db.Column(db.String(100))
  password = db.Column(db.String(100))

  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password

  def __repr__(self):
    return f'Hello {self.username}'
  