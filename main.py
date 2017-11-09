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


def plotgraph(filename, number):
    """
        plot graph
    """
    dataframe = csv_to_dataframe(filename)
    lst_year = dataframe.ix[0].index.values[1:].tolist()
    country = dataframe['Country']

    bar_chart = pygal.Line()
    bar_chart.title = filename[8:-13].title()
    bar_chart.x_labels = map(str, lst_year)
    for i in range(len(dataframe)):
        bar_chart.add(country[i], dataframe.ix[i][1:])

    bar_chart.render_to_file("chart"+filename[7:-5]+".svg")
    return [filename[8:filename.find("_")],dataframe[number]]

def plot_sum_continent(dataframe):
    """ Plot graph of sum continent """
    continents = dataframe.index.tolist()
    bar_chart = pygal.Line()
    bar_chart.title = "Peple for each continent"
    bar_chart.x_labels = map(str, dataframe.columns.tolist())
    for continent in continents:
        bar_chart.add(continent, dataframe.loc[continent].tolist())
    bar_chart.render_to_file("chart/person_continents.svg")

def main():
    """
        main function
    """
    files = [filename.strip("\n\r") for filename in open("dataset/file.txt")]

    list_continent = ['africa', 'america', 'east asia', 'europe', 'middle east', 'oceania', 'south asia']
    start_year, end_year = 2550, 2560

    sum_data = {start_year+i: [] for i in range(end_year - start_year)} #list for keep sum(i[1]) กคือผลรวมจำนวนคน
    data_keep = {}
    for year in sum_data.keys():
        for continent in range(len(files)):
            data_keep[list_continent[continent]] = plotgraph("dataset/"+files[continent],year)
            data = pd.DataFrame(data_keep)
            sum_data[year].append(data[list_continent[continent]][1].sum())
    sum_data = pd.DataFrame(sum_data, index=list_continent) #sum_data is sum of people from each continent in each year
    plot_sum_continent(sum_data)#sent dataframe to plot graph
    sum_data.loc['sum_values'] = pd.Series(sum_data.loc['africa':'south asia'].sum(), index=sum_data.columns.tolist())
    print(sum_data)
main()
