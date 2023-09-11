import json

# Define the input and output file names
input_file_name = 'k.json'
output_file_name = 'output.json'

# Read data from the input JSON file
with open(input_file_name, 'r') as input_file:
    input_data = json.load(input_file)

# Flatten the JSON structure
output_data = {
    "name": input_data["name"],
    "age": input_data["age"],
    "street": input_data["address"]["street"],
    "city": input_data["address"]["city"],
    "state": input_data["address"]["state"]
}

# Write the flattened data to the output JSON file
with open(output_file_name, 'w') as output_file:
    json.dump(output_data, output_file, indent=4)

print(f'Flattened data saved to "{output_file_name}"')
