from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from os import getenv
from time import sleep
from bs4 import BeautifulSoup
import requests
from scraping import Scraping

zillow_clone_url="https://appbrewery.github.io/Zillow-Clone/"

scrape= Scraping()

print(scrape.listings)