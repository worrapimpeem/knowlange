import pandas as pd

# Replace 'your_excel_file.xlsx' with the actual path to your Excel file
excel_file = 'your_excel_file.xlsx'

# Load Excel data into a pandas DataFrame
df = pd.read_excel(excel_file, engine='openpyxl')

# Convert DataFrame to JSON
json_data = df.to_json(orient='records')

# Specify the output JSON file name
json_file_name = 'output.json'

# Save the JSON data to a file
with open(json_file_name, 'w') as json_file:
    json_file.write(json_data)

print(f"Data has been saved to {json_file_name}")
