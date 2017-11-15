import csv
import os
import sys
from bokeh.charts import Scatter, show
import pandas as pd


pathProg = 'C:\\Users\\209945\\AppData\\Local\\Continuum\\anaconda3'
os.chdir(pathProg)

if os.getcwd() != pathProg:
    print ("EEROR: the file path incorrect.")
    sys.exit()

file = open(pathProg + '\\12V3.csv', 'r')
csvCursor = csv.reader(file)


for row in csvCursor:
    
    speed = row[7]
    dist  = row[8]
    
file.close()


cyl_df = pd.DataFrame({
    "頻率": speed,
     "次數": dist
})
scatter = Scatter(cars_df, x = "頻率", y = "次數")
show(bar)
