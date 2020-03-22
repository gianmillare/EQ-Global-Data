# Now using a larger data set

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_global_30_days.json'

# Part 7: Customizing marker size
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dicts in all_eq_dicts:
    mag = eq_dicts['properties']['mag']
    lon = eq_dicts['geometry']['coordinates'][0]
    lat = eq_dicts['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="plots/global_earthquakes_v2.html")

