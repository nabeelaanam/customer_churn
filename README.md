📊 Customer Churn Prediction Web Application

This project is a Machine Learning–based Customer Churn Prediction system with a Flask web interface.
It predicts whether a customer is likely to churn (leave) or stay, based on customer details.

🚀 Project Features

● Trained Machine Learning model (Scikit-Learn)
● Flask backend for prediction
● User-friendly web interface (Bootstrap)
● Real-time churn prediction
● Modular and beginner-friendly structure

🧠 Machine Learning Details

● Problem Type: Binary Classification
● Target Variable: Churn (0 = Stay, 1 = Churn)
● Algorithm Used: Random Forest Classifier
● Preprocessing: Label Encoding (categorical data)
                 StandardScaler (feature scaling)

🧾 Input Features Used (11 Features)

1.Gender
2.Subscription Type
3.Contract Length
4.Monthly Charges
5.Total Charges
6.Payment Method
7.Tenure
8.Device Protection
9.Online Security
10.Paperless Billing
11.Senior Citizen

🗂️ Project Folder Structure
customer_churn_flask/
│
├── app.py                 # Flask backend
├── model.pkl              # Trained ML model
├── scaler.pkl             # StandardScaler object
├── requirements.txt       # Required Python libraries
├── README.md              # Project documentation
│
└── templates/
    └── index.html         # Frontend UI
