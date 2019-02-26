# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 08:49:16 2019

@author: d805664
"""

import quandl
import pandas as pd

quandl.ApiConfig.api_key = "-t85uxfxDxUd4NxyE7DF"


# Oil Prices
data = quandl.get("EIA/PET_RWTC_D")

#data.tail(100).plot()


# Brazil's BOP
data = quandl.get("UGID/BOP_BRA")

#data["OVERALL BALANCE"].plot()

# CDI in annual terms

data = quandl.get("BCB/4392", start_date='2018-01-31')

#data.plot()

# Exchange Rate

data = quandl.get("BCB/10813", start_date='2015-01-31')

#data.plot()

#International Reserves

data = quandl.get("BCB/13621")

#data.plot()


#GDP Pct Growth

data = quandl.get("BCB/7326", start_date='2010-12-31')

#data.plot(kind="bar", grid=True)

# Net Debt/GDP

data = quandl.get("BCB/10831")

data = data.asfreq("A", how="end")

#data.plot(grid=True, title="Net Debt to GDP")

# International reserves.

data = quandl.get("BCB/3546")

data = data.asfreq("A", how="end").diff()

#data.plot(grid=True, title="International Reserves Change")


## Cálculo da inflação implícita nos EUA

# UST10Y

UST10Y = quandl.get("ECB/FM_M_US_USD_RT_BZ_USD10YZ_R_YLDE")
#UST10Y.plot()

TIPS = quandl.get("FED/TIPSY")
#TIPS["TIPSY10"].plot()

yields = pd.concat([UST10Y, TIPS], axis=1, join="inner")
yields = yields.rename(columns={"Percent per annum":"UST10Y"})

yields["implied_inflation"] = (1+ yields["UST10Y"])/(1+yields["TIPSY10"])-1

yields[["UST10Y", "TIPSY10", "implied_inflation"]].plot(grid=True, legend=False)

