# webscrapper/webscrapper.py

from bs4 import BeautifulSoup
import requests

def main():
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('table', class_="wikitable sortable")
    table_titles = table.find_all('th')

    table_titles_text = [title.text.strip() for title in table_titles]
    print(table_titles_text)