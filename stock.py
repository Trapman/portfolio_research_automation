"""The best way to screen stocks is through following the news and tracking historical performance. This includes trading ratios, and peer comparison, not just stock price 
tracking. For a holistic approach to picking stocks, or conducting analysis you want both the income statement and balance sheet on top of market trading statistics. 
From there, you have everything that you need. With a little bit of knowledge on Python, and JSON, you’ll be able to set up your own automated stock tracker in under 10 minutes. 
You’ll be pulling balance sheet and income statement items, as well as other key information such as a company’s CEO. Although only a couple of data points are going 
to be walked through, there are many other data points to explore."""

############################################

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:32:51 2020

@author: das68451
"""

import requests
import pandas as pd

def getdata(stock):
 # Company Quote Group of Items
    company_quote = requests.get(f"https://financialmodelingprep.com/api/v3/quote/{stock}")
    company_quote = company_quote.json()
    share_price = float("{0:.2f}".format(company_quote[0]['price']))
    
# Balance Sheet Group of Items    
    BS = requests.get(f"https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/{stock}?period=quarter")
    BS = BS.json()
    
#Total Debt
    debt = float("{0:.2f}".format(float(BS['financials'][0]['Total debt'])/10**9))
#Total Cash
    cash = float("{0:.2f}".format(float(BS['financials'][0]['Cash and short-term investments'])/10**9))
    
# Income Statement Group of Items
    IS = requests.get(f"https://financialmodelingprep.com/api/v3/financials/income-statement/{stock}?period=quarter")
    IS = IS.json()

# Most Recent Quarterly Revenue
    qRev = float("{0:.2f}".format(float(IS['financials'][0]['Revenue'])/10**9))
    
# Company Profile Group of Items
    company_info = requests.get(f"https://financialmodelingprep.com/api/v3/company/profile/{stock}")
    company_info = company_info.json()
# Chief Executive Officer
    ceo = company_info['profile']['ceo']
    
    return (share_price, cash, debt, qRev, ceo)

tickers = ('AAPL', 'MSFT', 'GOOG', 'T', 'CSCO', 'INTC', 'ORCL', 'AMZN', 'FB', 'TSLA', 'NVDA')
    
data = map(getdata, tickers)

df = pd.DataFrame(data,
     columns=['Total Cash', 'Total Debt', 'Q3 2019 Revenue', 'CEO'],
     index=tickers)
print(df)

# Writing to Excel
writer = pd.ExcelWriter('example.xlsx')
df.to_excel(writer, 'Statistics')
writer.save()
