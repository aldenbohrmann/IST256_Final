import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create a values as dictionary of lists

url = "http://www.topendsports.com/events/calendar-2017.htm"

# Scrape the HTML at the url
r = requests.get(url)

# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(r.text, "html.parser")

table = soup.find('table')
rows = table.findAll('tr')
data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]

final_list = 

for w in words[]
    
print(data)
