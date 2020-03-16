from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
    def search_element(self,tru):
        return self.driver.find_element(*tru)
    def search_elements(self,tru):
        return self.driver.find_elements(*tru)
    def click_element(self,tru):
        self.search_element(tru).click()
    def input_element(self,tru,text):
        e = self.search_element(tru)
        e.clear()
        e.send_keys(text)


