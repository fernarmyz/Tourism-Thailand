""" data crawlers program use to crawlers dataset from tourism.go.th """
import requests

def main():
    """ main function """
    req = requests.get("http://www.tourism.go.th/view/1/สถิตินักท่องเที่ยวชาวต่างชาติที่เดินทางเข้าประเทศไทย%20ปี%202559/TH-TH")
    print(req.status_code)
main()
