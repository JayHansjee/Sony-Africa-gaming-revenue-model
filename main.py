from sensitivity import tornado_series
from model import total_revenue
import pandas as pd
from plot import tornado_plot

if __name__ == '__main__':
    df_ass = pd.read_csv('data/assumptions.csv')
    df_ass = df_ass.set_index('id')

    countries = ['sa','eg','ng']
    assumptions = df_ass.index

    torn = tornado_series(df_ass, countries, assumptions)
    torn['perc_swing'] = 100*torn['swing']/torn['swing'].sum()

    base_case = total_revenue(df_ass['base'],countries)
    print(base_case)

    tornado_plot(torn, base_case)
