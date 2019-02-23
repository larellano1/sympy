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
from sklearn import linear_model
import numpy as np

plt.style.use("ggplot")

## Extração dos dados do ativo.

data_inicial = round(time.mktime((datetime.datetime(2013,11,1)).timetuple()))
data_final = round(time.mktime((datetime.datetime(2019,2,18)).timetuple()))
intervalo = "1mo" #options: 1d 1wk 1mo
frequencia = "1mo" #options: 1d 1wk 1mo
ticker = "VALE3"


url = "https://finance.yahoo.com/quote/{4}.SA/history?period1={0}&period2={1}&interval={2}&filter=history&frequency={3}".format(data_inicial,data_final, intervalo, frequencia, ticker)

html = requests.get(url)

soup = bs4.BeautifulSoup(html.text, "lxml")

petr = pd.read_html((soup.table).prettify())[0]
petr.dropna(inplace=True)

petr["Date"] = pd.to_datetime(petr["Date"])

petr.set_index("Date", inplace=True)
petr.sort_index(inplace=True)

petr["Close30"] = petr["Close*"].rolling(30).mean()
petr["Close10"] = petr["Close*"].rolling(10).mean()
petr["Pct_Change"] = petr["Close*"].pct_change()


## Extração dos dados do IBOVESPA.

data_inicial = round(time.mktime((datetime.datetime(2013,11,1)).timetuple()))
data_final = round(time.mktime((datetime.datetime(2019,2,18)).timetuple()))
intervalo = "1mo" #options: 1d 1wk 1mo
frequencia = "1mo" #options: 1d 1wk 1mo
ticker1 = "%5EBVSP"


url = "https://finance.yahoo.com/quote/{4}/history?period1={0}&period2={1}&interval={2}&filter=history&frequency={3}".format(data_inicial,data_final, intervalo, frequencia, ticker1)

html = requests.get(url)

soup = bs4.BeautifulSoup(html.text, "lxml")

ibov = pd.read_html((soup.table).prettify())[0]
ibov.dropna(inplace=True)

ibov["Date"] = pd.to_datetime(ibov["Date"])

ibov.set_index("Date", inplace=True)
ibov.sort_index(inplace=True)

ibov["Close30"] = ibov["Close*"].rolling(30).mean()
ibov["Close10"] = ibov["Close*"].rolling(10).mean()
ibov["Pct_Change"] = ibov["Close*"].pct_change()


## Cálculo da correlação

corr = petr["Pct_Change"].corr(ibov["Pct_Change"])
print("Correlation: {0:.4f}".format(corr))

## Plot das séries

plt.scatter(ibov["Pct_Change"], petr["Pct_Change"], color="b")
plt.title("{} x IBOV".format(ticker))
## Cálculo do beta

X = ibov[["Pct_Change"]]
Y = petr["Pct_Change"]

model = linear_model.LinearRegression()
res = model.fit(X[1:],Y[1:].to_frame())
print("Beta: {0:.4f}\nIntercept: {1:.4f}\nR2:{2:.4f}".format(res.coef_[0][0], res.intercept_[0], model.score(X[1:],Y[1:])))

plt.plot(np.linspace(-.15,.2,100), (np.vectorize(lambda x: res.coef_*x + res.intercept_))(np.linspace(-.15,.2,100)), color="r")
plt.show()
