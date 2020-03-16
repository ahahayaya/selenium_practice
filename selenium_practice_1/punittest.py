from selenium import webdriver
import unittest

class TestClass1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.baidu.com')
    def test1(self):
        input_e = self.driver.find_element_by_xpath("//*[id='kw']")
        input_e.send_keys('python')
        search_e = self.driver.find_element_by_xpath("//*[id='su']")
        search_e.click()
        self.driver.back()
        input_e.click()
    def tearDown(self):
        self.driver.quit()
    def test2(self):
        input_e = self.driver.find_element_by_xpath("//*[id='kw']")
        input_e.send_keys('java')
        search_e = self.driver.find_element_by_xpath("//*[id='su']")
        search_e.click()
        self.driver.back()
        input_e.click()

if __name__ == '__main__':
    unittest.main()