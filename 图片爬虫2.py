import requests
from pyquery import PyQuery

photo = []
num = 3538

def onepage(one_url, oneflag):
    response = requests.get(url=one_url)
    if response.status_code != 200:
        return False
    #print(response.text)
    doc = PyQuery(response.text)
    title = doc('title').text()
    print(title)
    desc = doc('head > meta:nth-child(6)').attr('content')
    print(desc)

    imglist = doc('#main > article > div > p a')
    #print(imglist)
    for dd in imglist.items():
        photo.append(dd.attr('href'))
#        print(dd.attr('href'))

    if oneflag == True:
        with open(r'G:\Python\test\图片爬虫\photo3\说明.txt', encoding='utf-8', mode='a+') as f1:
            f1.write(title+'\n')
        page = doc('#main > article > div > div.page-links a')
        for i in page.items():
            with open(r'G:\Python\test\图片爬虫\photo3\说明.txt', encoding='utf-8', mode='a+') as f1:
                f1.write(i.attr('href')+'\n')
            print(i.attr('href'))
            onepage(i.attr('href'), False)
        with open(r'G:\Python\test\图片爬虫\photo3\说明.txt', encoding='utf-8', mode='a+') as f1:
            f1.write('\n\n\n')


for j in range(143, 1000):
    url = 'https://chottie.com/blog/archives/'+str(j)
    photo = []
    if onepage(url, True)==False:
        continue
    print(j)
    print(photo)
    for i in photo:
        a = requests.get(i)
        with open(r'G:\Python\test\图片爬虫\photo3\{}-{}.jpg'.format(j, num), 'wb') as f2:
            f2.write(a.content)
        num += 1





