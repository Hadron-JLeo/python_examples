from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import pathlib
from pathlib import Path

wiki_url = 
wiki_table = "wikitable sortable jquery-tablesorter"
wiki_tag = "tbody"

options = Options()
page_wait_time = 20

def initialiseDriver(b):
    options.headless = b
#caps = webdriver.DesiredCapabilities.CHROME.copy()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    WebDriverWait(driver, 1)
    time.sleep(1)
    return driver

d = initialiseDriver(False)
d.get(wiki_url) # get on wiki page
time.sleep(1)

def Get_Servants():
    servant_list = []
    d.implicitly_wait(3)
    table = d.find_element_by_xpath("//*[contains(@class, 'wikitable sortable jquery-tablesorter')]").find_element_by_tag_name("tbody")
    table_elements = table.find_elements_by_tag_name("tr")
    

    for index, i in enumerate(table_elements):
        
        my_servant = table_elements[index].find_element_by_tag_name("td").find_element_by_css_selector('a[title]') # gets me the attribute title
        star_amount = table_elements[index].find_elements_by_tag_name("td")[2].text
        my_stars = len(star_amount.replace(" ", ""))

        # star_symbol = "\u9733"

        

        print(my_servant.get_attribute('title'), "Rarity = " + str(my_stars), index) # prints the content of attribute title
        my_stars = 0
        
        if (index == len(table_elements)):
            d.close()

    return servant_list

def Rid_Popup():
    
    try:
        #d.implicitly_wait(page_wait_time)
        #d.implicitly_wait(3)
        #_2o0B8MF50eAK1jv60jldUQ
        d.find_element_by_xpath("//*[contains(@class, '_2o0')]").click()
        d.implicitly_wait(2)
        print("found")
    except:
        try:
            d.find_element_by_name("data-tracking-opt-in-accept").click()
            d.implicitly_wait(2)
        except:
            print("Not found")
            pass

Rid_Popup()
Get_Servants()
    
