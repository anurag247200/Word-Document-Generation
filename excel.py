import pandas as pd

# Function to validate data
def validate_data(df):
    # Check for missing values
    missing_values = df.isnull().sum()
    print("Missing Values per Column:\n", missing_values)
    
    # Validate specific data columns based on expected data types
    for column in df.columns:
        if df[column].dtype == 'object':
            # If a string column, ensure no numeric values in it
            if df[column].str.isnumeric().any():
                print(f"Warning: Numeric values found in string column '{column}'")
        elif df[column].dtype in ['int64', 'float64']:
            # Check if numeric columns have non-numeric or NaN values
            if df[column].isnull().any():
                print(f"Warning: Missing or invalid numeric values in column '{column}'")

# Function to read Excel data
def read_excel(file_path, sheet_name=0):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print("Data successfully read from Excel.")
        
        # Handle missing values by filling with a placeholder (e.g., "N/A" for strings, 0 for numbers)
        df = df.fillna({
            col: 'N/A' if df[col].dtype == 'object' else 0 for col in df.columns
        })
        
        # Perform data validation
        validate_data(df)

        return df
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = r"D:\Visual Studio Code\C++\sample_excel_data.xlsx"  # New full file path
df = read_excel(file_path)

if df is not None:
    print(df.head())  # Print the first few rows of the data
else:
    print("Failed to load the data.")
