from flask import Flask, render_template, request
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all 11 values from form
        features = [
            int(request.form['gender']),
            int(request.form['subscription_type']),
            int(request.form['contract_length']),
            float(request.form['monthly_charges']),
            float(request.form['total_charges']),
            int(request.form['payment_delay']),
            int(request.form['tenure']),
            int(request.form['device_protection']),
            int(request.form['online_security']),
            int(request.form['paperless_billing']),
            int(request.form['senior_citizen'])
        ]

        # Format and scale
        features = np.array([features])
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]

        result = "Customer is likely to CHURN." if prediction == 1 else "Customer is likely to STAY."
        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)




