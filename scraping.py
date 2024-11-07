from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv(dotenv_path=".env")
zillow_clone_url=getenv("link-to-zillow")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


def get_soup(url: str = zillow_clone_url):
    response = requests.get(url=url, headers=header)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

soup = get_soup()


def get_the_urls():
    url_list = soup.select("a.property-card-link")
    return [url.get('href') for url in url_list]

def get_the_prices():
    price_list = soup.select("span.PropertyCardWrapper__StyledPriceLine")
    finished_price_list=[]

    for item in price_list:
        item_text = item.getText()
        if "," in item_text:
            finished_price_list.append(item_text[:6])
        else:
            finished_price_list.append(f"{item_text[:2]},{item_text[2:5]}")

    return finished_price_list

def get_the_addresses():
    return [address.getText().strip() for address in soup.select("a.StyledPropertyCardDataArea-anchor address")]


class Listing:
    def __init__(self, url : str, price : str, address: str ):
        self.url = url
        self.price = price
        self.address = address

    def __str__(self):
        return f"The house at this: {self.address} is listed at: {self.price} with this url: {self.url}"


class Scraping:
    def __init__(self):
        urls = get_the_urls()
        prices = get_the_prices()
        addresses = get_the_addresses()
        self.listings = []
        self.no_of_listings = len(urls)
        for i in range(len(urls)):
            self.listings.append(Listing(url=urls[i], price=prices[i], address=addresses[i]))




