from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is your Flask app!'
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for all routes


@app.route('/get_predicted_temperature', methods=['GET'])
def get_predicted_temperature():
    # Load the trained model
    model = load_your_trained_model()

    # Connect to the database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='2003',
        database='weather'
    )

    # Prepare a query to get the latest weather data
    query = "SELECT TMIN, TMAX FROM weather_data ORDER BY DATE DESC LIMIT 1"
    df = pd.read_sql_query(query, connection)

    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[['TMIN', 'TMAX']])

    # Make predictions
    predicted_temperature = model.predict(X_scaled)

    # Close the database connection
    connection.close()

    # Return the predicted temperature as JSON
    return jsonify({'predicted_temperature': predicted_temperature[0]})

def load_your_trained_model():
    # Load and return your trained model from a separate file
    model = joblib.load("C:/Users/Bhumika Shankar/OneDrive/Desktop/Web Project/Machine_Learning_Model/bayesian_ridge_model.joblib")
    return model

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

