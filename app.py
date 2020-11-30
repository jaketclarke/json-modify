import json
import os

# with open('test-data-input/dir-one/one.json') as file:
#     data = json.load(file)

# print(data)

directory = r'test-data-input'

for subdir, dirs, files in os.walk(directory):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".json"):
            print (filepath)