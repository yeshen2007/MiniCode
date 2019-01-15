"""
开发环境：python3.7.1+windows
IDE:pycharm
第三方库PIL：安装pillow
"""
from PIL import Image

# 思路，用不同的字符去代表不同的灰度区间
chars = '"$%_&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-/+@<>i!;:,\^`.'
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
fb = open('img.txt', 'w')
temp = ''
for j in range(height):
    for i in range(width):
        r, g, b = img.getpixel((i, j))
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        char = chars[int(gray / 256.0 * len(chars))]
        temp += char
    temp += '\n'
fb.write(temp)
