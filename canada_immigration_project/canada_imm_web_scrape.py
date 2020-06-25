import requests
from bs4 import BeautifulSoup
import pandas as pd
    
url = 'https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations/results-previous.html'
page = requests.get(url,'html.parser')
soup = BeautifulSoup(page.content, 'html.parser')
div = soup.find('div',attrs={'class': 'mwsgeneric-base-html parbase section'})

i = 0
j = 0
invitation_stream = []
num_of_invitations = []
rank_required = []
date_time = []
crs_score = []
tie_breaking_rule = []

# This for loop takes the last 50 rounds of invitations and splits the necessary data from each round into separate lists. Each of these lists will become their own columns in our database  
for i in range(50):
    invitation_stream.append(soup.find_all('p')[j].text)
    num_of_invitations.append(soup.find_all('p')[j + 2].text)
    rank_required.append(soup.find_all('p')[j + 3].text)
    date_time.append(soup.find_all('p')[j + 4].text)
    crs_score.append(soup.find_all('p')[j + 5].text)
    tie_breaking_rule.append(soup.find_all('p')[j + 6].text)
    j += 7

# Now I will clean the data. In particular, we only need the numbers from most of the lists

i = 0
for i in range(50):
    num_of_invitations.append(''.join([char for char in num_of_invitations[i] if char.isdigit()]))
    rank_required.append(''.join([char for char in rank_required[i] if char.isdigit()]))
    date_time[i] = date_time[i].replace('Date and time of round: ','')
    date_time[i] = date_time[i].replace('at ','')
    date_time[i] = date_time[i].replace(',','')
    date_time[i] = date_time[i].replace('UTC','')
    crs_score.append(''.join([char for char in crs_score[i] if char.isdigit()]))
    tie_breaking_rule[i] = tie_breaking_rule[i].replace('Tie-breaking rule: ','')
    tie_breaking_rule[i] = tie_breaking_rule[i].replace('at ','')
    tie_breaking_rule[i] = tie_breaking_rule[i].replace(',','')
    tie_breaking_rule[i] = tie_breaking_rule[i].replace('UTC','')
num_of_invitations = [int(num) for num in num_of_invitations[50:]]
rank_required = [int(num) for num in rank_required[50:]]
crs_score = [int(num) for num in crs_score[50:]]

data_lists = [invitation_stream, num_of_invitations, rank_required, date_time, crs_score, tie_breaking_rule]
# Now I will convert the data into a dataframe and create a csv file with this data
df = pd.DataFrame(data_lists).transpose()
df.columns = ['invitation_stream', 'num_of_invitations', 'rank_required', 'date_time', 'crs_score', 'tie_breaking_rule']
df.to_csv(r'C:\Users\Chris\Documents\GitHub\python\canada_immigration_project\express_entry.csv')