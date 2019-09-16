# -*- coding: utf-8 -*-
# 一,  创建图片并在图上添加文本

from PIL import Image, ImageDraw, ImageFont

a = '我们不一样'  # 定义文本
font = ImageFont.truetype(r'%windir%\Fonts\Deng.ttf', 24)  # 定义字体，这是本地自己下载的
img = Image.new('RGB', (300, 300), (255, 180, 0))  # 新建长宽300像素，背景色为（255,180,0）的画布对象
draw = ImageDraw.Draw(img)  # 新建画布绘画对象
draw.text((50, 50), a, (255, 0, 0), font=font)  # 在新建的对象 上坐标（50,50）处开始画出红色文本
# 左上角为画布坐标（0,0）点
img.save('./img.jpeg')
