# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(564, 428)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 10, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.startbutton = QtWidgets.QPushButton(Dialog)
        self.startbutton.setGeometry(QtCore.QRect(240, 60, 93, 28))
        self.startbutton.setAcceptDrops(False)
        self.startbutton.setObjectName("startbutton")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(150, 60, 61, 31))
        self.spinBox.setMaximum(50)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(370, 60, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(30, 110, 256, 192))
        self.listView.setObjectName("listView")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 330, 201, 61))
        self.label_3.setObjectName("label_3")
        self.analysisbutton = QtWidgets.QPushButton(Dialog)
        self.analysisbutton.setGeometry(QtCore.QRect(300, 350, 93, 28))
        self.analysisbutton.setObjectName("analysisbutton")

        self.retranslateUi(Dialog)
        self.startbutton.clicked.connect(self.listView.update)
        self.startbutton.clicked.connect(self.progressBar.update)
        self.listView.clicked['QModelIndex'].connect(self.analysisbutton.showNormal)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "神经网络感情分析"))
        self.label.setText(_translate("Dialog", "是否开始爬虫抓取图片"))
        self.startbutton.setText(_translate("Dialog", "开始"))
        self.label_2.setText(_translate("Dialog", "请选择数量"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">选择分析的图片</span></p></body></html>"))
        self.analysisbutton.setText(_translate("Dialog", "分析"))
