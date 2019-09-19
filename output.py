# -*- coding: UTF-8 -*-
from models import Receipts
import xlrd

options = {'1': '付款申请单', '2': '旅游团款结算单'}
for key in options:
    print(key, options[key])


def input_type(option):
    keys = option.keys()
    while True:
        choice = input('请输入要打印的单据类型编号: ')
        if choice in keys:
            break
        else:
            print('输入错误，请重新输入。')
    return options[choice]


outType = input_type(options)
background = r'.\background\{}扫描件.jpg'.format(outType)
file = r'.\receiptSetting\批量录入发票模板.xlsx'
datafile = r'.\receiptsData\{}数据.xlsx'.format(outType)
user = input('请输入你的名字： ')

while True:
    confirm = input('开始打印前,先确认{}里的数据是否已更新。 y/n? : '.format(datafile))

    if confirm == 'y' or confirm == 'Y':
        workbook = xlrd.open_workbook(datafile)
        index = workbook.sheet_names()[0]
        table = workbook.sheet_by_name(index)
        rows = table.nrows
        for i in range(1, rows):
            receipt = Receipts(background=background, title=outType, file=file, sheet=outType)
            receipt.load_data(datafile, i)
            for value in receipt.value_list:
                try:
                    output = receipt.add_text_to_image(value)
                except Exception:
                    pass
            filename = r'./output/' + user + outType + str(i) + '.png'
            output.save(filename)
            print('第{}张图片输出成功'.format(i))

        print('所有图片输出成功，请去output文件夹下查看图片。')
        exit()

    else:
        print('请更新数据后再运行程序。')
