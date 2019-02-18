# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:13:39 2019

@author: d805664
"""

import pandas as pd
import requests
import bs4
import time, datetime
import matplotlib.pyplot as plt

plt.style.use("ggplot")

data_inicial = round(time.mktime((datetime.datetime(2010,11,1)).timetuple()))
data_final = round(time.mktime((datetime.datetime(2019,2,18)).timetuple()))
intervalo = "1mo" #options: 1d 1wk 1mo
frequencia = "mo" #options: 1d 1wk 1mo
ticker = "BRML3"


url = "https://finance.yahoo.com/quote/{4}.SA/history?period1={0}&period2={1}&interval={2}&filter=history&frequency={3}".format(data_inicial,data_final, intervalo, frequencia, ticker)

html = requests.get(url)

soup = bs4.BeautifulSoup(html.text, "lxml")

df = pd.read_html((soup.table).prettify())[0]
df.dropna(inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df.set_index("Date", inplace=True)
df.sort_index(inplace=True)

df["Close30"] = df["Close*"].rolling(30).mean()
df["Close10"] = df["Close*"].rolling(10).mean()
df["Pct_Change"] = df["Close*"].pct_change()

df[["Close*","Pct_Change"]].plot(subplots=True, title=ticker, layout=(2,1), color="br")

