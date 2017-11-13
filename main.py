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


def plotgraph(data, year, chart_title, x_axis_title, y_axis_title):
    """
        plot graph
    """
    dataframe = csv_to_dataframe(data)
    year_list = dataframe.loc[0].index.values[1:].tolist()
    country = dataframe[dataframe.columns[0]]

    bar_chart = pygal.Line(title=chart_title, x_title=x_axis_title, y_title=y_axis_title)
    # bar_chart = pygal.Line(title=u'Statistics from '+ data[8:-13] + " to Thailand in 2550 - 2559.", y_title='จำนวนนักท่องเที่ยว(คน)', x_title='ปีพ.ศ.')
    bar_chart.x_labels = map(str, year_list)
    for i in range(len(dataframe)):
        bar_chart.add(str(country[i]).strip() , dataframe.loc[i][1:])

    bar_chart.render_to_file("chart"+data[7:-5]+".svg")
    return [data[8:data.find("_")],dataframe[year]]

def plot_sum_continent(dataframe):
    """ Plot graph of sum continent """
    continents = dataframe.index.tolist()
    bar_chart = pygal.Bar(title=u'สถิตินักท่องเที่ยวชาวต่างชาติทุกทวีปที่เดินทางเข้าประเทศไทยในปี พ.ศ. 2550 – 2559', y_title='จำนวนนักท่องเที่ยว(คน)', x_title='ปีพ.ศ.')
    bar_chart.x_labels = map(str, dataframe.columns.tolist())
    for continent in continents:
        bar_chart.add(continent, dataframe.loc[continent].tolist())
    bar_chart.render_to_file("chart/person_continents.svg")


def main():
    """
        main function
    """
    files = ["dataset/"+filename.strip("\n\r") for filename in open("dataset/file.txt")]

    list_continent = ['africa', 'america', 'east asia', 'europe', 'middle east', 'oceania', 'south asia']
    start_year, end_year = 2550, 2560

    sum_data = {start_year+i: [] for i in range(end_year - start_year)} #list for keep sum(i[1]) กคือผลรวมจำนวนคน
    data_keep = {}
    for year in sum_data.keys():
        for continent in range(len(files)):

            dataframe = csv_to_dataframe(files[continent])
            title = 'Statistics from '+ list_continent[continent]+ " to Thailand in 2550 - 2559."
            y_title='จำนวนนักท่องเที่ยว(คน)'
            x_title='ปีพ.ศ.'
            
            data_keep[list_continent[continent]] = plotgraph(files[continent],year, title, x_title, y_title)
            data = pd.DataFrame(data_keep)
            sum_data[year].append(data[list_continent[continent]][1].sum())
    sum_data = pd.DataFrame(sum_data, index=list_continent) #sum_data is sum of people from each continent in each year
    plot_sum_continent(sum_data)#sent dataframe to plot graph
    sum_data.loc['sum_values'] = pd.Series(sum_data.loc['africa':'south asia'].sum(), index=sum_data.columns.tolist())
    bar_chart = pygal.Line(title=u'สถิตินักท่องเที่ยวชาวต่างชาติที่เดินทางเข้าประเทศไทยในปี พ.ศ. 2550 – 2559', y_title='จำนวนนักท่องเที่ยว(คน)', x_title='ปีพ.ศ.')
    bar_chart.add("the tourist", sum_data.loc['sum_values'])
    lst_year = [i for i in sum_data.keys()]
    bar_chart.x_labels = map(str, lst_year)
    bar_chart.render_to_file("Person_of_year"+".svg")
main()

def test():
    files = ["dataset/"+filename.strip("\n\r") for filename in open("dataset/file.txt")]
    df = csv_to_dataframe(files[0])
    print(df[2550])
# test()
