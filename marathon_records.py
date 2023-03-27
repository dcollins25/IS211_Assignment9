# This script pulls data from a web site that lists the top 25 marathon world record times. 
# The output should show the Mark (runner's time), the Competitor, the Nat (country of the runner), the Venue (place marathon was held), and the Date (of the marathon).
# https://www.worldathletics.org/records/all-time-toplists/road-running/marathon/outdoor/men/senior?regionType=world&drop=regular&fiftyPercentRule=regular&page=1&bestResultsOnly=true&firstDay=1990-12-31&lastDay=2023-03-26

import requests
from bs4 import BeautifulSoup

# Get the information from the web page
url = 'https://www.worldathletics.org/records/all-time-toplists/road-running/marathon/outdoor/men/senior?regionType=world&drop=regular&fiftyPercentRule=regular&page=1&bestResultsOnly=true&firstDay=1990-12-31&lastDay=2023-03-26'
response = requests.get(url)

# Start using BeautifulSoup to find the table on the page and get the data from the table.
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'records-table'})

# I only wanted to print out specific columns so I looked for the headers and got the column names.
headers = table.find_all('th')
column_names = [header.text.strip() for header in headers]
rows = table.find_all('tr')[1:26]

# Use a FOR loop to get the data 
data = []
for row in rows:
    cells = row.find_all('td')
    entry = []
    for i, cell in enumerate(cells):
        # Only include data for the specified columns
        if column_names[i] in ['Mark', 'Competitor', 'Nat', 'Venue', 'Date']:
            entry.append(cell.text.strip())
    data.append(entry)

# Print the data
for entry in data:
    print('\t'.join(entry))
