import pandas as pd



###Testing
#print(hardware_revenue(df_ass['low'],'sa'))
#print(total_revenue(df_ass['low'],['sa','ng','eg']))
###

def hardware_revenue(param_series, country_code):
    return param_series[f'hw_{country_code}'] * param_series[f'ps_share_{country_code}']

def hardware_total_revenue(param_series, countries):
    return sum(hardware_revenue(param_series, cc) for cc in countries)

def content_revenue(param_series, country_code):
    return param_series[f'content_{country_code}'] * param_series[f'ps_share_{country_code}'] * param_series['capture_rate']

def content_total_revenue(param_series, countries):
    return sum(content_revenue(param_series, cc) for cc in countries)

def roa_calc(p) -> int:
    total_inflow = (p['roa_declared_imports'] + p['roa_tunisia_allowance']) * p['roa_customs_to_retail'] * p['roa_grey_uplift'] + p['roa_nonreporting_allowance']
    hardware_revenue = total_inflow * p['roa_new_console_share'] * p['ps_share_roa']
    content_spend = min(total_inflow * p['roa_content_ratio'], p['roa_content_ceiling'])
    content_revenue = content_spend * p['ps_share_roa'] * p['capture_rate']
    return content_revenue + hardware_revenue

def total_revenue(param_series, countries) -> int:
    return content_total_revenue(param_series, countries) + hardware_total_revenue(param_series, countries) + roa_calc(param_series)
