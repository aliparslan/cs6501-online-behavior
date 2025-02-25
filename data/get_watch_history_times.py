import json

# Load the JSON data from a file
with open('data.json', 'r') as infile:
    data = json.load(infile)

# Create a new list with only the "time" field from each item
times_only = [{'time': item['time']} for item in data if 'time' in item]

# Optionally, write the result to a new JSON file
with open('output.json', 'w') as outfile:
    json.dump(times_only, outfile, indent=4)

# If you simply want to print the result:
print(json.dumps(times_only, indent=4))
