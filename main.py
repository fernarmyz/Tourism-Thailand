"""
    Plot graph from dataset
"""
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pygal

def plotgraph(filename):
    """
        plot graph
    """
    dataframe = pd.read_excel(filename)
    lst_year = dataframe.ix[0].index.values[1:].tolist()
    country = dataframe['Country']


    bar_chart = pygal.Line()
    bar_chart.title = filename[8].upper() + filename[9:-13]
    bar_chart.x_labels = map(str, lst_year)

    for i in range(len(dataframe)):
        bar_chart.add(country[i], dataframe.ix[i][1:])

    bar_chart.render_to_file("chart/"+filename[7:-5]+".svg")
    return [filename[8:filename.find("_")],dataframe[2550]]

def main():
    """
        main function
    """
    files = [filename for filename in open("dataset/file.txt")]
    list_x = []
    for item in files:
        list_x.append(plotgraph("dataset/" + item.strip("\n")))
    for i in list_x:
         print(sum(i[1]))
main()
