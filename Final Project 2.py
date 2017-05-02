from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd

url = "http://www.topendsports.com/events/calendar-2017.htm"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

soup.find_all("list")
table = soup.find_all("list")
rows = table.find_all('tr')

data = {
    'date' : [],
    'sport' : [],
    'event' : [],
    'location' : []
}
for row in rows:
    cols = row.find_all("tr")
    data['date'].append( cols[0].get_text() )
    data['sport'].append( cols[1].get_text() )
    data['event'].append( cols[2].get_text() )
    data['location'].append( cols[3].get_text() )

sport_data = pd.DataFrame( data )
sport_data.to_csv("2017 Sports Schedule.csv")


print(data)
