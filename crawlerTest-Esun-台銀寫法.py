import pandas as pd
dfs=pd.read_html('https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/foreign-exchange-rates')
print(dfs)
#currency = dfs[0]