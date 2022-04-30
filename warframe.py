
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager #used to install latest firefox driver
from bs4 import BeautifulSoup #used to parse prices 
from selenium.webdriver.common.by import By
import time


warframe_market = "https://xbox.warframe.market/"
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

driver.get(warframe_market)

item_to_search = input("Enter item name: ")
item_search_field = "/html/body/section/section/div/section[1]/div[1]/section/div/section/div/section/span/input"

def search_item(item_name):
    search_bar = driver.find_element(By.XPATH, value=item_search_field)
    search_bar.click()
    print(item_name)
    search_bar.send_keys(f"{item_name}")
    first_option = "/html/body/section/section/div[2]/section[1]/div[1]/section/div/section/div/section[2]/ul/li[2]"
    driver.find_element(By.XPATH, value=first_option).click()
    launch_search = driver.find_element(By.XPATH, value="/html/body/section/section/div/section[1]/div[1]/section/div/section/button")
    launch_search.click()

    found_prices = [i.text for i in driver.find_elements(By.CLASS_NAME, value="price")]
    print(found_prices)

exe = True
search_item(item_to_search)