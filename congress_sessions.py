# This script pulls data from a web site that shows info on 20 years of U.S. Congress sessions, from 1867 - 1887
# The output should show The Congress #, the # of years of the Congress session, the Beginning and End Dates.
# https://history.house.gov/Institution/Session-Dates/40-49/

import requests
from bs4 import BeautifulSoup

# Get the information from the web page
url = "https://history.house.gov/Institution/Session-Dates/40-49/"
response = requests.get(url)

# Start using BeautifulSoup to find the table on the page and get the data from the table.
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table")
rows = table.find_all("tr")

# Use a FOR loop to get the data 
for row in rows:
    # Find all the cells in the row
    cells = row.find_all("td")
    
# Extract the data from the cells, if there are any
    if len(cells) > 0:
        congress_number = cells[0].get_text().strip()
        years = cells[1].get_text().strip()
        begin_date = cells[2].get_text().strip()
        adjournment_date = cells[3].get_text().strip()
        
# Print out the info
        print(f"Congress Number: {congress_number}")
        print(f"Years: {years}")
        print(f"Beginning Date: {begin_date}")
        print(f"Adjournment Date: {adjournment_date}")
        print()
