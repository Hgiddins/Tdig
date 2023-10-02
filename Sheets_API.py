import gspread
from credentials import credentials
import Market_Data
import time
import numpy as np


def startup():
    serviceAccount = gspread.service_account_from_dict(credentials)
    googleSheet = serviceAccount.open("TridentResearchPlatform")
    worksheet = googleSheet.worksheet("Federal Treasuries")
    return worksheet


def add_us_treasury_yields(worksheet, top_left_row, top_left_col):
    # Get US bond data using the fetch_us_bonds() function
    df = Market_Data.fetch_us_bonds()

    # Combine header and data
    data_to_write = [df.columns.values.tolist()] + df.values.tolist()

    # Convert column number to letter (e.g., 2 -> B)
    col_letter = chr(64 + top_left_col)

    # Define the range
    end_row = top_left_row + len(data_to_write) - 1
    end_col = chr(64 + top_left_col + len(df.columns) - 1)
    cell_range = f"{col_letter}{top_left_row}:{end_col}{end_row}"

    # Write to Google Sheet in one go
    worksheet.update(cell_range, data_to_write)

def add_brazil_treasury_yields(worksheet, top_left_row, top_left_col):

    # Write headers first
    df = Market_Data.fetch_brazil_bonds()
    data_to_write = [df.columns.values.tolist()] + df.values.tolist()

    # Convert column number to letter (e.g., 2 -> B)
    col_letter = chr(64 + top_left_col)

    # Define the range
    end_row = top_left_row + len(data_to_write) - 1
    end_col = chr(64 + top_left_col + len(df.columns) - 1)
    cell_range = f"{col_letter}{top_left_row}:{end_col}{end_row}"

    # Write to Google Sheet in one go
    worksheet.update(cell_range, data_to_write)





def add_nyfed_rates(worksheet, top_left_row, top_left_col):
    df = Market_Data.fetch_nyfed_overnight_rates()
    if df.empty:
        print("No data to update.")
        return

    # Replace NaN with an empty string
    df = df.replace(np.nan, '', regex=True)

    data_to_write = [df.columns.values.tolist()] + df.values.tolist()

    # Convert column number to letter (e.g., 2 -> B)
    col_letter = chr(64 + top_left_col)

    # Define the range
    end_row = top_left_row + len(data_to_write) - 1
    end_col = chr(64 + top_left_col + len(df.columns) - 1)
    cell_range = f"{col_letter}{top_left_row}:{end_col}{end_row}"

    # Write to Google Sheet in one go
    # Adjusted based on the warning
    worksheet.update(cell_range, data_to_write)


########################################################################################################################


def update_sheet():  # INSERT ALL FUNCTIONS
    worksheet = startup()
    add_us_treasury_yields(worksheet, top_left_row=3, top_left_col=2)
    add_nyfed_rates(worksheet, top_left_row=25, top_left_col=2)
    add_brazil_treasury_yields(worksheet,top_left_row=3, top_left_col=9)


if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    update_sheet()  # Call your main function
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate the total execution time
    print(f"Execution time: {execution_time:.2f} seconds")  # Print the execution time to 2 decimal places
