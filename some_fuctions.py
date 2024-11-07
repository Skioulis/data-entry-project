from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def driver_initialization():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    chrome_options.add_argument('window-position=-1930,0')  # opens at x=2000,y=0 from the start
    chrome_options.add_argument("--start-maximized")
    inner_driver = webdriver.Chrome(options=chrome_options)

    return inner_driver