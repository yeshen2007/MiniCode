import requests
from pyquery import PyQuery

# 目标地址
chapter1_url = 'http://www.biquyun.com/14_14055/9194140.html'


def get_one_chapter(chapter_url):
    # 获取一章内容
    # 使用requests工具 发送请求
    response = requests.get(url=chapter_url)

    # 万能的解决编码问题：用内容中的编码来解析
    response.encoding = response.apparent_encoding
    # print(response.text)

    # 把文字变成网页格式
    doc = PyQuery(response.text)
    title = doc("h1").text()
    print(title)
    content = doc('#content').text()
    print(content)
    with open(file='三寸人间.txt', encoding='utf-8', mode="a+") as f:
        f.write(title + '\n' + content + '\n\n\n')


# 书本目录
index_url = 'http://www.biquyun.com/14_14055/'
response = requests.get(url=index_url)
response.encoding = response.apparent_encoding
doc = PyQuery(response.text)
list_dd = doc('#list > dl > dd a')
for dd in list_dd.items():
    get_one_chapter('http://www.biquyun.com'+dd.attr('href'))
