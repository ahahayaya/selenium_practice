import os,sys,pytest,allure

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
import Page,yaml
from Page.Page_Login import Page_Login
from Page.get_driver import get_driver



def get_data():
    data_list = []
    with open('./Data/login_data.yaml','r',encoding='utf-8') as f:
        readdata = f.read()
        data = yaml.load(readdata).get("data")
    for i in data:
        for o in i.keys():
            data_list.append((i.get(o).get('uname'),i.get(o).get('pwd')))
    return data_list


class Test_login:
    def setup_class(self):
        self.pl_obj = Page_Login(get_driver())
    def teardown_class(self):
        self.pl_obj.driver.quit()
    def test_1(self):
        self.pl_obj.click_login()
    def test_2(self):
        self.pl_obj.switch_to_frame()
    @pytest.mark.paramtrize("uname pwd",get_data())
    def test_3(self,uname,pwd):
        self.pl_obj.input_name_pwd_login(uname,pwd)
