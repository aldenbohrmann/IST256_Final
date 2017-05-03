# Group 14
# IST256 Fianl Project
# Alden Bohrmann, Maya Alston, Ayana Kerr

# import staments
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make sure user input is a valid year
while True:
    try:
        user_input_year = int(input("Enter Year (2011-2021): "))
        break
    except NameError, ValueError:
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
header = ['DATE', 'SPORT', 'EVENT', 'LOCATION']


data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
# First row is blank, so get rid of it
data = data[1:]

# Function to get the value, x, and handle the errors
def get_value(x):
    try:
        return x[0]
    except (TypeError, IndexError):
        return ''

# Apply function to each column to get the value out of the list
# Assigns df to create the panda dataframe
df = pd.DataFrame(data, columns=header)
df['DATE'] = df['DATE'].apply(get_value)
df['SPORT'] = df['SPORT'].apply(get_value)
df['EVENT'] = df['EVENT'].apply(get_value)
df['LOCATION'] = df['LOCATION'].apply(get_value)

# Final print statement for panda dataframe, df
print (df)
