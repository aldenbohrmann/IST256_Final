# Group 14
# IST256 Fianl Project
# Alden Bohrmann, Maya Alston, Ayana Kerr

# import staments
import requests
from bs4 import BeautifulSoup
import pandas as pd
import wikipedia


# Make sure user input is a valid year, if the year is not valid, ask for another year.
while True:
    try:
        user_input_year = int(input("Enter Year (2011-2021): "))
        break
    except NameError, AttributeError:
        print("WOAH! That was no valid year. Please try again...")


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
sport_search = raw_input("Type sport to filter: ")
# Find sport in dataframe, column 'sport

sport_df = df[df['sport'] == sport_search]

# sport_df print statement for panda dataframe, df
print(sport_df)
# search event input
event_search = raw_input("Search event on wikipedia: ")
# Find event in dataframe, column 'event'
event_df = sport_df[sport_df['event'] == event_search]
# event_df print statement for panda dataframe, df

wiki_find = wikipedia.page(event_search)
wiki_find.content
print "Here is what Wikipedia has to say about your sporting event: \n", "\n", wikipedia.summary(event_search)
