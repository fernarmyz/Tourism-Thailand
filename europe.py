import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pygal


file_loc = "dataset/europe_cleaned.xlsx"
df = pd.read_excel(file_loc, sheetname="Sheet3")
lst_year = df.ix[0].index.values[1:].tolist()
country = df['Country']

bar_chart = pygal.Line()
bar_chart.title = 'Europe'
bar_chart.x_labels = map(str, lst_year)

for i in range(len(df)):
    bar_chart.add(country[i], df.ix[i][1:])

bar_chart.render_to_file("chart/"+file_loc[7:]+".svg")
