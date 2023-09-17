import json

# Sample output data (Python dictionary)
output_data = {
    "name": "Alice",
    "age": 25,
    "city": "San Francisco"
}

# Specify the file path where you want to save the JSON data
file_path = "output.json"

# Write the output data to the JSON file
try:
    with open(file_path, "w") as file:
        json.dump(output_data, file, indent=4)
    print(f"Data has been written to '{file_path}' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
