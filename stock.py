"""The best way to screen stocks is through following the news and tracking historical performance. This includes trading ratios, and peer comparison, not just stock price 
tracking. For a holistic approach to picking stocks, or conducting analysis you want both the income statement and balance sheet on top of market trading statistics. 
From there, you have everything that you need. With a little bit of knowledge on Python, and JSON, you’ll be able to set up your own automated stock tracker in under 10 minutes. 
You’ll be pulling balance sheet and income statement items, as well as other key information such as a company’s CEO. Although only a couple of data points are going 
to be walked through, there are many other data points to explore."""

############################################

# we will use a free API for personal investing and learning, 'Financial Modeling Prep'

import requests
import pandas as pd

def getdata(stock):
 # Company Quote Group of Items
    company_quote = requests.get(f"https://financialmodelingprep.com/api/v3/quote/{stock}")
    company_quote = company_quote.json()
    share_price = float("{0:.2f}".format(company_quote[0]['price']))
    
