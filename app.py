from flask import Flask
import mysql.connector

app = Flask(__name__)

db=mysql.connector.connect(
  host='localhost',
  user='Andy',
  password='@ver@g3V#1w3r',
  database='media_catalog',
)

app.route('/')
def index():
  return 'Hello, World!'

app.run(debug=True)