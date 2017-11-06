""" data crawlers program use to crawlers dataset from tourism.go.th """
import requests
from bs4 import BeautifulSoup as bs
import pathlib
def find_link_intable(url):
    """ Find link of dataset for download """
    links = []
    web = requests.get(url).text
    soup = bs(web, 'html.parser')
    file_table = soup.find('table', attrs={"class":"table-striped"}) #Find table that contain link of dataset
    for item in file_table.find_all('a'):
        links.append(item['href'])
    return links
def downloads(links, year):
    """ download file from link in links """
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for item in range(len(links)-1):
        url = "http://www.tourism.go.th"+links[item]
        pathlib.Path(year).mkdir(parents=True, exist_ok=True)
        download = requests.get(url).content
        path = year+"/"+months[item]+".xls"
        print(path)
        with open(path, "wb") as datafile:
            datafile.write(download)
    
def main():
    """ main function """
    url = "http://www.tourism.go.th/view/1/สถิตินักท่องเที่ยวชาวต่างชาติที่เดินทางเข้าประเทศไทย%20ปี%202559/TH-TH"
    links = find_link_intable(url)
    downloads(links, "2559")

main()