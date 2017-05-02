#import statements

from bs4 import BeautifulSoup
import urllib2
import pandas as pd

#website
wiki = "http://www.topendsports.com/events/calendar-2017.htm"
#ignore, used for handling Wikipedia's scraping issue
header = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, "html.parser")

#column titles
date = ""
sport = ""
event = ""
location = ""

#Calendar by month table
table = soup.find_all(class_='list')


for row in table.findAll("tr"):
    cells = row.findAll("th")
    #For each "tr", assign each "td" to a variable.
    if len(cells) == 5:
        date = cells[0].find(text=True)
        sport = cells[1].findAll(text=True)
        event = cells[2].find(text=True)
        location = cells[3].find(text=True)
    print(cells)

#def search(cells):
    #user_input = input("Enter a sport that you would like to see all of the major events for 2017")

#panadas
search(cells)
