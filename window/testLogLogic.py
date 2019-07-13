

from __future__ import division
from PyQt5.QtWidgets import QDialog
import testLogWin

from PyQt5.QtCore import *

class testWin(QDialog):
    def __init__(self):
        super().__init__()
        self.testUi=testLogWin.Ui_Dialog()
        self.testUi.setupUi(self)
        self.setWindowTitle('输入账号')
        self.testUi.pushButton.setFocusPolicy(Qt.ClickFocus)
        self.testUi.lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.testUi.pushButton_2.setFocusPolicy(Qt.ClickFocus)
        self.setFocusPolicy(Qt.NoFocus)
        self.testUi.pushButton.clicked.connect(self.testLogwin)  # 按钮事件绑定处理手动输入
        self.user_id=''
        self.s_user_id=''
        self.rangekey=[x for x in range(48,58)]+[x for x in range(65,91)]
    def showTestWin(self):
        self.exec_()
    #手动输入
    def testLogwin(self):
        id=self.testUi.lineEdit.text()
        if id:
            self.user_id=id
            self.testUi.lineEdit.setText('')
        else:
            self.testUi.label_3.setText('用户不存在，请重新输入!!!')
    def keyPressEvent(self, e):
        s=e.key()
        #扫码
        if s in (self.rangekey):
            self.s_user_id += chr(s)
            #print(self.s_user_id)
        elif s==16777217:
            self.user_id=self.s_user_id
            #print('消息输入信息是：', self.user_id)
            self.s_user_id=''
        elif s==16777220:
            self.testLogwin()