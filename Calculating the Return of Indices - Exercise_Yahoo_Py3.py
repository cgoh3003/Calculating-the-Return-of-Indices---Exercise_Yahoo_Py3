import numpy as np
import pandas as pd 
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
tickers=['^GSPC','^IXIC','^DJI']

ind_data = pd.DataFrame()

for t in tickers:
    ind_data[t]=wb.DataReader(t,data_source='yahoo',start='2000-1-1')['Adj Close']
ind_data.head()
(ind_data/ind_data.iloc[0]*100).plot(figsize=(15,6));
plt.show
ind_returns=(ind_data/ind_data.shift(1))-1
ind_returns.tail()
annual_ind_returns=ind_returns.mean()*250
annual_ind_returns