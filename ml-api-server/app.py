from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load("best_model.pkl")

@app.route('/')
def home():
    return "✅ ML Model API is live!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)

        # Debugging logs (important!)
        print("📥 Input Features:", features)

        # Get prediction
        prediction = int(model.predict(features)[0])

        # More debug
        print("🤖 Prediction:", prediction)

        return jsonify({'prediction': prediction})

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({'error': str(e)}), 500
