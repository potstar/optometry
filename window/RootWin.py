# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RootWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(795, 904)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setMinimumSize(QtCore.QSize(250, 500))
        self.listView.setMaximumSize(QtCore.QSize(350, 16777215))
        self.listView.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.listView.setObjectName("listView")
        self.verticalLayout_5.addWidget(self.listView)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        self.label_5.setMaximumSize(QtCore.QSize(70, 30))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(11)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(500, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_7.addWidget(self.lineEdit_3)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_7.addWidget(self.lineEdit_5)
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
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_8.addWidget(self.lineEdit_7)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.label_16)
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_2)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_8.addWidget(self.comboBox_3)
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_8.addWidget(self.pushButton_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 300))
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_10.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_10.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_10.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_10.addWidget(self.pushButton_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_3.addWidget(self.graphicsView_2)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_3.addWidget(self.graphicsView_3)
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_3.addWidget(self.graphicsView)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "视力检测"))
        self.label_6.setText(_translate("Dialog", "用户：超级管理员"))
        self.label_7.setText(_translate("Dialog", "工作人员管理"))
        self.label_5.setText(_translate("Dialog", "用户名："))
        self.pushButton_2.setText(_translate("Dialog", "删除人员"))
        self.pushButton.setText(_translate("Dialog", "添加人员"))
        self.pushButton_10.setText(_translate("Dialog", "重置密码"))
        self.label_2.setText(_translate("Dialog", "学生管理"))
        self.label_11.setText(_translate("Dialog", "姓名(必填)"))
        self.label_12.setText(_translate("Dialog", "性别"))
        self.label_13.setText(_translate("Dialog", "年龄"))
        self.label_14.setText(_translate("Dialog", "学校"))
        self.pushButton_4.setText(_translate("Dialog", "新建用户档案并生成条码"))
        self.pushButton_3.setText(_translate("Dialog", "密码重置"))
        self.label_4.setText(_translate("Dialog", "用户ID"))
        self.label_16.setText(_translate("Dialog", "年龄"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "所有"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "7-10"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "11-15"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "16-20"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "21-25"))
        self.label_15.setText(_translate("Dialog", "性别"))
        self.comboBox.setItemText(0, _translate("Dialog", "所有"))
        self.comboBox.setItemText(1, _translate("Dialog", "男"))
        self.comboBox.setItemText(2, _translate("Dialog", "女"))
        self.label_17.setText(_translate("Dialog", "学校"))
        self.pushButton_9.setText(_translate("Dialog", "查询"))
        self.pushButton_8.setText(_translate("Dialog", "上一页"))
        self.pushButton_7.setText(_translate("Dialog", "下一页"))
        self.pushButton_6.setText(_translate("Dialog", "删除"))
        self.pushButton_5.setText(_translate("Dialog", "导出"))

