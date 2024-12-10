import os

from dotenv import load_dotenv
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

# Load and parse environment file
load_dotenv()

# Constants
PATH_TO_UPLOADS = '../data'
ALLOWED_EXTENSIONS = ['pdf']

# App Configuration
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PATH_TO_UPLOADS
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
CORS(app, resources={r"*": {"origins": "http://localhost:3000"}})


# Routes
@app.route('/')
def default():
    abort(404)


'''
upload_file: receives pdf file from client and stores them on the server.
'''
@app.route('/upload', methods=['POST'])
def upload_file():
    if not request.files:
        print("Sending this error...")
        abort(400)

    file = request.files['file']

    if not (file and file.filename) or not allowed_files(file.filename):
        print(file.filename)
        abort(400)

    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return jsonify({'message': 'File uploaded successfully.'})


'''
list_documents: returns the list of documents stored on server
'''
@app.route('/list-documents', methods=['GET'])
def list_documents():
    return jsonify({'documents': os.listdir(app.config['UPLOAD_FOLDER'])})


# Helpers
def allowed_files(name):
    return '.' in name and name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS