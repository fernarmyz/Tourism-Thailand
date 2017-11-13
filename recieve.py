import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pygal

# dataframe = pd.read_excel("dataset/receive.xlsx")
# lst_year = dataframe.ix[0].index.values[1:].tolist()
# bar_chart = pygal.Bar(title=u'รายได้ของประเทศไทยที่ได้รับจากธุรกิจการท่องเที่ยวในปี พ.ศ. 2550 – 2559', y_title='รายได้(ล้านบาท)', x_title='ปีพ.ศ.')
# bar_chart.x_labels = map(str, lst_year)
# country = dataframe['Country']

# for i in range(len(dataframe)):
#     bar_chart.add(country[i], dataframe.ix[i][1:])
# bar_chart.render_to_file("chart/"+"money_recieve"+".svg")

dataframe = pd.read_excel("dataset/receive.xlsx")
print(dataframe[dataframe.columns[0]])