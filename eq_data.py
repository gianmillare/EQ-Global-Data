import json

# Explore the file
filename = 'data/eq_1_day.json'

with open(filename) as f:
    all_eq_data = json.load(f) # changes the format into something Python can read

readable_file = 'data/reformat_1_day.json' # create a new file to put all data in a more readable format
with open(readable_file, 'w') as f: # the 'w' stands for 'write' which loops to write all data in the new file
    json.dump(all_eq_data, f, indent=4) # this takes all the data read and dumps it into the new file

    