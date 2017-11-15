"""
    Plot graph from dataset
"""
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pygal

def csv_to_dataframe(filename):
    """ CSV TO DATAFRAME """
    dataframe = pd.read_excel(filename)
    return dataframe


def plotgraph(data, name, chart_title, graph_type):
    """
        plot graph
    """
    y_axis_title='จำนวนนักท่องเที่ยว(คน)'
    x_axis_title='ปีพ.ศ.'
    dataframe = data
    year_list = dataframe.loc[0].index.values[1:].tolist()
    country = dataframe[dataframe.columns[0]]

    if graph_type == "line":
        chart = pygal.Line(x_title=x_axis_title, y_title=y_axis_title)
    elif graph_type == "bar":
        chart = pygal.Bar()
    elif graph_type == "pie":
        chart == pygal.Pie()

    chart.title = chart_title

    chart.x_labels = map(str, year_list)
    for i in range(len(dataframe)):
        chart.add(str(country[i]).strip() , dataframe.loc[i][1:].astype(float))

    chart.render_to_file("chart/"+name+".svg")

def main():
    """
        main function
    """

    """ Plotgraph of continents """
    files = ["dataset/continents/"+filename.strip("\n\r") for filename in open("dataset/continents/file.txt")]
    list_continent = ['africa', 'america', 'east asia', 'europe', 'middle east', 'oceania', 'south asia']
    start_year, end_year = 2550, 2560
    list_year = [i for i in range(start_year, end_year)]
    continent_values = {}
    for continent in range(len(files)):
        dataframe = csv_to_dataframe(files[continent])
        name = list_continent[continent]
        title = 'Statistics from '+ list_continent[continent]+ " to Thailand in 2550 - 2559."
        continent_values[list_continent[continent]] = dataframe.sum().tolist()[1:]
        plotgraph(dataframe,name,title, "line")

    """ Plotgraph of tourist each continents per year"""
    data = pd.DataFrame(continent_values, index = list_year)
    tourist_each_continent = data.transpose().reset_index()
    plotgraph(tourist_each_continent,"tourist_each_continent", "สถิตินักท่องเที่ยวแต่ละทวีปที่เดินทางเข้าประเทศไทยในปี พ.ศ. 2550 – 2559", "line")

    """ Plotgraph of all tourist per years """
    tourist_per_year = data.transpose().sum().reset_index().set_index('index').transpose()
    tourist_per_year.index = ['จำนวนนักท่องเที่ยว']
    tourist_per_year = tourist_per_year.reset_index()
    plotgraph(tourist_per_year,"tourist_per_year", "สถิตินักท่องเที่ยวชาวต่างชาติที่เดินทางเข้าประเทศไทยในปี พ.ศ. 2550 – 2559", "line")

    """ Plotgraph tourist info """
    files = [filename.strip("\n\r") for filename in open("dataset/tourist_info/file.txt")]
    for file_info in files:
        dataframe = csv_to_dataframe("dataset/tourist_info/"+file_info)
        name = file_info[:file_info.find(".")]
        title = 'Statistics about '+ name + " to Thailand in 2550 - 2559."
        plotgraph(dataframe,name,title, "bar")
        # print(dataframe[dataframe.columns[0]])
main()

