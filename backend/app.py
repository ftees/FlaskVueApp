from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle
from sklearn.cluster import KMeans
import os
import uuid


app = Flask(__name__)
CORS(app) 



df = pd.read_csv(r'C:\Project\templateFlaskVue\backend\uploads\winequality-red.csv', sep=';')

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

 # Render your main HTML file

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        try:
            # Save the uploaded file to the designated folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

            # Optionally, you can perform additional processing here
            return jsonify({'message': 'File successfully uploaded'}), 200

        except Exception as e:
            return jsonify({'error': f'Error during file upload: {str(e)}'}), 500

    return jsonify({'error': 'Invalid file type'}), 400


@app.route("/api/train", methods=["POST"])
def train():
    try:
        if 'model' in request.json and request.json["model"] == 'K-means':
            token = kmeans(request.json)
            print("Token:", token)

        return {"success": True, 'token': token}
    except Exception as e:
        print("Error:", e)
        return {"success": False, 'error': str(e)}




@app.route("/api/predict/<token>", methods=["POST"])
def predict(token):
  with open('models/'+token+'.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    prediction = model.predict(pd.DataFrame([request.json]))[0]
  return {"sucess" : True, 'prediction': prediction}

def kmeans(params):
     
    kmeans_model = KMeans(n_clusters=int(params['clusters']))
    kmeans_model.fit(df)

    models_directory = 'models'
    os.makedirs(models_directory, exist_ok=True)

    token = str(uuid.uuid4())
    with open('models/'+token+'.pkl', 'wb') as model_file:
        pickle.dump(kmeans_model, model_file)
    return token