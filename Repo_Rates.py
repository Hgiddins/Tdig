import gspread
from credentials import credentials
import Market_Data
import time
import numpy as np
from datetime import datetime, timedelta

def startup():
    serviceAccount = gspread.service_account_from_dict(credentials)
    googleSheet = serviceAccount.open("TridentResearchPlatform")
    worksheet = googleSheet.worksheet("Historic Repo Rates")
    return worksheet

def get_last_date(worksheet):
    last_dates = {}
    rate_types_columns = {
        'EFFR': (1, 4),  # Columns A-D
        'OBFR': (6, 7),  # Columns F-G
        'TGCR': (9, 10),  # Columns I-J
        'BGCR': (12, 13),  # Columns L-M
        'SOFR': (15, 16)  # Columns O-P
    }
    default_date = datetime.strptime('1990-01-01', '%Y-%m-%d').date()
    for rate_type, (start_col, end_col) in rate_types_columns.items():
        last_date_str = worksheet.col_values(end_col)[-1]  # Using end_col to get the date column
        try:
            last_date = datetime.strptime(last_date_str, '%Y-%m-%d').date()
        except ValueError:
            # Unable to parse last_date_str as a date, use the default date
            last_date = default_date
        last_dates[rate_type] = last_date
    return last_dates

def fetch_new_data(startdate):
    df = Market_Data.fetch_nyfed_overnight_rates(startdate=startdate)
    if df.empty:
        print("No data to update.")
        return df
    return df

def write_data_to_sheet(worksheet, data, rate_type):
    rate_types_columns = {
        'EFFR': (1, 4),  # Columns A-D
        'OBFR': (6, 7),  # Columns F-G
        'TGCR': (9, 10),  # Columns I-J
        'BGCR': (12, 13),  # Columns L-M
        'SOFR': (15, 16)  # Columns O-P
    }
    start_col,end_col = rate_types_columns[rate_type]


    rate_data = data[data['Rate Type'] == rate_type]
    rate_data = rate_data.fillna('')
    rate_data = rate_data.drop(columns=['Rate Type'])

    if rate_type != 'EFFR':
        rate_data = rate_data.drop(columns=['Target (Lower Bound)', 'Target (Upper Bound)'])

    rate_data = rate_data.iloc[::-1]  # Reverse the order of the data so it's old to new
    data_to_write = rate_data.values.tolist()
    last_row = len(worksheet.col_values(start_col))
    end_row = last_row + len(data_to_write)
    cell_range = f"{chr(64 + start_col)}{last_row + 1}:{chr(64 + end_col)}{end_row}"

    try:
        response = worksheet.update(cell_range, data_to_write)
        # Assuming a successful response contains an 'updatedRange' key
        if 'updatedRange' in response:
            print(f"{rate_type} data written successfully.")
        else:
            print(f"Unexpected response when writing {rate_type} data: {response}")
    except Exception as e:
        print(f"Failed to write {rate_type} data: {e}")

def update_historic_repo_rates():
    worksheet = startup()
    last_dates = get_last_date(worksheet)
    oldest_date = min(last_dates.values())  # Find the oldest date among all last dates
    start_date = (oldest_date + timedelta(days=1)).strftime('%Y-%m-%d')
    new_data = fetch_new_data(start_date)  # Fetch the data once
    if not new_data.empty:
        for rate_type in last_dates.keys():
            rate_data = new_data[new_data['Rate Type'] == rate_type]  # Filter the data for the current rate type
            if not rate_data.empty:
                write_data_to_sheet(worksheet, rate_data, rate_type)

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    update_historic_repo_rates()  # Call your main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the total execution time
    print(f"Execution time: {execution_time:.2f} seconds")  # Print the execution time to 2 decimal places
