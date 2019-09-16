# -*- coding: UTF-8 -*-
from models import Template
import xlrd


name = '输出测试图片'
background = r'.\background\付款申请单扫描件.jpg'
file = r'.\receiptSetting\批量录入发票模板.xlsx'
datafile = r'.\receiptsData\付款申请单数据.xlsx'

workbook = xlrd.open_workbook(datafile)
index = workbook.sheet_names()[0]
table = workbook.sheet_by_name(index)
rows = table.nrows

for i in range(1, rows):
    template = Template(background=background, title=name, file=file)
    template.load_data(datafile, i)
    for value in template.value_list:
        try:
            output = template.add_text_to_image(value)
        except Exception:
            pass
    filename = r'./output/' + name + str(i) + '.png'
    output.save(filename)
