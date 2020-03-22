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



# #  Part 2: List all the earthquakes
# with open(filename) as f:
#     all_eq_data = json.load(f)
#
# all_eq_dicts = all_eq_data['features'] # This is how we would normally 'call' a specific dictionary
# print(len(all_eq_dicts))



# # Part 3: Extracting Magnitudes
# with open(filename) as f:
#     all_eq_data = json.load(f)
#
# all_eq_dicts = all_eq_data['features']
#
# mags = [] # Create an open list to store the information
# for eq_dict in  all_eq_dicts: # loop through the all dictionaries under 'features'
#     mag = eq_dict['properties']['mag'] # store all mag data into a variable
#     mags.append(mag) # append the mag data into the empty list
# print(mags[:10])



# Part 4: Extracting the locations
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
