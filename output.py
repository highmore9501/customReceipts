# -*- coding: UTF-8 -*-
from models import Template
import xlrd

outType = r'旅游团款结算单'
user = '温小荣'
background = r'.\background\{}扫描件.jpg'.format(outType)
file = r'.\receiptSetting\批量录入发票模板.xlsx'
datafile = r'.\receiptsData\{}数据.xlsx'.format(outType)

workbook = xlrd.open_workbook(datafile)
index = workbook.sheet_names()[0]
table = workbook.sheet_by_name(index)
rows = table.nrows

for i in range(1, rows):
    template = Template(background=background, title=outType, file=file, sheet=outType)
    template.load_data(datafile, i)
    for value in template.value_list:
        try:
            output = template.add_text_to_image(value)
        except Exception:
            pass
    filename = r'./output/' + user + outType + str(i) + '.png'
    output.save(filename)
