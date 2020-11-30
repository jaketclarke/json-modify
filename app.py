import json

with open('test-data-input/dir-one/one.json') as file:
    data = json.load(file)

print(data)