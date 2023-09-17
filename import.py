import json

# Original JSON data
data = {
    'name': "'dick'John'put'",
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'New York'
    }
}

# Serialize the data to a properly formatted JSON string
formatted_json = json.dumps(data, indent=4)

# Print the formatted JSON
print(formatted_json)
