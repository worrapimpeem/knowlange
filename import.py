import json

# Define the input and output file names
input_file_name = 'input.json'
output_file_name = 'output.json'

# Read data from the input JSON file
with open(input_file_name, 'r') as input_file:
    input_data = json.load(input_file)

# Process the data and create the desired output structure
output_data = []
for item in input_data:
    flat_item = {
        "name": item["name"],
        "substreet": item["person"]["street"]["substreet"],
        "city": item["person"]["street"]["city"]
    }
    output_data.append(flat_item)

# Write the processed data to the output JSON file
with open(output_file_name, 'w') as output_file:
    json.dump(output_data, output_file, indent=4)

print(f'Processed data saved to "{output_file_name}"')
