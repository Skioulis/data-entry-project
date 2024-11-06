from time import sleep
from bs4 import BeautifulSoup
import requests

zillow_clone_url="https://appbrewery.github.io/Zillow-Clone/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

class Scraping:
    def __init__(self):
        self.listings = self.get_the_urls()
        self.prices = []
        self.addresses = []



    def get_the_urls(self, url: str = zillow_clone_url):
        response = requests.get(url=url, headers=header)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        houses = soup.select("ul.List-c11n-8-84-3-photo-cards li")
        # print(len(houses))
        url_list = soup.select("a.property-card-link")
        # print(len(self.listings))
        # print(self.listings[0].get_attribute_list("href"))
        return [url.get('href') for url in url_list]
