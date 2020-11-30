import json
import os

def load_json(file):
    with open(file) as file:
        return json.load(file)

directory = r'test-data-input'

for subdir, dirs, files in os.walk(directory):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".json"):
            # print (filepath)
            data = load_json(filepath)
            print(data)