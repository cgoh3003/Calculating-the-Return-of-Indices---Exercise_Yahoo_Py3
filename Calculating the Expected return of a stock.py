import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['MSFT', '^GSPC']
data = pd.DataFrame()
for t in tickers:
    data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']  
    
sec_returns = np.log( data / data.shift(1) )
cov = sec_returns.cov() * 250
cov_with_market = cov.iloc[0,1]
market_var = sec_returns['^GSPC'].var() * 250

MSFT_beta = cov_with_market / market_var
MSFT_er=0.025+MSFT_beta*0.05
MSFT_er