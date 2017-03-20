#encoding: UTF-8


# import sys
import webbrowser
# sys.path.append("libs")
#
# url = "http://www.baidu.com"
# webbrowser.open_new(url)
# webbrowser.get()

#"D:\Program Files (x86)\360_brower_4\360se3\360se.exe"
bPath = r'D:\Program Files (x86)\360_brower_4\360se3\360se.exe'
webbrowser.register('360', None, webbrowser.BackgroundBrowser(bPath))
webbrowser.get('360').open_new_tab('http://www.baidu.com')



# import urllib.request
#
# url = "http://www.baidu.com"
# data = urllib.request.urlopen(url)
# data = data.read()
# data = data.decode('UTF-8')
# print(data)
