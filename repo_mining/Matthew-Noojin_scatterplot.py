import json
import requests
import csv

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

if not os.path.exists("data"):
 os.makedirs("data")

data = pd.read_csv("data/file_rootbeer.csv")
df = pd.DataFrame(data)

dictfiles = {}
dictauthor = {}

datecreated = '2015-06-14'

for x, name in enumerate(df['Filename']):
    dictfiles[name] = 0

ct = 1
for key in dictfiles:
    dictfiles[key] = ct
    ct = ct + 1
    
for x, name in enumerate(df['Author']):
    dictauthor[name] = 0
    
colors = [
    'red',
    'blue',
    'green',
    'orange',
    'purple',
    'cyan',
    'magenta',
    'yellow',
    'black',
    'teal',
    'coral',
    'turquoise',
    'indigo',
    'gold',
    'pink',
    'lime',
    'silver',
    'violet',
    'brown'
] 
ct = 1
for key in dictauthor:
    dictauthor[key] = ct
    ct = ct + 1

weeks = []
for x, date in enumerate(df['Date']):
    numbers = re.findall(r'\d+', date)
    year = int(numbers[0])
    month = int(numbers[1])
    day = int(numbers[2])
    
    input_days = year * 365 + month * 30 + day
    ref_days = 2015 * 365 + 6 * 30 + 14
    
    diff = input_days - ref_days
    
    week = diff // 7
    
    weeks.append(week)
    
for x, value in enumerate(weeks):
    plt.scatter(dictfiles[df.iat[x,0]],value,color=colors[dictauthor[df.iat[x,1]]])

plt.xlabel('File')
plt.ylabel('Weeks')
plt.show()