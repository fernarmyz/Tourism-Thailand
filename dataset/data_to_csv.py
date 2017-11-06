import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl


style.use('fivethirtyeight')

def main():
    dfs = pd.read_csv('country_new.csv', encoding='utf-8', index_col = 2)
    mpl.font_manager.FontProperties(family='JasmineUPC',size=20)
    dfs['2550'].str.replace(",", "").fillna(0).astype(float).plot()
    plt.show()
main()
