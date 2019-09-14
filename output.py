# -*- coding: UTF-8 -*-
from models import Template
from PIL import Image
from PIL import PSDraw
import xlrd

"""
1.选定模板
2.确定位置（这一步可以改成从excel中读取位置坐标）
3.选定excel文件，从中批量读取值（包括坐标，值，字体，大小）
4.生成Word实例，打印在模板上
5.输出图片
"""

name = '输出测试图片'
background = r'F:\图片\付款申请单扫描件.jpg'
file = r'F:\图片\朱诚文作品\发票申请模板.xlsx'
datafile = r'E:\My Documents\付款申请单数据.xlsx'
template = Template(background=background, title=name, file=file)
template.load_data(datafile)

for value in template.value_list:
    try:
        template.add_text_to_image(value)
    except Exception:
        pass

template.background.save(name)
