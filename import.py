import json

# Specify the input JSON file name
input_json_file = "input_data.json"

try:
    # Open and read the input JSON file
    with open(input_json_file, 'r') as file:
        json_data = file.read()

    # Replace single quotes with double quotes
    cleaned_json = json_data.replace("'", "\"")

    # Load the cleaned JSON into a Python dictionary
    data_dict = json.loads(cleaned_json)

    # Serialize the dictionary back to valid JSON format with proper indentation
    formatted_json = json.dumps(data_dict, indent=2)

    # Specify the output JSON file name
    output_json_file = "formatted_data.json"

    # Save the formatted JSON data to a new JSON file
    with open(output_json_file, 'w') as outfile:
        outfile.write(formatted_json)

    print(f"Formatted JSON data saved to {output_json_file}")

except FileNotFoundError:
    print(f"The file '{input_json_file}' was not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
