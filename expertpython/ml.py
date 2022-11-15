import pandas as pd
import quandl
# zPXNNLbdkrx2mhPfRXUk
quandl.ApiConfig.api_key = 'zPXNNLbdkrx2mhPfRXUk'
df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close',
         'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close']
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
