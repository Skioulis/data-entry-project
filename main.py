from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from os import getenv
from time import sleep
from bs4 import BeautifulSoup
import requests
from scraping import Scraping, Listing
from some_fuctions import driver_initialization

load_dotenv(dotenv_path=".env")
form_url=getenv("link-to-form")
mail=getenv("mail")
password=getenv("password")

scrape= Scraping()


driver = driver_initialization()
driver.get(form_url)
p = driver.current_window_handle
sleep(3)


for i in range(scrape.no_of_listings):
    listing = scrape.listings[i]
    continue_without_save = driver.find_elements(By.XPATH, value="/html/body/div[2]/div/div[2]/div[3]/div[1]/span/span")

    if continue_without_save:
        continue_without_save[0].click()

    input_texts = driver.find_elements(By.CSS_SELECTOR, value="div div div div div div div div div input")

    input_texts[0].send_keys(listing.address)
    input_texts[1].send_keys(listing.price)
    input_texts[2].send_keys(listing.url, Keys.TAB, Keys.ENTER)

    sleep(1)
    next_answer = driver.find_elements(By.CSS_SELECTOR, value="div div div div div a")
    next_answer[1].click()

driver.quit()