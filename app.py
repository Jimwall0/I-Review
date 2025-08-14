from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlclient://username:password@localhost/database_name'
db = SQLAlchemy(app)

class media(db.model):
  