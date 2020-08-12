from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal
import settings
import os

class settingWin(QDialog):
    teleSignal1 = pyqtSignal(str)
    def __init__(self,path,config):
        super().__init__()
        # 遥控信号常量值
        self.right = config.RIGHT
        self.left = config.LEFT
        self.ok = config.OK

        self.settingUi=settings.Ui_Dialog()
        self.settingUi.setupUi(self)
        self.setWindowTitle('设置')
        self.sightpath=path
        self.settingsNow()
        self.Buttons = [self.settingUi.pushButton_2,self.settingUi.pushButton]
        self.Selects = ['3', '5']
        self.settingUi.pushButton.clicked.connect(self.settingDone5)
        self.settingUi.pushButton_2.clicked.connect(self.settingDone3)
    def initUI(self):
        self.teleSignal1.emit('sight_start')
        self.exec_()
        self.teleSignal1.emit('sight_stop')
    def settingsNow(self):
        if 'sight3' in self.sightpath:
            self.selected='3'
            self.Button = self.settingUi.pushButton_2
            self.settingUi.pushButton_2.setStyleSheet('background-color:yellow')
        else:
            self.selected='5'
            self.Button = self.settingUi.pushButton
            self.settingUi.pushButton.setStyleSheet('background-color:yellow')
    def settingDone3(self):
        self.selected='3'
        self.saveSetting()
    def settingDone5(self):
        self.selected='5'
        self.saveSetting()
    def saveSetting(self):
        if self.selected == '3':
            basePath = os.getcwd()
            self.sightpath = basePath + '\sight3_setting'
            self.teleSignal1.emit(self.sightpath)
            self.close()
        elif self.selected == '5':
            basePath = os.getcwd()
            self.sightpath = basePath + '\sight5_setting'
            self.teleSignal1.emit(self.sightpath)
            self.close()
    def teleControl(self,connect):
        if self.right in connect:
            self.Button.setStyleSheet('')
            index=self.Selects.index(self.selected)+1
            if index>1:
                index=0
            self.Button=self.Buttons[index]
            self.selected = self.Selects[index]
            self.Button.setStyleSheet('background-color:yellow')
        elif self.left in connect:
            self.Button.setStyleSheet('')
            index = self.Selects.index(self.selected) - 1
            if index <0:
                index = 0
            self.Button = self.Buttons[index]
            self.selected = self.Selects[index]
            self.Button.setStyleSheet('background-color:yellow')
        elif self.ok==connect:
            self.saveSetting()
