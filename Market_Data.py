import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


# def US_Treasury_yield_curve_rates():
#     API_URL = "https://data.nasdaq.com/api/v3/datasets/USTREASURY/YIELD.json"
#     API_KEY = "7NL5tnLGDWJZZ2xTkaVK"
#
#     def fetch_data(api_url, api_key, limit=1):
#         response = requests.get(api_url, params={
#             "api_key": api_key,
#             "limit": limit
#         })
#
#         if response.status_code == 200:
#             return response.json()
#         else:
#             response.raise_for_status()
#
#     data = fetch_data(API_URL, API_KEY)
#
#     # The latest data will be the first item in the 'data' list
#     latest_data = data["dataset"]["data"][0]
#
#     keys = ["date", "1_month_yield", "2_month_yield", "3_month_yield", "6_month_yield", "12_month_yield"]
#     yield_data = dict(zip(keys, latest_data))
#
#     print("-----------------------")
#     print("US Treasury Yield Rates")
#     print(f"Date: {yield_data['date']}")
#     for key, value in yield_data.items():
#         if key != 'date':
#             print(f"{key.replace('_', ' ').title()}: {value}%")
#
#     return yield_data

def fetch_us_bonds():
    URL = "http://www.worldgovernmentbonds.com/country/united-states/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {
        'class': 'w3-table w3-white table-padding-custom w3-small font-family-arial table-valign-middle'})

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
    df = pd.DataFrame(extracted_data, columns=columns)

    # Convert string columns with % and bp to float values
    df['Yield'] = df['Yield'].str.rstrip('%').astype('float') / 100
    df['Chg 1M'] = df['Chg 1M'].str.rstrip(' bp').str.replace('+', '').astype('float') / 10000
    df['Chg 6M'] = df['Chg 6M'].str.rstrip(' bp').str.replace('+', '').astype('float') / 10000

    return df

def fetch_brazil_bonds():
    URL = "http://www.worldgovernmentbonds.com/country/brazil/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {
        'class': 'w3-table w3-white table-padding-custom w3-small font-family-arial table-valign-middle'})

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
    df = pd.DataFrame(extracted_data, columns=columns)

    # Convert string columns with % and bp to float values
    df['Yield'] = df['Yield'].str.rstrip('%').astype('float') / 100
    df['Chg 1M'] = df['Chg 1M'].str.rstrip(' bp').str.replace('+', '').astype('float') / 10000
    df['Chg 6M'] = df['Chg 6M'].str.rstrip(' bp').str.replace('+', '').astype('float') / 10000

    return df


def fetch_nyfed_overnight_rates(limit = 5, startdate = None ):

    # startdate format must be format '2020-10-03'
    if startdate == None:
        URL = f"https://markets.newyorkfed.org/read?productCode=50&eventCodes=510,515,520,500,505&limit={limit}&startPosition=0&sort=postDt:-1&format=json"
    else:
        URL = f"https://markets.newyorkfed.org/read?startDt={startdate}&eventCodes=510,515,520,500,505&productCode=50&sort=postDt:-1,eventCode:1&format=json"

    response = requests.get(URL)
    if response.status_code != 200:
        response.raise_for_status()

    # Parsing the JSON content
    data = response.json()

    df_list = []
    if 'refRates' in data and len(data['refRates']) > 0:
        for entry in data['refRates']:

            effective_date = entry['effectiveDate']
            percent_rate = entry['percentRate']
            # volume = entry['volumeInBillions']
            rate_type = entry['type']

            rate_data = {
                "Rate Type": rate_type,
                "Rate": percent_rate/100,
                # "Volume in Billions": volume,
                "Date": effective_date
            }
            if rate_type == 'EFFR':
                rate_data["Target (Lower Bound)"] = entry['targetRateFrom']/100
                if datetime.strptime(effective_date, '%Y-%m-%d').date() >= datetime(2016, 1, 3).date():
                    rate_data["Target (Upper Bound)"] = entry['targetRateTo']/100
                # else:
                #     rate_data["Target (Upper Bound)"] = ''


            df_list.append(rate_data)

    # Specify the column order when creating the dataframe
    # columns_order = ["Rate Type", "Rate", "Volume in Billions", "Target (Lower Bound)", "Target (Upper Bound)", "Date"]
    columns_order = ["Rate Type", "Rate", "Target (Lower Bound)", "Target (Upper Bound)", "Date"]

    df = pd.DataFrame(df_list, columns=columns_order)
    print(df)
    return df





if __name__ == "__main__":
    # US_Treasury_yield_curve_rates()
    df = fetch_us_bonds()
    fetch_nyfed_overnight_rates(limit = 5, startdate='2005-10-03')
    print(df)
    df = fetch_brazil_bonds()
    print(df)
