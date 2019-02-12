# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:38:07 2019

@author: d805664
"""

import quandl
from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

aapl = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")

df = aapl[["Open","High","Low","Close"]]

df.reset_index(inplace=True)
df["Date"] = df["Date"].apply(mdates.date2num)

f1 = plt.subplot2grid((6, 4), (1, 0), rowspan=6, colspan=4)

candlestick_ohlc(f1, df.values,  width=.6, colorup='#53c156', colordown='#ff1717')
f1.xaxis_date()
f1.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))
plt.xticks(rotation=45)
plt.ylabel('Stock Price')
plt.xlabel('Date')

plt.show()