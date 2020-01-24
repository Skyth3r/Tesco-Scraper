#!/usr/bin/env python
#coding:utf-8

import config, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as soup

class TescoScraper(object):

    def __init__(self, *args, **kwargs):
        self.user_field_id = "username"
        self.pass_field_id = "password"   
        
    def get_tesco_points(self):
        login_page_url = 'https://secure.tesco.com/account/en-GB/login'
        points_page_url = 'https://secure.tesco.com/Clubcard/MyAccount/Points/Home'
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        driver.get(login_page_url) # login page
        self.login_into_tesco_clubcard(driver, config.email, config.password)
        driver.get(points_page_url) # points page
        self.scrape_page(driver)
        driver.quit()            
        
    def login_into_tesco_clubcard(self, driver, username, password): # Logins into Tesco wesbite        
        user_field_element = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(self.user_field_id))
        user_field_element.clear()
        user_field_element.send_keys(username)
        pass_field_element = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(self.pass_field_id))
        pass_field_element.clear()
        pass_field_element.send_keys(password)
        pass_field_element.send_keys(Keys.ENTER)

    def scrape_page(self, driver):
        time.sleep(3)
        page_html = driver.page_source
        html_soup = soup(page_html, "html.parser")
        points_count = html_soup.find("span", id="currentPoints")
        print(points_count.text)   
    
if __name__ == '__main__': 
    tesco = TescoScraper()
    tesco.get_tesco_points()