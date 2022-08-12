import csv 
import plotly.express as px

data = []

with open('final.csv') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
data_rows = data[1:]

star_masses = []
star_radiuses = []
star_gravities = []
star_names = []
for star_data in data_rows:
    try:
        star_masses.append(float(star_data[2]))
    except: pass
    try:
        star_radiuses.append(float(star_data[3]))
    except: pass
    try:
        star_gravities.append(float(star_data[8]))
    except: pass
    star_names.append(star_data[0])

fig = px.scatter(x=star_radiuses, y=star_masses, size=star_gravities, hover_data=[star_names])
fig.show()