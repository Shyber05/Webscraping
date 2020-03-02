'''
This program will scrape the website "https://forecast.weather.gov/
The program extracts data from the detailed forecast section 
'''

from bs4 import BeautifulSoup
import requests
import pandas as pd


odd_days = []
even_days = []
days = []

odd_forecasts = []
even_forecasts = []
forecasts = []

#Port Saint Lucie's weather
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=27.2939&lon=-80.3503#.XlyEQMZKhhE')
soup = BeautifulSoup(page.content, 'html.parser')



# Contains all the detailed forecast information and the day of the week
for div in soup.findAll('div', class_='panel-body', id='detailed-forecast-body'):

    #Collects the days of the week
    for i in div.findAll('div','row row-odd row-forecast'):
        odd_day = i.find('b')
        odd_days.append(odd_day.getText())
    for j in div.findAll('div','row row-even row-forecast'):
        even_day = j.find('b')
        even_days.append(even_day.getText())

    #Collects the forecast for the week
    for k in div.findAll('div','row row-odd row-forecast'):
        odd_forecast = k.find('div', class_='col-sm-10 forecast-text')
        odd_forecasts.append(odd_forecast.getText())
    for l in div.findAll('div','row row-even row-forecast'):
        even_forecast = l.find('div', class_='col-sm-10 forecast-text')
        even_forecasts.append(even_forecast.getText())



#This will organize our final list 
# Algorithms complexity is O(N) not great for large data
for i,v in enumerate(even_days):
    odd_days.insert(2*i+1,v)
    days = odd_days

for i,v in enumerate(even_forecasts):
    odd_forecasts.insert(2*i+1,v)
    forecasts = odd_forecasts


# This dictionary will store the information
data = {'Day': days, 'Forecasts': forecasts}
df = pd.DataFrame(data=data)
print(df)