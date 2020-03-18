'''
Coronavirus Status Program
This program scrapes information about the coronavirus
from the website 'www.worldmeters.info'
'''
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.text
time = soup.select('#page-top+ div')
print(f'{title}\n{time[0].text}\n')

# Collects the inital update information
current_update = soup.findAll('div',id='maincounter-wrap')
for i in current_update:
    print(f'{i.text}\n')



table_body = soup.find('tbody')
table_rows = table_body.findAll('tr')

countries = []
total_cases = []
new_cases = []
deaths = []
total_recovered = []

# This is data based on each individual country 
for tr in table_rows:
    td = tr.findAll('td')
    countries.append(td[0].text)
    total_cases.append(td[1].text)
    new_cases.append(td[2].text)
    deaths.append(td[3].text)
    total_recovered.append(td[5].text)

# Create a pandas database that will allow easy readability
indicies = [i for i in range(1,len(countries)+1)]
headers = ['Countries', 'Total Cases', 'New Cases', 'Deaths', 'Total Recovered']
df = pd.DataFrame(list(zip(countries,total_cases,new_cases,deaths,total_recovered)),columns=headers,index=indicies)
pd.set_option('display.max_rows', None)
print(f'Current status:\n{df}')