# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:13:39 2019

@author: d805664
"""

import pandas as pd
import requests
import bs4

url = "https://finance.yahoo.com/quote/PETR4.SA/history?period1=1424224800&period2=1550458800&interval=1d&filter=history&frequency=1d"

html = requests.get(url)

soup = bs4.BeautifulSoup(html.text, "lxml")

df = pd.read_html((soup.table).prettify())[0]
pd.to_datetime(df["Date"], format="%b %d, %Y", errors="ignore")
df.set_index("Date", inplace=True)
print(df)
df[["Close*"]].plot()