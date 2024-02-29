import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import BayesianRidge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import joblib

# Load the dataset
df = pd.read_csv('weather1.csv')

# Select only the relevant columns for prediction
selected_columns = ['TMIN', 'TMAX', 'TAVG']

# Fill missing values with dummy data (mean value for simplicity)
df[selected_columns] = df[selected_columns].fillna(df[selected_columns].mean())

# Drop rows with missing values
df = df.dropna(subset=selected_columns)

# Check if there are enough samples for modeling
if len(df) >= 2:
    # Select features and target variable
    X = df[['TMIN', 'TMAX']]
    y = df['TAVG']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train the Bayesian Ridge Regression model
    bayesian_ridge_model = BayesianRidge()
    bayesian_ridge_model.fit(X_train_scaled, y_train)

    # Save the trained model using joblib
    model_file_path = r'C:\Users\Bhumika Shankar\OneDrive\Desktop\Web Project\Machine_Learning_Model\bayesian_ridge_model.joblib'
    joblib.dump(bayesian_ridge_model, model_file_path)

    # Make predictions for tomorrow's temperature using the test set
    predicted_temperature = bayesian_ridge_model.predict(X_test_scaled)

    # Display the predicted temperature for tomorrow
    print(f'Predicted Temperature for Tomorrow: {predicted_temperature[0]}')

    # Evaluate the model
    mse = mean_squared_error(y_test, predicted_temperature)
    print(f'Mean Squared Error: {mse}')

else:
    print("Not enough samples in the dataset.")
