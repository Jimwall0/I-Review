from flask import Flask, jsonify
from marshmallow import Schema, fields
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
  host='localhost',
  user='Andy',
  password='@ver@g3V#1w3r',
  database='media_catalog',
)


class media_schema(Schema):
    id = fields.Int()
    title = fields.Str(required=True)
    watched = fields.Bool()
    media_type = fields.Str()
    recommendation = fields.Str()
    review = fields.Str()


media = media_schema(many=True)


@app.route('/media', methods=['GET'])
def get_media():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM media")
    media_list = cursor.fetchall()
    cursor.close()
    result = media.dump(media_list)
    return jsonify(result)


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
