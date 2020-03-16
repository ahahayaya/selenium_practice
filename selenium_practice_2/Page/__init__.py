from selenium.webdriver.common.by import By
"""
百度首页
"""

#登录链接
login_link_xpath = (By.LINK_TEXT,"登录")
#frame
frmaelabel_tag_name = (By.TAG_NAME,'iframe')
#用户名密码登录
uname_pwd_login_xpath = (By.XPATH,"//*[contains(@title,'用户名密码登录')]")
#输入用户名
input_uname_css_se = (By.CSS_SELECTOR,'#TANGRAM__PSP_10__userName')
#输入密码
input_pwd_css_se = (By.CSS_SELECTOR,'#TANGRAM__PSP_10__password')
#登录
login_btn_xpath = (By.XPATH,"//*[@id='TANGRAM__PSP_10__submit']")
