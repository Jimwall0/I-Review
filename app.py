from flask import Flask, render_template, request, jsonify
from marshmallow import Schema, fields
import mysql.connector
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

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
    return render_template('index.html', media=serialized_media), 200


@app.route('/add_media', methods=['POST'])
def post_media():
    data = request.get_json()
    logger.debug(f"Recieved data: {data}")


@app.route('/')
def index():
    return 'Go to /media'


if __name__ == '__main__':
    app.run(debug=True)
