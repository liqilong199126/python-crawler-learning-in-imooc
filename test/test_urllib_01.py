# conding:utf8
# 引入urllib下的request模块
import urllib.request

url = "http://www.baidu.com"

print('第一种方法')

# 使用urlopen发送请求，并获得响应

response1 = urllib.request.urlopen('http://www.baidu.com')
print(response1.getcode())
print(len(response1.read()))

