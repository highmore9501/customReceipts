# -*- coding: UTF-8 -*-
from PIL import Image, ImageDraw, ImageFont
import xlrd


class Template(object):
    """
    此类定义要打印的表单背景，以及初始化需要打印的值
    初始化时从将指定的xlsx文件中读取设置，生成一个包含列表的列表，包含表单中所有的字段名称，值，字体，大小，位置
    每个被包含的列表，所含的值按顺序分别是text,font,size,x,y,name
    所以当这些值要被打印的时候，按顺序调用text,font,size,x,y就可以了
    """

    def __init__(self, background, title, file, sheet=None):
        self.background = Image.open(background)
        self.title = title
        self.value_list = []
        self.default_font = ImageFont.truetype(r'%windir%\Fonts\Deng.ttf', 36)
        workbook = xlrd.open_workbook(file)
        index = sheet
        if sheet is None:
            index = workbook.sheet_names()[0]
        table = workbook.sheet_by_name(index)
        rows = table.nrows
        for i in range(1, rows):
            self.value_list.append(table.row_values(i))

    def load_data(self, data, row):
        workbook = xlrd.open_workbook(data)
        index = workbook.sheet_names()[0]
        table = workbook.sheet_by_name(index)
        cols = table.ncols
        if len(self.value_list) != cols:
            print('数据数量与配置不匹配，请检查配置文件或者数据文件')
            exit()
        for i in range(1, cols):
            self.value_list[i][0] = table.row_values(row)[i]

    def add_text_to_image(self, value):

        if isinstance(value[0], float) and value[5] == '金额':
            text = "%.2f" % value[0]
        else:
            text = value[0]

        if value[1] == '' or value[2] == '':
            custom_font = self.default_font
        else:
            custom_font = ImageFont.truetype(value[1], value[2])

        x = int(value[3])
        y = int(value[4])
        image = self.background.convert('RGBA')
        text_overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
        image_draw = ImageDraw.Draw(text_overlay)
        # 设置文本文字位置
        text_xy = (x, y)
        # 设置文本颜色
        image_draw.text(text_xy, text, (0, 0, 0), font=custom_font)
        image_with_text = Image.alpha_composite(image, text_overlay)
        self.background = image_with_text
        return self.background

