#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_xpath("//form[@id='form' and @class='fm']/span/input[@id='kw']").send_keys('nh')

driver.find_element_by_xpath("//form[@id='form']/span[2]/input")


#driver.find_element_by_link_text(u'新闻').click()
#driver.find_element_by_xpath("//input[@id='kw']").send_keys('hh')
# inputs = driver.find_elements_by_tag_name('input')
# for i in inputs:
#     if i.get_attribute('autocomplete') == 'off':
#         i.send_keys('zh')

print(driver.title)
