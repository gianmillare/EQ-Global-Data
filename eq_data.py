import json

# Explore the file
filename = 'data/eq_1_day.json'



# Part 1: Restructure the Data
# with open(filename) as f:
#     all_eq_data = json.load(f) # changes the format into something Python can read
#
# readable_file = 'data/reformat_1_day.json' # create a new file to put all data in a more readable format
# with open(readable_file, 'w') as f: # the 'w' stands for 'write' which loops to write all data in the new file
#     json.dump(all_eq_data, f, indent=4) # this takes all the data read and dumps it into the new file




#  Part 2: List all the earthquakes
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features'] # This is how we would normally 'call' a specific dictionary
print(len(all_eq_dicts))