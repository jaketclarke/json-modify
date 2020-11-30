import json
import os

# with open('test-data-input/dir-one/one.json') as file:
#     data = json.load(file)

# print(data)

directory = r'test-data-input'
for entry in os.scandir(directory):
    print(entry.name)