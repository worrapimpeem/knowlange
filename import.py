import json

# Specify the JSON file name
json_file = "data.json"

try:
    # Open and read the JSON file
    with open(json_file, 'r') as file:
        json_data = file.read()

    # Replace single quotes with double quotes
    cleaned_json = json_data.replace("'", "\"")

    # Load the cleaned JSON into a Python dictionary
    data_dict = json.loads(cleaned_json)

    # Serialize the dictionary back to valid JSON format with proper indentation
    formatted_json = json.dumps(data_dict, indent=2)

    # Print the cleaned and formatted JSON
    print(formatted_json)

except FileNotFoundError:
    print(f"The file '{json_file}' was not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
