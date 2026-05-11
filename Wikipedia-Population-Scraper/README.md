# Wikipedia Population Scraper

This is a simple Python script I wrote to practice web scraping. It fetches population data from Wikipedia and displays it using Pandas.

## How it works
I used the `requests` library to get the page content and `pandas` to extract the tables. Since Wikipedia blocks requests without headers, I added a simple User-Agent.

## Requirements
You will need these libraries:
- requests
- pandas
- lxml

Source: [Wikipedia - List of Countries by Population](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population)

## Usage
Just run the script and it will print the first 5 rows of the population table.
