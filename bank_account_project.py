'''
***All credit for the data sourced for this project goes to exchangerates.org.uk***

This program simulates a transaction with an ATM machine. If the user decides to 
withdraw money from their bank account, they are given the option to enter the 
withdrawal amount in a foreign currency. The program will grab the most updated 
currency exchange figures and return the amount remaining in the bank account 
in GBP. 
'''

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

'''This function scrapes conversion rates between GBP(£) and some of the most 
common currencies in the world. The function takes two arguments: 'gbp' which
can be a float or integar that notates the amount in gbp that we are wanting 
to convert to a different currency , and 'currency' which is the currency 
that the amount in gbp is to be converted to.''' 
def currency_func(gbp,currency):

    page = requests.get(URL,'html.parser')
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Grabbing the desired div and table for which the desired data is housed
    table = soup.find('table')
     
    return float(table.find_all('td')[currencies_table_indices[currency]].text) * gbp


class BankAccount(object):

    
    def __init__(self,balance=0.0):
        self.balance = balance

    
    def withdraw(self):
        print('You may withdraw money from this ATM in the following currencies: ')
        for value in currencies_table_indices:
            print(value, end = ", ")
        currency = str(input('Please select which of these currencies you would like to proceed with: '))
        
        # Should implement error handling here for when an invalid currency is entered.
        
        while True:
           withdraw_amount = float(input('How many ' + currency.upper() + 's would you like to withdraw? '))
           
           if currency.upper() == "GBP":
               self.balance -= withdraw_amount
               break
           else:
               withdraw_amount /= float(currency_func(1, currency.upper()))
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break           
           
        print(f'Withdraw successful. You now have a balance of £{str(round(self.balance, 2))}')

    
    def deposit(self):
        deposit_amount = float(input("How many GBPs would you like to deposit? \n"))
        self.balance += deposit_amount
        print(f'Deposit successful. You now have a balance of £{str(round(self.balance, 2))}')


    def display(self):
        print(f'You have a balance of £{str(round(self.balance, 2))}')
