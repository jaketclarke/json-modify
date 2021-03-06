# libraries
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
    if '/' in subdir:
        datalength = len(subdir) - subdir.find('/') - 1
        outpath = subdir[-datalength:]
    else:
        outpath = None
    return outpath

def make_directorytree_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)