import pandas as pd
from model import total_revenue

def tornado_series(df_ass, countries, ass_list):
    base = df_ass['base']
    base_total = total_revenue(base, countries)
    torn_rows = []
    for ass in ass_list:
        out = {}
        for case in ['high', 'low']:
            p = base.copy()
            p[ass] = df_ass.loc[ass, case]
            out[case] = total_revenue(p, countries) - base_total
        torn_rows.append({'assumption':ass, 'high':out['high'], 'low':out['low']})
    df = pd.DataFrame(torn_rows)
    df['swing'] = (df['high']-df['low']).abs()
    return df.sort_values('swing', ascending=False)
