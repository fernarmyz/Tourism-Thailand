import pandas as pd

def main():
    dfs = pd.read_csv('country_new.csv', encoding='utf-8')
    del dfs['Unnamed: 0']
    print(dfs['ประเทศ']['2550'])
main()
