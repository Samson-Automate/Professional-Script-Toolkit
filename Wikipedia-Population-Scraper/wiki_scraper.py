import requests
import pandas as pd
from io import StringIO

# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

# User-Agent is important, otherwise Wikipedia might block the script as a bot
headers = {
    "User-Agent": "Mozilla/5.0 "
}

try:
    # Sending the request to fetch HTML content
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    response.raise_for_status()

    # Using StringIO because pandas will soon stop accepting raw strings directly
    html_data = StringIO(response.text)

    # Use Pandas Library to read html and parse it into a list of DataFrames
    tables = pd.read_html(html_data)

    print(f'Tables found: {len(tables)}')

    # Wikipedia has multiple tables, index [0] is usually the main population table
    if len(tables) > 0:
        df = tables[0]
        print("First few rows of the population table:")
        print(df.head())
    else:
        print("No tables found on the page.")

except Exception as e:
    # Error handling to catch network or parsing issues
    print(f"An error occurred while scraping: {e}")
