import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create a values as dictionary of lists

url = "http://www.topendsports.com/events/calendar-2017.htm"

# Scrape the HTML at the url
r = requests.get(url)

# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(r.text, "html.parser")

date = []
sport = []
event = []
location = []
columns = {}

table = soup.find('table')

for row in table.find_all('table'):
    # Create a variable of all the <td> tag pairs in each <tr> tag pair,
    col = row.find_all('td')[:0]

    column_1 = col[0].string.strip()
    # and append it to date variable
    date.append(column_1)

    column_2 = col[1].string.strip()
    # and append it to sport variable
    sport.append(column_2)

    column_3 = col[2].string.strip()
    # and append it to event variable
    event.append(column_3)

    column_4 = col[3].string.strip()
    # and append it to location variable
    location.append(column_4)

    columns = {'date': date, 'sport': sport, 'event': event, 'location': location}

    df = pd.DataFrame(columns)

    print(df)

print(table)
