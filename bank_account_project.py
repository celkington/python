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



# This function scrapes conversion rates between GBP(£) and some of the most 
# common currencies in the world. The function takes one argument, gbp, that 
# must be either an integar or a float. 
def currency_func(gbp):

    page = requests.get(URL,'html.parser')
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Grabbing the desired div and table for which the desired data is housed
    table = soup.find('table')
    
    # Grabbing all of the desired table data 
    eur_exch = float(table.find_all('td')[3].text)
    usd_exch = float(table.find_all('td')[8].text)
    nzd_exch = float(table.find_all('td')[13].text)
    aud_exch = float(table.find_all('td')[18].text)
    cad_exch = float(table.find_all('td')[23].text)
    jpy_exch = float(table.find_all('td')[28].text)
    zar_exch = float(table.find_all('td')[33].text)
    aed_exch = float(table.find_all('td')[38].text)
    inr_exch = float(table.find_all('td')[43].text)
    try_exch = float(table.find_all('td')[48].text)
    chf_exch = float(table.find_all('td')[53].text)
    
    exchange_rates = [eur_exch, usd_exch, nzd_exch, aud_exch, cad_exch,
                      jpy_exch, zar_exch, aed_exch, inr_exch, try_exch,
                      chf_exch]
    
    return [gbp * x for x in exchange_rates]


class BankAccount(object):

    
    def __init__(self,balance=0.0):
        self.balance = balance

    
    def withdraw(self):
        currency = str(input('''You may withdraw your money in the following currencies: 
        GBP, EUR, USD, NZD, AUD, CAD, JPY, ZAR, AED, INR, TRY, CHF. 
        What currency do you want to withdraw your money in? '''))
        
        # Should implement error handling here for when an invalid currency is entered.
        
        while True:
           withdraw_amount = float(input('How many ' + currency.upper() + 's would you like to withdraw? '))
           
           # Each if statement calculates the withdrawal amount in GBP for any of the given currencies
           # Should try to make this portion of the program more elegent with a function
           
           if currency.upper() == 'EUR':
               withdraw_amount /= float(currency_func(1)[0])
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break
           
           elif currency.upper() == 'USD':
               withdraw_amount /= float(currency_func(1)[1])
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break
           
           elif currency.upper() == 'NZD':
               withdraw_amount /= float(currency_func(1)[2])
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break
           
           elif currency.upper() == 'AUD':
               withdraw_amount /= float(currency_func(1)[3])
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break
           
           elif currency.upper() == 'CAD':
               withdraw_amount /= float(currency_func(1)[4])
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break
           
           elif currency.upper() == 'JPY':
               withdraw_amount /= float(currency_func(1)[5])
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break
           
           elif currency.upper() == 'ZAR':
               withdraw_amount /= float(currency_func(1)[6])
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break
           
           elif currency.upper() == 'AED':
               withdraw_amount /= float(currency_func(1)[7])
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break
           
           elif currency.upper() == 'INR':
               withdraw_amount /= float(currency_func(1)[8])
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break
           
           elif currency.upper() == 'TRY':
               withdraw_amount /= float(currency_func(1)[9])
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break
          
           elif currency.upper() == 'CHF':
               withdraw_amount /= float(currency_func(1)[10])
               if withdraw_amount > self.balance:
                   print("Insufficient funds. Enter again. ")
               else:
                   self.balance -= withdraw_amount
                   break
           
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
