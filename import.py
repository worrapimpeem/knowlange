import pandas as pd

# Replace 'your_excel_file.xlsx' with the actual path to your Excel file
excel_file = 'your_excel_file.xlsx'

# Load Excel data into a pandas DataFrame
df = pd.read_excel(excel_file, engine='openpyxl')

# Convert DataFrame to JSON
json_data = df.to_json(orient='records')

# Print or save the JSON data
print(json_data)

# If you want to save the JSON data to a file, you can do this:
# with open('output.json', 'w') as json_file:
#     json_file.write(json_data)
