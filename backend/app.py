from flask import Flask, g
from flask_cors import CORS
from flask import Flask, jsonify, request
import os
import io
from sklearn.cluster import KMeans
import pickle
import pandas as pd
import numpy as np
import uuid
import base64
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app) 


@app.route("/")
def home():
    return "Hello, Flask!"

df = r'D:\projetweb\backend\uploads\wine.csv'


# upload file
@app.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files["file"]
        file.save(os.path.join("uploads", 'file.csv'))

        return jsonify({
            'data': True,
            'message': "upload success",
        })
    except Exception as e:
        return jsonify({
            'data': False,
            'message': "upload fail",
        })
    

# upload file
@app.route("/api/train", methods=["POST"])
def train():
  if(request.json["model"] == 'K-means'):
      token = kmeans(request.json)

  return {"sucess" : True, 'token': token}

# generate kmeans model
def kmeans(params):
    dataframe = pd.read_csv(r"uploads\file.csv")
    kmeans_model = KMeans(n_clusters=int(params['clusters']))
    kmeans_model.fit(dataframe)
    token = str(uuid.uuid4())
    with open('models/'+token+'.pkl', 'wb') as model_file:
        pickle.dump(kmeans_model, model_file)
    return token


@app.route("/api/predict/<token>", methods=["POST"])
def predict(token):
    try:
        model_filename = f'models/{token}.pkl'
        
        # Check if the model file exists
        if not os.path.exists(model_filename):
            return jsonify({"success": False, "error": "Model not found"}), 404

        with open(model_filename, 'rb') as model_file:
            model = pickle.load(model_file)
        
        # Read the CSV file for prediction
        dataframe = pd.read_csv(r"uploads\file.csv")
        predictions = model.predict(dataframe)
        
        # Create a bar chart
        plt.bar(range(len(predictions)), predictions)
        plt.xlabel('Sample Index')
        plt.ylabel('Cluster Prediction')
        plt.title('K-Means Cluster Predictions')
        
        # Convert the plot to a base64-encoded image
        image_stream = io.BytesIO()
        plt.savefig(image_stream, format='png')
        image_stream.seek(0)
        
        # Encode the image to base64
        base64_image = base64.b64encode(image_stream.read()).decode('utf-8')
        
        # Convert predictions to a JSON-serializable format (list)
        predictions_list = predictions.tolist()
        
        # Close the plot to release resources
        plt.close()
        
        return {"success": True, "prediction": predictions_list, "chart_image": base64_image}
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
        
    

    

