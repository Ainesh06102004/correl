import plotly.express as px
import csv
import numpy as np

tvsize = []
tvtime = []

with open("coffee.csv", newline='') as file:
    filedata = csv.DictReader(file)
    list1 = list(filedata)
    
    for row in list1:
        tvsize.append(float(row["Coffee in ml"]))
        tvtime.append(float(row["sleep in hours"]))
    

#scattergraph = px.scatter(list1, x = 'Size of TV', y = '\tAverage time spent watching TV in a week (hours)')
#scattergraph.show()

correl = np.corrcoef(tvsize,tvtime)
print(correl)