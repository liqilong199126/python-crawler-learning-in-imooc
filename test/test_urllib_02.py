# conding:utf8
import urllib.request

url = "http://www.baidu.com"

print('第二种方法')

# 创建一个Request对象
req = urllib.request.Request('http://www.baidu.com')

# 使用Request对象发送请求
req.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib.request.urlopen(req)
print(response2.getcode())
print(len(response2.read()))