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
    bar_chart.title = filename[8].upper() + filename[9:-13]
    bar_chart.x_labels = map(str, lst_year)
    for i in range(len(dataframe)):
        bar_chart.add(country[i], dataframe.ix[i][1:])

    bar_chart.render_to_file("chart/"+filename[7:-5]+".svg")
    if number + 2549 >= 2560:  # ถ้าเกิน 2560 ให้ตัดเหลือ 2559 เพราะมันมีถึงปี 2559
        number -= 1
    return [filename[8:filename.find("_")],dataframe[2549 + number]]

def main():
    """
        main function
    """
    files = [filename for filename in open("dataset/file.txt")]
    list_x = []
    list_get_lst_of_sum = []  #เก็บlistผลรวมจำนวนคนในแต่ละทวีป โดยในlist จะมี list ย่อย 10 list คือ ปี 2550 - 2559 และในแต่ละ list ย่อยมี 7 index คือทวีป
    list_sum = []
    list_of_number_and_lanmass = []
    list_country = ['africa', 'america', 'east asia', 'europe', 'middle east', 'oceania', 'south asia']
    number_to_plotgraph_function_for_add_years = 1  # send to plotgraph function to +1 year
    count = 0 # count if count == 7 it means 7 ทวีป  change year example: year 2554 and count % 7 == 0  >>> year += 1 เริ่มต้นทวีปใหม่
    lst = [] #list for keep sum(i[1]) กคือผลรวมจำนวนคน
    for item in (files * 10):  # * 10 for 10 years
        count += 1
        list_x.append(plotgraph("dataset/" + item.strip("\n"), number_to_plotgraph_function_for_add_years))
        if count % 7 == 0:  # count คือพอเป็น 7 ทวีปละให้มันเปลี่ยนปี (year += 1)
            number_to_plotgraph_function_for_add_years += 1
    for i in list_x:
        lst.append(sum(i[1])) #keep sum of people number
        if len(lst) == 7: #its means เก็บครบ 7 ทวีปเหมือนเดิม append lst to list_get_lst_of_sum
            list_get_lst_of_sum.append(lst)
            lst = []
    for i in range(7): #7 ทวีป
        for j in range(10): # 10 years
            lst.append(list_get_lst_of_sum[j][i]) #เก็บ list ใหญ่ index j  และ list เล็ก index i เพื่อแยกเปนทวีปๆ
        lst.append(list_country[i])
        list_of_number_and_lanmass.append(lst) #add name country
        lst = []
    print(list_of_number_and_lanmass)
main()
