# -*- coding: UTF-8 -*-

configExcelFile = r'.\receiptSetting\批量录入发票模板.xlsx'


class CustomConfig(object):

    def __init__(self, file=configExcelFile):
        self.x = 0
        self.y = 0
        pass

    def read(self, column):
        pass

    def write(self, column):
        pass

    def click(self):
        return self.x, self.y
