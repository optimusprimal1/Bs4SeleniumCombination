from lib2to3.pgen2 import driver
import time
from selenium.webdriver.support import expected_conditions as EC
import  selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import os
import  os.path
from os import path

class SeleniumScrape():

    path = "D:\BS4Selenium\chromeDriver\chromedriver.exe"
    service = Service(path)
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service = service, options=option)
    driver.maximize_window()

    def gettingDownloadingFile(self,href):
        
        self.driver.get("https://www.pdfdrive.com"+href)
        time.sleep(10)
        return self.driver.page_source

    def driver_quit(self):
        self.driver.quit()