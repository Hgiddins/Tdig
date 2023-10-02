import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "http://www.worldgovernmentbonds.com/country/brazil/"
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'w3-table w3-white table-padding-custom w3-small font-family-arial table-valign-middle'})

# Extract headers
headers = [header.text for sublist in table.find_all("tr")[:2] for header in sublist.find_all('th')]

# Extract rows
rows = table.find('tbody').find_all('tr')

data = []

for row in rows:
    columns = row.find_all(['td', 'th'])
    columns = [col.text.strip() for col in columns]
    data.append(columns)

# Remove empty strings from each sublist
cleaned_data = [list(filter(None, sublist)) for sublist in data]

# Extract required columns from cleaned data
extracted_data = []
for row in cleaned_data:
    new_row = row[:4] + [row[-1]]
    extracted_data.append(new_row)

columns = ['Maturity', 'Yield', 'Chg 1M', 'Chg 6M', 'Date Updated']

# Create the DataFrame with extracted data
df = pd.DataFrame(extracted_data, columns=columns)

print(df)
