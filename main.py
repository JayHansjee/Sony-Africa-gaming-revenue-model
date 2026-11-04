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

    base_case = round(total_revenue(df_ass['base'],countries), 2)
    low_case = round(total_revenue(df_ass['low'],countries), 2)
    high_case = round(total_revenue(df_ass['high'],countries), 2)

    print(f"The base case estimate is ${base_case}mn. The high case is ${high_case}mn, and the low is ${low_case}".format())

    tornado_plot(torn, base_case)
