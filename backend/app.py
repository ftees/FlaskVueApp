from flask import Flask
from flask_cors import CORS
from flask import Flask, jsonify, request
import os

from flasgger import Swagger

app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)


@app.route("/")
def home():
    return "Hello, Flask!"


# upload file
@app.route("/upload", methods=["POST"])
def upload():
    """
    Upload File
    ---
    tags:
      - File Operations
    consumes:
      - multipart/form-data
    parameters:
      - in: formData
        name: file
        type: file
        required: true
        description: The file to upload.
    responses:
      200:
        description: File uploaded successfully
      400:
        description: Missing file or no file part in the request
    """
    try:
        file = request.files["file"]
        file.save(os.path.join("uploads", file.filename))
        return jsonify({
            'data': True,
            'message': "upload success",
        })
    except Exception as e:
        return jsonify({
            'data': False,
            'message': "upload fail",
        })
