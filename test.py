# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'originalUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MouseQLabel(QLabel):

    singal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.justDoubleClicked = False
        self.message = ""

    '''重新实现鼠标释放事件'''

    def mouseReleaseEvent(self, event):
        # 若鼠标释放为双击释放，则不跟踪鼠标移动
        # 若鼠标释放为单击释放，则需要改变跟踪功能的状态，如果开启跟踪功能的话就跟踪，不开启跟踪功能就不跟踪
        if self.justDoubleClicked:
            self.justDoubleClicked = False
        else:
            self.setMouseTracking(not self.hasMouseTracking())  # 单击鼠标
            if self.hasMouseTracking():
                self.message = "开启鼠标跟踪功能.\n" + \
                            "请移动一下鼠标！\n" + \
                            "单击鼠标可以关闭这个功能"
            else:
                self.message = "关闭鼠标跟踪功能.\n" + \
                            "单击鼠标可以开启这个功能"
            self.emitSignal()

    '''重新实现鼠标移动事件'''

    def mouseMoveEvent(self, event):
        if not self.justDoubleClicked:
            globalPos = self.mapToGlobal(event.pos())  # 窗口坐标转换为屏幕坐标
            self.message = """鼠标位置：
            窗口坐标为：QPoint({0}, {1}) 
            屏幕坐标为：QPoint({2}, {3}) """.format(event.pos().x(), event.pos().y(), globalPos.x(), globalPos.y())
            self.emitSignal()

    '''重新实现鼠标双击事件'''

    def mouseDoubleClickEvent(self, event):
        self.justDoubleClicked = True
        self.message = "你双击了鼠标"
        self.emitSignal()

    def emitSignal(self):
        self.singal.emit(self.message)
