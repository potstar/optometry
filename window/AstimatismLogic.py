'''
文件：Astimatismlogic.py 散光测试逻辑
作者：potstar
版权：
日期：2019.1.28
'''
import astimatism
import os
import messagelogic
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
import time

class AstimatismWindow(QDialog):
    astiTeleSignal=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.testNum1=1
        self.astimatism_ui = astimatism.Ui_Dialog()
        self.astimatism_ui.setupUi(self)
        self.astimatism_ui.pushButton_4.clicked.connect(self.astimatismSlotY)
        self.astimatism_ui.pushButton_3.clicked.connect(self.astimatismSlotN)
        #self.picture_asti = TestPicture()

        self.anti_ms = messagelogic.MessageWindow()
        #self.selectButtons=[self.astimatism_ui.pushButton_4,self.astimatism_ui.pushButton_3]
        #self.selectedButton=self.astimatism_ui.pushButton_4
        #self.selects=['yes','no']
        #self.selected='yes'
        #self.anti_ms.m_ui.pushButton.clicked.connect(self.anti_ms.close)

        self.filename='anti.png'

        self.testObject='右'
        self.rightAsti = ''
        self.leftAsti = ''

    def astimatismSlotY(self):
        self.astiGrad='无散光'
        self.messageTip()

    def astimatismSlotN(self):
        self.astiGrad = '可能存在散光'
        self.messageTip()

    def messageTip(self):
        if self.testObject!='左':
            self.testObject='左'
            self.rightAsti=self.astiGrad
            self.astiTeleSignal.emit('sight_stop')
            self.astiTeleSignal.emit('message_start')
            self.anti_ms.initUi('开始左眼散光测试!!!')
            self.astiTeleSignal.emit('message_stop')
            self.astiTeleSignal.emit('sight_start')
            self.astimatism_ui.label_5.setText(
                '<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">左眼</span></p></body></html>')
        else:
            self.leftAsti=self.astiGrad
            self.astiTeleSignal.emit('sight_stop')
            self.astiTeleSignal.emit('message_start')
            self.anti_ms.initUi('散光测试结束!!!')
            self.astiTeleSignal.emit('message_stop')
            self.testData()
            time.sleep(0.5)
            self.close()
    def initUi(self):
        self.astiTeleSignal.emit('sight_start')
        self.showMaximized()
        self.exec_()
        self.astiTeleSignal.emit('sight_stop')
    def astiTeleControl(self,connect):
        if connect=='009f0e' or connect=='009f02':
            self.astimatismSlotY()
        elif connect=='009f06' or connect=='00':
            self.astimatismSlotN()
    def testData(self):
        #print(self.rightAsti)
        self.astiTeleSignal.emit(self.leftAsti+'_'+self.rightAsti+'_avalue')

