import json

# Load the JSON data from a file
with open("data.json", "r") as json_file:
    data = json.load(json_file)

# Define the criteria for deletion (e.g., "Age" equals 30)
criteria = "Age"
value_to_delete = 30

# Iterate through the JSON array and remove matching objects
data = [item for item in data if item.get(criteria) != value_to_delete]

# Save the modified data back to the JSON file
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
