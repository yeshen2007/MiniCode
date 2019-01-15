"""
1.URL
2.模拟浏览器请求资源
3.解析网页
4.保存数据到本地
"""
import requests   #第三方库
import urllib.parse
import json
import jsonpath

url ='https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}'
label = '校花'
label = urllib.parse.quote(label)
#print(label)
num = 0

for index in range(0, 2400, 24):
    u = url.format(label, index)
    we_data = requests.get(u).text
#    print(we_data)
    html = json.loads(we_data)
    photo = jsonpath.jsonpath(html, "$..path")
    print(photo)
    for i in photo:
        a = requests.get(i)
        with open(r'G:\Python\test\图片爬虫\photo\{}.jpg'.format(num), 'wb') as f:
            f.write(a.content)
        num += 1


