import json
import os

def load_json(file):
    with open(file) as file:
        return json.load(file)
    

directoryinput = r'test-data-input'
directoryoutput = r'output'
key = 'foo'
value = 'bar'

for subdir, dirs, files in os.walk(directoryinput):
    for filename in files:
        # where is the file
        filepath = subdir + os.sep + filename
        
        # where should we write to?
        # get the full path without the parent folder (so we can output somewhere other than we input)
        # so right of the first slash
        datalength = len(subdir) - subdir.find('/') - 1
        outpath = subdir[-datalength:]
        # combine with output dir and os separator
        outfolderpath = directoryoutput + os.sep + outpath
        outfilepath = outfolderpath + os.sep + filename
        
        # print(filepath)
        print(filepath)
        print(outfolderpath)
        print(outfilepath)
        # 

        if filepath.endswith(".json"):
            # read data
            data = load_json(filepath)
            # append new key
            data[key] = value
            # print(data)
            # write to output
            
            # # ensure folder exists
            # if not os.path.exists('my_folder'):
            #     os.makedirs('my_folder')
            
            # with open(outfilepath, 'w') as outfile:
            #     json.dump(data, outfile)