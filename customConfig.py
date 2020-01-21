# -*- coding: UTF-8 -*-
import xlrd
import xlwt
from PyQt5 import sip
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from customReceiptsUI import *


class CustomConfig(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.excelFile = r'receiptSetting/批量录入发票模板.xlsx'
        self.book = xlrd.open_workbook(self.excelFile)
        self.rows = 0
        self.cols = 0
        self.name = self.book.sheet_names()[0]
        self.res = QImage('./background/{}.jpg'.format(self.name))
        self.pixScale = self.calcuPixScale()
        self.preview = QPixmap('./background/{}.jpg'.format(self.name)).scaled(self.res.width() * self.pixScale,
                                                                               self.res.height() * self.pixScale)
        # self.value_list = []  可能并不需要value_list这个东西来储存数据
        self.loadSheetNames()
        self.loadReceiptData()
        self.graphicsView.setPixmap(self.preview)
        self.graphicsView.singal.connect(self.label2.setText)
        self.show()

    def loadSheetNames(self):
        _translate = QtCore.QCoreApplication.translate
        sheetName = self.book.sheet_names()
        for sheet in sheetName:
            self.__dict__['action' + str(sheet)] = QtWidgets.QAction(self)
            self.__dict__['action' + str(sheet)].setObjectName("action" + str(sheet))
            self.menuOpen.addAction(self.__dict__['action' + str(sheet)])
            self.__dict__['action' + str(sheet)].setText(_translate("MainWindow", sheet))

    def calcuPixScale(self):
        """
        跳出来一个表单，需要填入名字，背景图片
        有了这两个值以后，先在excel文档中新建一个sheet，名字就是刚刚填入的表单名字
        同时把背景图片复制到background文件夹内，名字改成sheetName.jpg
        :return:
        """
        desktop = QApplication.desktop()
        screenRect = desktop.screenGeometry()
        pixScale = (screenRect.width() * 0.5) / self.res.size().width()  # 将缩放比例设置成 图片宽度 / 屏幕宽度 * 2 ，保证预览图占半屏宽
        return pixScale

    def getPreviewPix(self):
        originWidth, originHeight = self.res.size().width(), self.res.size().height()
        mgnWidth = int(originWidth * self.pixScale)
        mgnHeight = int(originHeight * self.pixScale)  # 缩放宽高尺寸
        size = QSize(mgnWidth, mgnHeight)
        self.previewPix = QPixmap.fromImage(self.res.scaled(size))
        self.previewPix.save(r'.\preview\{}.jpg'.format(self.name))

    def loadReceiptData(self, receiptName=None):
        """
        载入选定的receipt里的值，将value_list里的数据加载到一个表单里，并且将表单呈现在界面上。
        """
        if receiptName is None:
            receiptName = self.name
        table = self.book.sheet_by_name(receiptName)
        self.cols = table.ncols
        self.rows = table.nrows
        for row in range(self.rows):
            for col in range(self.cols):
                #  生成值列表，并填入初始值。要用self.__dict__[<expression>] = Object() 这样的写法来批量生成类内对象，不然的话只是函数内的对象，用完就丢掉找不到了。
                #  如果是在更外面一层可以用Locals()[<expression>]这样的写法
                if row == 0:
                    self.__dict__['lineEdit_' + str(row) + str(col)] = QtWidgets.QLabel(self.frame)
                else:
                    self.__dict__['lineEdit_' + str(row) + str(col)] = QtWidgets.QLineEdit(self.frame)

                self.__dict__['lineEdit_' + str(row) + str(col)].setMaximumSize(QtCore.QSize(40, 20))
                self.__dict__['lineEdit_' + str(row) + str(col)].setObjectName("lineEdit_" + str(row) + str(col))
                self.__dict__['lineEdit_' + str(row) + str(col)].setText(str(table.row_values(row)[col]))
                self.gridLayout.addWidget(self.__dict__['lineEdit_' + str(row) + str(col)], row, col, 1, 1)

            # 每一行生成一个 - 按键，用来删除本行。第一行生成一个New按键，用来生成新行
            _translate = QtCore.QCoreApplication.translate

            self.__dict__['label_' + str(row)] = QtWidgets.QLabel(self.frame)
            self.__dict__['label_' + str(row)].setMaximumSize(QtCore.QSize(40, 16777215))
            self.__dict__['label_' + str(row)].setObjectName("label_" + str(row))
            self.gridLayout.addWidget(self.__dict__['label_' + str(row)], row, self.cols, 1, 1)
            self.__dict__['label_' + str(row)].setText(_translate("MainWindow", str(row)))

            self.__dict__['pushButton_' + str(row)] = QtWidgets.QPushButton(self.frame)
            self.__dict__['pushButton_' + str(row)].setMaximumSize(QtCore.QSize(40, 16777215))
            self.__dict__['pushButton_' + str(row)].setObjectName("pushButton_" + str(row))
            self.gridLayout.addWidget(self.__dict__['pushButton_' + str(row)], row, self.cols + 1, 1, 1)
            if row == 0:
                self.__dict__['pushButton_' + str(row)].setText(_translate("MainWindow", "new"))
                self.__dict__['pushButton_' + str(row)].clicked.connect(self.newCol)
            else:
                self.__dict__['pushButton_' + str(row)].setText(_translate("MainWindow", "-"))
                self.__dict__['pushButton_' + str(row)].clicked.connect(self.removeCol)

    def removeCol(self):
        # 通过分析按键名字，来判断要删掉第几行
        sender = self.sender()
        r = sender.objectName()
        currentRow = r.replace('pushButton_', '')
        # 从当前行开始，将每个lineEdit控件的值替换成下一行对应控件的值
        if int(currentRow) < self.rows - 1:
            for row in range(int(currentRow), self.rows - 1):
                for col in range(self.cols):
                    self.__dict__['lineEdit_' + str(row) + str(col)].setText(
                        self.__dict__['lineEdit_' + str(row + 1) + str(col)].text())
        # 然后删除最后一行
        for col in range(0, self.cols)[::-1]:
            self.gridLayout.removeWidget(self.__dict__['lineEdit_' + str(self.rows - 1) + str(col)])
            sip.delete(self.__dict__['lineEdit_' + str(self.rows - 1) + str(col)])
        self.gridLayout.removeWidget(self.__dict__['label_' + str(self.rows - 1)])
        sip.delete(self.__dict__['label_' + str(self.rows - 1)])
        self.gridLayout.removeWidget(self.__dict__['pushButton_' + str(self.rows - 1)])
        sip.delete(self.__dict__['pushButton_' + str(self.rows - 1)])
        # 总行数减1
        self.rows -= 1
        self.show()

    def newCol(self):
        row = self.rows
        for col in range(self.cols):
            #  生成值列表，并填入初始值
            self.__dict__['lineEdit_' + str(row) + str(col)] = QtWidgets.QLineEdit(self.frame)
            self.__dict__['lineEdit_' + str(row) + str(col)].setMaximumSize(QtCore.QSize(40, 20))
            self.__dict__['lineEdit_' + str(row) + str(col)].setObjectName("lineEdit_" + str(row) + str(col))
            self.__dict__['lineEdit_' + str(row) + str(col)].setText('')
            self.gridLayout.addWidget(self.__dict__['lineEdit_' + str(row) + str(col)], row, col, 1, 1)

        _translate = QtCore.QCoreApplication.translate

        self.__dict__['label_' + str(row)] = QtWidgets.QLabel(self.frame)
        self.__dict__['label_' + str(row)].setMaximumSize(QtCore.QSize(40, 16777215))
        self.__dict__['label_' + str(row)].setObjectName("label_" + str(row))
        self.gridLayout.addWidget(self.__dict__['label_' + str(row)], row, self.cols, 1, 1)
        self.__dict__['label_' + str(row)].setText(_translate("MainWindow", str(row)))

        self.__dict__['pushButton_' + str(row)] = QtWidgets.QPushButton(self.frame)
        self.__dict__['pushButton_' + str(row)].setMaximumSize(QtCore.QSize(40, 16777215))
        self.__dict__['pushButton_' + str(row)].setObjectName("pushButton_" + str(row))
        self.gridLayout.addWidget(self.__dict__['pushButton_' + str(row)], row, self.cols + 1, 1, 1)
        self.__dict__['pushButton_' + str(row)].setText(_translate("MainWindow", "-"))
        self.__dict__['pushButton_' + str(row)].clicked.connect(self.removeCol)
        self.rows += 1
        self.show()

    def saveReceipt(self):
        """
        将临时表单里的值加载到对应receipt的设置里，也就是写到excel里去
        :return:
        """
        workbook = xlwt.Workbook(self.excelFile)
        table = workbook.add_sheet(self.name)
        for col in range(self.cols):
            for row in range(self.rows):
                text = self.__dict__['lineEdit_' + str(row) + str(col)].toPlainText()
                table.write(col, row, text)
        workbook.save(self.excelFile)

    def click2XY(self, event):
        """
        e是鼠标动作
        i是当前workReceipt里的value_list里的序列值,i值用别的办法传进去
        启动后监控鼠标在图片上的xy值，双击后跳出确认界面，确认后
        将xy值写入到value_list[i]里的对应部分
        :return:
        """
        if event.buttons() == Qt.LeftButton:
            s = event.pos()
            self.setMouseTracking(True)
            self.label2.setText('X:' + str(s.x()) + '  ' + 'Y:' + str(s.y()))

    def chosePix(self):
        """
        按下按键以后选择文件，然后将选定的文件路径加载到图片的textLine
        """
        pass

    def default(self):
        """
        将value_list[i]重新加载，等于是把所有变动都重置了
        """
        pass


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("CustomConfig")
    window = CustomConfig()
    app.exec_()
