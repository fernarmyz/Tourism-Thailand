"""
    Plot graph from dataset
"""
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pygal

#use data by file to plot graph by using data of landmass.
#this is a data of number people who tourism in thailand Classified by country.
#get Number of people to plot graph.
def plotgraph(filename):
    """plot graph"""
    dataframe = pd.read_excel(filename)
    lst_year = dataframe.ix[0].index.values[1:].tolist()
    country = dataframe['Country']

    print(dataframe[2550])
    bar_chart = pygal.Line()
    bar_chart.title = filename[8].upper() + filename[9:-13]
    bar_chart.x_labels = map(str, lst_year)

    for i in range(len(dataframe)):
        bar_chart.add(country[i], dataframe.ix[i][1:])

    bar_chart.render_to_file("chart/"+filename[7:-5]+".svg")

def main():
    """main function"""
    files = [filename for filename in open("dataset/file.txt")]
    for item in files:
        plotgraph("dataset/" + item.strip("\n"))

main()
