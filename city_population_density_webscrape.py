import requests
from bs4 import BeautifulSoup

city = input('Please enter a city name: ')

def city_population_density(city):

    URL = 'https://worldpopulationreview.com/world-cities/' + city + '-population/'
    page = requests.get(URL,'html.parser')
    soup = BeautifulSoup(page.content, 'html.parser')     
    pop_dens = list(soup.find_all(('div'), class_ = 'rowvalue')[1])
    return 'The population density of ' + city.capitalize() + ' is ' + pop_dens[0] + ' km^2.'