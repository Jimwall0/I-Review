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
    if not request.is_json:
        logger.warning("Invalid Content-Type")
        return jsonify({"error": "Content-Type must be application/json"}), 415
    data = request.get_json()
    logger.debug(f"Recieved data: {data}")
    query = """
    INSERT INTO media (title, release_date, watched, media_type, review)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        data['title'],
        data['release_date'],
        data['watched'],
        data['media_type'],
        data['review'],
    )
    try:
        cursor = db.cursor()
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        logger.info("New media added to database.")
        return jsonify({"message": "Media added successfully!"}), 201
    except Exception as e:
        logger.error(f"Error inserting media: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/')
def index():
    return 'Working go to /media', 200


if __name__ == '__main__':
    app.run(debug=True)
