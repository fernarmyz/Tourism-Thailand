"""
    Plot graph from dataset
"""
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pygal

def plotgraph(filename, number):
    """
        plot graph
    """
    dataframe = pd.read_excel(filename)
    lst_year = dataframe.ix[0].index.values[1:].tolist()
    country = dataframe['Country']

    bar_chart = pygal.Line()
    bar_chart.title = filename[8:-13].title()
    bar_chart.x_labels = map(str, lst_year)
    for i in range(len(dataframe)):
        bar_chart.add(country[i], dataframe.ix[i][1:])

    bar_chart.render_to_file("chart/"+filename[7:-5]+".svg")
    return [filename[8:filename.find("_")],dataframe[number]]

def main():
    """
        main function
    """
    files = [filename.strip("\n") for filename in open("dataset/file.txt")]
    list_x = []
    list_get_lst_of_sum = []  #เก็บlistผลรวมจำนวนคนในแต่ละทวีป โดยในlist จะมี list ย่อย 10 list คือ ปี 2550 - 2559 และในแต่ละ list ย่อยมี 7 index คือทวีป
    list_sum = []
    list_of_number_and_lanmass = []
    list_country = ['africa', 'america', 'east asia', 'europe', 'middle east', 'oceania', 'south asia']
    number_to_plotgraph_function_for_add_years = 1  # send to plotgraph function to +1 year
    count = 0 # count if count == 7 it means 7 ทวีป  change year example: year 2554 and count % 7 == 0  >>> year += 1 เริ่มต้นทวีปใหม่
    lst = {2550:[], 2551:[], 2552:[], 2553:[], 2554:[], 2555:[], 2556:[], 2557:[], 2558:[], 2559:[]} #list for keep sum(i[1]) กคือผลรวมจำนวนคน
    data_keep = {}
    for year in lst.keys():
        for i in range(len(files)):
            data_keep[list_country[i]] = plotgraph("dataset/"+files[i],year)
            test_df = pd.DataFrame(data_keep)
            lst[year].append(test_df[list_country[i]][1].sum())
    print(lst)
main()
