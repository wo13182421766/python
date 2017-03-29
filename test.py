#encoding: UTF-8


from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://radar.kuaibo.com')

print(driver.title)

driver.quit()






# import sys
#import webbrowser
# sys.path.append("libs")
#
# url = "http://www.baidu.com"
# webbrowser.open_new(url)
# webbrowser.get()

#"D:\Program Files (x86)\360_brower_4\360se3\360se.exe"
# bPath = r'D:\Program Files (x86)\360_brower_4\360se3\360se.exe'
# webbrowser.register('360', None, webbrowser.BackgroundBrowser(bPath))
# webbrowser.get('360').open_new_tab('http://www.baidu.com')


# import urllib.request
#
# url = "http://www.baidu.com"
# data = urllib.request.urlopen(url)
# data = data.read()
# data = data.decode('UTF-8')
# print(data)





#selenium demo
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
# import time
#
# browser = webdriver.Firefox() # Get local session of firefox
# browser.get("http://www.yahoo.com") # Load page
# assert "Yahoo!" in browser.title
# elem = browser.find_element_by_name("p") # Find the query box
# elem.send_keys("seleniumhq" + Keys.RETURN)
# time.sleep(0.2) # Let the page load, will be added to the API
# try:
#     browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
# except NoSuchElementException:
#     assert 0, "can't find seleniumhq"
# browser.close()
