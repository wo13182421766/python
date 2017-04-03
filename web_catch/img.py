from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get('http://www.mzitu.com')
print(u'已经进入' + driver.title)

#driver.find_element_by_xpath("//div[@class='header']/div/span/form/input[@name='s']").send_keys(u'zh')
driver.find_element_by_css_selector('div.header>div>span>form>input').send_keys(u'zh')
driver.maximize_window()
driver.find_element_by_css_selector('span.search > form > button').click()
driver.find_element_by_xpath("//div[@class='postlist']/ul/li[21]/a").click()

#img = driver.find_element_by_css_selector("div.main-image > p > a > img")
#img = driver.find_element_by_xpath("//div[@class='main-image']/p/a/img")
img = driver.find_element_by_css_selector('div.main-image>p>a>img')
print(img.get_attribute('src'))
