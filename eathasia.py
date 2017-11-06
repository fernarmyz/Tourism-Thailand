<<<<<<< HEAD
<<<<<<< HEAD
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
from matplotlib import style
import pygal

style.use('fivethirtyeight')
file_loc = "1122.xlsx"
df = pd.read_excel(file_loc, sheetname='Sheet2')
list_1 = df.ix[0][1:]
list_2 = df.ix[1][1:]
list_3 = df.ix[2][1:]
list_4 = df.ix[3][1:]
list_5 = df.ix[4][1:]
list_6 = df.ix[5][1:]
list_7 = df.ix[6][1:]
list_8 = df.ix[7][1:]
list_9 = df.ix[8][1:]
list_10 = df.ix[9][1:]
list_11 = df.ix[10][1:]
list_12 = df.ix[11][1:]
list_13 = df.ix[12][1:]
list_14 = df.ix[13][1:]
list_15 = df.ix[14][1:]
lst_year = [2550, 2551, 2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559]

bar_chart = pygal.Line()
bar_chart.title = 'South Asia'
bar_chart.x_labels = map(str, lst_year)
bar_chart.add('Negara Brunei Darussalam', list_1)
bar_chart.add('Cambodia', list_2)
bar_chart.add('Indonesia', list_3)
bar_chart.add('Lao', list_4)
bar_chart.add('Malaysia', list_5)
bar_chart.add('Myanmar', list_6)
bar_chart.add('Philippines', list_7)
bar_chart.add('Singapore', list_8)
bar_chart.add('Vietnam', list_9)
bar_chart.add('Chinese', list_10)
bar_chart.add('Hong Kong', list_11)
bar_chart.add('Japan', list_12)
bar_chart.add('Korea', list_13)
bar_chart.add('Taiwan', list_14)
bar_chart.add('Other Country', list_15)
bar_chart.render_to_file('bar_chart.svg')
