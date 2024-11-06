from time import sleep
from bs4 import BeautifulSoup
import requests

zillow_clone_url="https://appbrewery.github.io/Zillow-Clone/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


def get_soup(url: str = zillow_clone_url):
    response = requests.get(url=url, headers=header)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

soup = get_soup()


def get_the_urls():
    url_list = soup.select("a.property-card-link")
    return [url.get('href') for url in url_list]


class Scraping:
    def __init__(self):
        self.listings = get_the_urls()
        self.prices = []
        self.addresses = []
