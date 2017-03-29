# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

dr = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('level_locate.html')
dr.get(file_path)

#点击Link1链接（弹出下拉列表）
dr.find_element_by_link_text('Link1').click()

#找到id 为dropdown1的父元素
WebDriverWait(dr, 10).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())
#WebDriverWait(dr, 10) 10秒内 每500ms 扫描一次页面变化。直到 lambda 定义的元素出现
#is_displayed() 该元素用户可以见

#在父亲元件下找到link为Action的子元素
menu = dr.find_element_by_id('dropdown1').find_element_by_link_text('Action')

#鼠标定位到子元素上
webdriver.ActionChains(dr).move_to_element(menu).perform()
#ActionChains 生成用户的行为，所有的行为都存放在 actionChains 对象中
#通过 perform() 执行
#move_to_element 鼠标移动到指定元素



time.sleep(2)





