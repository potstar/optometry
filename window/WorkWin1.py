# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WorkWin1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 780)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(500, 30))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_9.setMaximumSize(QtCore.QSize(80, 70))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_10.addWidget(self.pushButton_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.comboBox_7 = QtWidgets.QComboBox(Dialog)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_7)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_7.addWidget(self.lineEdit_5)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_7.addWidget(self.comboBox_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_7.addWidget(self.lineEdit_7)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.line_2 = QtWidgets.QFrame(Dialog)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setMinimumSize(QtCore.QSize(50, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_4)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setMinimumSize(QtCore.QSize(50, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(3, "")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.comboBox_6 = QtWidgets.QComboBox(Dialog)
        self.comboBox_6.setObjectName("comboBox_6")
        self.horizontalLayout_3.addWidget(self.comboBox_6)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_3.addWidget(self.comboBox_5)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_11.addWidget(self.pushButton_7)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_11.addWidget(self.pushButton_5)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_11.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 642, 1500))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 1500))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 530))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_6.addWidget(self.graphicsView)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView_2.setMinimumSize(QtCore.QSize(0, 530))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_6.addWidget(self.graphicsView_2)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView_3.setMinimumSize(QtCore.QSize(0, 530))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_6.addWidget(self.graphicsView_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.groupBox_4)
        self.graphicsView_4.setMinimumSize(QtCore.QSize(0, 500))
        self.graphicsView_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.horizontalLayout_8.addWidget(self.graphicsView_4)
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.groupBox_4)
        self.graphicsView_5.setMinimumSize(QtCore.QSize(0, 500))
        self.graphicsView_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.horizontalLayout_8.addWidget(self.graphicsView_5)
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.groupBox_4)
        self.graphicsView_6.setMinimumSize(QtCore.QSize(0, 500))
        self.graphicsView_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.horizontalLayout_8.addWidget(self.graphicsView_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_9.addWidget(self.pushButton_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5.addWidget(self.groupBox_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "工作人员："))
        self.pushButton_9.setText(_translate("Dialog", "修改密码"))
        self.label_11.setText(_translate("Dialog", "姓名"))
        self.label_9.setText(_translate("Dialog", "性别"))
        self.comboBox_7.setItemText(0, _translate("Dialog", "男"))
        self.comboBox_7.setItemText(1, _translate("Dialog", "女"))
        self.label_13.setText(_translate("Dialog", "年龄"))
        self.label.setText(_translate("Dialog", "省"))
        self.label_4.setText(_translate("Dialog", "城市"))
        self.label_12.setText(_translate("Dialog", "学校"))
        self.pushButton_4.setText(_translate("Dialog", "新建个人档案"))
        self.pushButton_6.setText(_translate("Dialog", "批量添加"))
        self.pushButton_3.setText(_translate("Dialog", "密码重置"))
        self.label_14.setText(_translate("Dialog", "用户ID"))
        self.label_7.setText(_translate("Dialog", "      年龄"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "所有"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "7-10"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "11-15"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "16-20"))
        self.comboBox_4.setItemText(4, _translate("Dialog", "21-25"))
        self.label_6.setText(_translate("Dialog", "    性别"))
        self.comboBox.setItemText(0, _translate("Dialog", "所有"))
        self.comboBox.setItemText(1, _translate("Dialog", "女"))
        self.comboBox.setItemText(2, _translate("Dialog", "男"))
        self.label_10.setText(_translate("Dialog", "    省"))
        self.label_8.setText(_translate("Dialog", "城市"))
        self.label_5.setText(_translate("Dialog", "学校"))
        self.pushButton.setText(_translate("Dialog", "查询"))
        self.pushButton_7.setText(_translate("Dialog", "上一页"))
        self.pushButton_5.setText(_translate("Dialog", "下一页"))
        self.pushButton_2.setText(_translate("Dialog", "导出"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">统计报告</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">1、基本视力情况</span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">2、视力变化情况</span></p></body></html>"))
        self.pushButton_8.setText(_translate("Dialog", "生成报告并打印"))

