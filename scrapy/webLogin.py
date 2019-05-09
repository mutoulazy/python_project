import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver import ActionChains

def start_chrome():
    browser = webdriver.Chrome()
    browser.set_window_size(1500, 1500)
    return browser

def login(browser, url):
    # 参考https://www.jianshu.com/p/568689e698d1?utm_source=oschina-app
    browser.get(url)
    # 切换到登陆标签
    # action = browser.find_element_by_xpath("//div[@class='SignContainer-switch']/span")
    # ActionChains(browser).move_to_element(action).click(action).perform()
    # 输入用户名密码
    browser.find_element_by_name("username").send_keys("admin")
    browser.find_element_by_name("password").send_keys("********")
    # 有验证码
    # time.sleep(20)
    # 点击登陆
    browser.find_element_by_xpath("//button[@id='login_but']").click()
    time.sleep(10)

# 填写的位置不固定 
def wirte_worktime():
    pass

if __name__ == "__main__":
    url = "https://www.jianshu.com"
    browser = start_chrome()
    login(browser, url)


