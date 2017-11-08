# conding:utf8
# 引入urllib下的request模块
import urllib.request
import http.cookiejar

url = "http://www.baidu.com"

print('第三种方法')

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(len(response3.read()))
print(cj)