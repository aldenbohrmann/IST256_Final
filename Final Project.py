# Group 14
# IST256 Fianl Project
# Alden Bohrmann, Maya Alston, Ayana Kerr

# import staments
import requests
from bs4 import BeautifulSoup
import pandas as pd
import wikipedia
import re


# Make sure user input is a valid year, if the year is not valid, ask for another year.
print("\n")
print("Welcome to the Major Leauge Sports Calander Search \n")

while True:
    user_input_year = int(input("Enter Sports Schedule Year (2011-2021): "))
    if 2011 <= user_input_year <= 2021:
        break
    else:
        print("Sorry that year is not within 2011 and 2021, Please Try Again!")


# If a nunmber assigns user_input_year to year variable
year = user_input_year
# For whatever year the user inputs, .fornmat will replace the year in the URL
url = "http://www.topendsports.com/events/calendar-{y}.htm".format(y=year)
# Scrape the HTML at the url
r = requests.get(url)
# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(r.text, "html.parser")
# Find the table in the HTML code
table = soup.find('table')
# In the element table, find all 'tr' tags
rows = table.findAll('tr')

# Create new blank list name data
data = []
# Names of columns, also know as headers in HTML
header = ['date', 'sport', 'event', 'location']


data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
# First row is blank, so get rid of it
data = data[1:]

# Function to get the value, x, and handle the errors
def get_value(x):
    try:
        return x[0].lower()
    except (TypeError, IndexError):
        return ''

# Apply function to each column to get the value out of the list
# Assigns df to create the panda dataframe
df = pd.DataFrame(data, columns=header)
df['date'] = df['date'].apply(get_value)
df['sport'] = df['sport'].apply(get_value)
df['event'] = df['event'].apply(get_value)
df['location'] = df['location'].apply(get_value)

# Prevents dataframe from outputting onto different lines depending on screensize
pd.set_option('display.expand_frame_repr', False)

# completed table print statement for panda dataframe, df
print(df)

# search sport input
# Find sport in dataframe, column 'sport


while True:
    sport_search = raw_input("Type sport to filter: ")
    sport_df = df[df['sport'] == sport_search]
    if sport_df.empty:
        print("Not a Valid Sport, Please Try Again!")
    else:
        print(sport_df)
        break
# sport_df print statement for panda dataframe, df

event_search = raw_input("Search event on wikipedia: ")
event_df = sport_df[sport_df['event'] == event_search]

# Find event in dataframe, column 'event'
# event_df print statement for panda dataframe, df

wiki_find = wikipedia.page(event_search)
wiki_find.content
print "\n", "Here is what Wikipedia has to say about your sporting event: \n", "\n", wikipedia.summary(event_search)
