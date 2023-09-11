import pandas as pd

# Specify the path to the JSON file
json_file_path = "data.json"

# Read the JSON data into a pandas DataFrame
df = pd.read_json(json_file_path)

# Specify the Excel file path where you want to save the data
excel_file_path = "data.xlsx"

# Convert the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

print(f"Data from {json_file_path} has been saved to {excel_file_path} in Excel format.")
