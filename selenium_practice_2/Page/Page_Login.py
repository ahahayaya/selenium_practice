from Base.Base import Base
import Page
class Page_Login(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    def click_login(self):
        self.click_element(Page.login_btn_xpath)
    def switch_to_frame(self,frame1=Page.frmaelabel_tag_name):
        e = self.search_element(frame1)
        self.driver.switch_to.frame(e)
    def input_name_pwd_login(self,name,pwd):
        self.input_element(self,Page.input_uname_css_se,name)
        self.input_element(self,Page.input_pwd_css_se,pwd)
        self.click_element(self,Page.login_btn_xpath)


