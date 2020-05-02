'''This function scrapes conversion rates between GBP(£) and some of the most common currencies in the world. The function takes two 
arguments: 'gbp' which can be a float or integar that notates the amount in gbp that we are wanting to convert to a different currency, 
and 'currency' which is the currency that the amount in gbp is to be converted to.''' 

import requests
from bs4 import BeautifulSoup

URL = 'https://www.exchangerates.org.uk/'

currencies_table_indices = {
        "EUR": 3,
        "USD": 8,
        "NZD": 13,
        "AUD": 18,
        "CAD": 23,
        "JPY": 28,
        "ZAR": 33,
        "AED": 38,
        "INR": 43,
        "TRY": 48,
        "CHF": 53
        }

def currency_func(gbp,currency):

    page = requests.get(URL,'html.parser')
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Grabbing the desired div and table for which the desired data is housed
    table = soup.find('table')
     
    return float(table.find_all('td')[currencies_table_indices[currency]].text) * gbp
