""" data crawlers program use to crawlers dataset from tourism.go.th """
import requests
from bs4 import BeautifulSoup as bs
def main():
    """ main function """
    web = requests.get("http://www.tourism.go.th/view/1/สถิตินักท่องเที่ยวชาวต่างชาติที่เดินทางเข้าประเทศไทย%20ปี%202559/TH-TH").text
    soup = bs(web, 'html.parser')
    print(soup)
main()
