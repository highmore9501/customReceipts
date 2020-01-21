# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'originalUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
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
            self.message = """鼠标坐标为：QPoint({0}, {1}) """.format(event.pos().x(), event.pos().y())
            self.emitSignal()

    '''重新实现鼠标双击事件'''

    def mouseDoubleClickEvent(self, event):
        self.justDoubleClicked = True
        self.message = "你双击了鼠标"
        self.emitSignal()

    def emitSignal(self):
        self.singal.emit(self.message)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(468, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.graphicsView = MouseQLabel(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 521, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuoption = QtWidgets.QMenu(self.menubar)
        self.menuoption.setObjectName("menuoption")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionconfigFile = QtWidgets.QAction(MainWindow)
        self.actionconfigFile.setObjectName("actionconfigFile")
        self.actiondefaultFont = QtWidgets.QAction(MainWindow)
        self.actiondefaultFont.setObjectName("actiondefaultFont")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.menuOpen.addSeparator()
        self.menuOpen.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuoption.addAction(self.actionconfigFile)
        self.menuoption.addAction(self.actiondefaultFont)
        self.menuhelp.addAction(self.actionabout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuoption.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label3.setText(_translate("MainWindow", "图片路径"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label2.setText(_translate("MainWindow", "当前坐标"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuoption.setTitle(_translate("MainWindow", "option"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionconfigFile.setText(_translate("MainWindow", "configFile"))
        self.actiondefaultFont.setText(_translate("MainWindow", "defaultFont"))
        self.actionabout.setText(_translate("MainWindow", "about"))
