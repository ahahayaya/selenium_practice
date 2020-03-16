from time import sleep

from selenium import webdriver
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_xpath()
handle = driver.window_handles
driver.switch_to.window(handle)
driver.switch_to.frame()
alert = driver.switch_to.alert
alert.text
alert.accept()
alert.dismiss()
js = 'window.scrollto(5,12)'
driver.execute_script()
select_e = driver.find_element_by_xpath('xxx')
select_o = Select(select_e)
select_o.select_by_index()
select_o.select_by_value()
select_o.select_by_visible_text()


action = ActionChains(driver)
element_action = action.context_click('element')
element_action.perfor()


driver.implicitly_wait(2)


class classname():
    def test(self):
        print('hello python')
suite = unittest.TestSuite()
suite.addTest(classname('methord'))
runner = unittest.TextTestRunner()
runner.run(suite)














sleep(3)
driver.quit()
