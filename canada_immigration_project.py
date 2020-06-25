import requests
from bs4 import BeautifulSoup
import pandas as pd
    
url = 'https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations/results-previous.html'
page = requests.get(url,'html.parser')
soup = BeautifulSoup(page.content, 'html.parser')
div = soup.find('div',attrs={'class': 'mwsgeneric-base-html parbase section'})
i = 0
j = 0
for i in range(75):
    print(soup.find_all('h3')[i].text) # Draw number and draw date
    print(soup.find_all('p')[j].text) # Class (CEC, PNC, PSW, general, FSW)
    print(soup.find_all('p')[j + 2].text) # Number of invitations issued
    print(soup.find_all('p')[j + 3].text) # Rank required to be invited
    print(soup.find_all('p')[j + 4].text) # Date/Time of round
    print(soup.find_all('p')[j + 5].text) # CRS score needed for invitation
    print(soup.find_all('p')[j + 6].text) # Tie-breaking rule
    print('')
    print('')
    j += 7

