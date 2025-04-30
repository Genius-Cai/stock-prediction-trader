from flask import Flask, request, jsonify
from data.data_loader import DataLoader
from data.preprocess import preprocess_data
from models.train import train_model
from predictions.predict import make_prediction

app = Flask(__name__)

@app.route('/load_data', methods=['GET'])
def load_data():
    data_loader = DataLoader()
    data_loader.load_data()
    return jsonify({"message": "Data loaded successfully."})

@app.route('/train_model', methods=['POST'])
def train():
    raw_data = request.json.get('data')
    processed_data = preprocess_data(raw_data)
    train_model(processed_data)
    return jsonify({"message": "Model trained successfully."})

@app.route('/predict', methods=['POST'])
def predict():
    new_data = request.json.get('data')
    prediction = make_prediction(new_data)
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True)