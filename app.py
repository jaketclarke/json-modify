# libraries
import json
import os
import argparse
import sys
from functions import *

# set up console interface
parser = argparse.ArgumentParser(description='A simple console app to add a key/value pair to every JSON file in a directory tree')
required = parser.add_argument_group('required arguments')
parser.add_argument('--input-dir', default='test-data-input', dest='inputdir', type=str, help='Directory to read JSON files from')
parser.add_argument('--output-dir', default='output', dest='outputdir', type=str, help='Directory to save JSON files to')
required.add_argument('--key', dest='key', type=str, help='Key to add to the JSON')
required.add_argument('--value', dest='value', type=str, help='Value to add to the JSON')

args = parser.parse_args()

# fail if mandatory pars misssing
if not args.key:
    print("\r\n")
    print("Please specify the key you wish to add to the JSON")
    parser.print_help()
    sys.exit(2)

if not args.value:
    print("Please specify the value you wish to add to the JSON")
    parser.print_help()
    sys.exit(2)

# set values
directoryinput = args.inputdir
directoryoutput = args.outputdir
key = args.key
value = args.value

for subdir, dirs, files in os.walk(directoryinput):
    for filename in files:
        # input file
        filepath = subdir + os.sep + filename
        
        # output details
        outpath = strip_parent_directory(subdir)
        if outpath:
            outfolderpath = directoryoutput + os.sep + outpath
        else:
            outfolderpath = directoryoutput
        outfilepath = outfolderpath + os.sep + filename

        if filepath.endswith(".json"):
            # read data
            data = load_json(filepath)
            # append new key
            data[key] = value
            # check output path exists
            make_directorytree_if_not_exists(outfolderpath)
            # make file
            dump_json(data, outfilepath)