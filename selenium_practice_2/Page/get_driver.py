from selenium import webdriver
def get_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://www.baidu.com')
    return driver