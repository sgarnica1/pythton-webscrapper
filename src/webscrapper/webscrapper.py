# webscrapper/webscrapper.py

from bs4 import BeautifulSoup
import pandas as pd
import requests

def main():
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('table', class_="wikitable sortable")
    table_titles = table.find_all('th')

    table_titles_text = [title.text.strip() for title in table_titles]

    df = pd.DataFrame(columns = table_titles_text)

    table_rows = table.find_all('tr')

    for row in table_rows[1:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]
        df.loc[len(df)] = individual_row_data   

    print(df)
