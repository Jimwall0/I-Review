from flask import Flask, render_template
from marshmallow import Schema, fields
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
  host='localhost',
  user='Andy',
  password='@ver@g3V#1w3r',
  database='media_catalog',
)


class MediaSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True)
    watched = fields.Str()
    media_type = fields.Str()
    recommendation = fields.Str()
    review = fields.Str()


media = MediaSchema(many=True)


@app.route('/media', methods=['GET'])
def get_media():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM media")
    media_list = cursor.fetchall()
    cursor.close()
    serialized_media = media.dump(media_list)
    return render_template('index.html', media=serialized_media)


@app.route('/media/:id', methods=['GET'])
def get_ip():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT ${id} FROM media")
    target = cursor.fetchall()
    cursor.close()
    serialized = media.dump(target)
    return render_template('index.html', media=serialized)


@app.route('/')
def index():
    return 'Go to /media'


if __name__ == '__main__':
    app.run(debug=True)
