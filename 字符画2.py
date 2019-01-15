"""
开发环境：python3.7.1+windows
IDE:pycharm
第三方库PIL：安装pillow
"""
from PIL import Image

img = Image.open('test.jpg')
# print(img.format)
# print(img.mode)
# print(img.size)

width, height = img.size
if width > 100:
    n = width // 100
else:
    n = 1
width = width // n
height = height // n // 2
img = img.resize((width, height))

# 写一个尺寸与图片一致的文档
fb = open('img.html', 'w')
html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{}
</body>
</html>'''
temp = ''
for j in range(height):
    for i in range(width):
        r, g, b = img.getpixel((i, j))
        temp += '<font color="#%02s%02s%02s">8</font>' % (hex(r)[2:], hex(g)[2:], hex(b)[2:])
    temp += '<br>'
fb.write(html.format(temp))
