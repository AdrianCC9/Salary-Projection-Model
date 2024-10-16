# data_preprocessing.py

import pandas as pd

def preprocess_data(file_path):
    """
    Preprocess the data: load the CSV and return the cleaned DataFrame.
    """
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Print column names to debug
    print("Columns in the dataset:", data.columns)
    
    # Check for any missing values
    if data.isnull().sum().any():
        print("Missing values detected. Handling missing values.")
        data = data.dropna()  # This is a simple approach; you can use others like imputation if needed
    
    # Use the correct column names
    X = data[['Years of Experience']]  # Independent variable
    y = data['Salary']  # Dependent variable
    
    return X, y

if __name__ == "__main__":
    file_path = '/Users/adrian/Salary-Projection-Model/data/Salary Data.csv'  # Ensure this is the correct path to your file
    X, y = preprocess_data(file_path)
    print("Data preprocessing completed.")
