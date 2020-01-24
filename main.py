#!/usr/bin/env python
#coding:utf-8

import config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as soup

def login_into_tesco_clubcard(driver, username, password): # Logins into Tesco wesbite
    user_field_id = "username"
    pass_field_id = "password"         
    userFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(user_field_id))
    userFieldElement.clear()
    userFieldElement.send_keys(username)
    passFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(pass_field_id))
    passFieldElement.clear()
    passFieldElement.send_keys(password)
    passFieldElement.send_keys(Keys.ENTER)
    
if __name__ == '__main__':
    login_page_url = 'https://secure.tesco.com/account/en-GB/login'    
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    driver.get(login_page_url) # login page
    login_into_tesco_clubcard(driver, config.email, config.password)
    
    # TODO - navigate to clubcard points page - https://secure.tesco.com/Clubcard/MyAccount/Points/Home
    
    driver.quit()    