import json
import os

def load_json(file):
    # load the json and return a dict
    with open(file) as file:
        return json.load(file)

def dump_json(data, outfilepath):
    with open(outfilepath, 'w') as outfile:
                json.dump(data, outfile)

def strip_parent_directory(subdir):
    # where should we write to?
    # get the full path without the parent folder (so we can output somewhere other than we input)
    # so right of the first slash
    datalength = len(subdir) - subdir.find('/') - 1
    outpath = subdir[-datalength:]
    return outpath

def make_directorytree_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

directoryinput = r'test-data-input'
directoryoutput = r'output'
key = 'foo'
value = 'bar'

for subdir, dirs, files in os.walk(directoryinput):
    for filename in files:
        # where is the file
        filepath = subdir + os.sep + filename
        
        outpath = strip_parent_directory(subdir)
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
            # check output path exists
            make_directorytree_if_not_exists(outfolderpath)
            # make file
            dump_json(data, outfilepath)