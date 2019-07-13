'''
文件：suitablelogic.py 适配测试逻辑
作者：potstar
版权：
日期：2019.1.27
'''
import sys
import os
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5 import QtCore
import sightable
import messagelogic
import random
import json
import dateserverse
import PyQt5.QtGui as Gui
from PyQt5.QtCore import *
import threading

class WinQdialog(QDialog):
    sightSignal =pyqtSignal(str)
    #sightTeleSignal=QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.s=''
        self.i=0
        self.rangekey = [x for x in range(48, 58)] + [x for x in range(65, 91)]
    def keyPressEvent(self, e):
        keys=e.key()
        if keys in self.rangekey:
            self.s += chr(e.key())
        elif  keys==16777217:
            self.i+=1
            print('视力输入信息是sight：', self.s)
            self.sightSignal1.emit(self.s)
            self.s = ''


class SightWindow(QtCore.QThread,QDialog):
    teleSignal1 = pyqtSignal(str)
    def __init__(self,path):
        super(SightWindow,self).__init__()

        #self.user = user[0]  # 用户
        self.testNum = 0  # 测试图数
        self.buttonValue = ''
        self.preDirect = ''
        self.wrong = 0  # 错误次数
        self.testObject = '右'  # 测试对象
        self.message = True
        #self.messageEnd = False
        self.sight_ms=messagelogic.MessageWindow()
        #self.sight_ms.m_ui.pushButton.clicked.connect(self.sight_ms.close)

        self.form_sight = WinQdialog() # 窗口初始化
        self.sight_ui = sightable.Ui_Dialog()
        self.sight_ui.setupUi(self.form_sight)

        # 绑定事件
        self.sight_ui.pushButton.clicked.connect(self.sightRightSlot)
        self.sight_ui.pushButton_2.clicked.connect(self.sightUpSlot)
        self.sight_ui.pushButton_4.clicked.connect(self.sightDownSlot)
        self.sight_ui.pushButton_3.clicked.connect(self.sightLeftSlot)

        self.sight_ui.pushButton.setFocusPolicy(Qt.ClickFocus)
        self.sight_ui.listView.setFocusPolicy(Qt.ClickFocus)
        self.sight_ui.pushButton_2.setFocusPolicy(Qt.ClickFocus)
        self.sight_ui.pushButton_4.setFocusPolicy(Qt.ClickFocus)
        self.sight_ui.pushButton_3.setFocusPolicy(Qt.ClickFocus)
        self.sightButtons=[self.sight_ui.pushButton_2,self.sight_ui.pushButton_4,self.sight_ui.pushButton_3,self.sight_ui.pushButton]
        self.sightedButton=self.sight_ui.pushButton_2
        self.sightSelects=['up','down','left','right']
        self.sightselected='up'
        self.picture = TestPicture(path)
        self.testGrad = 4.5
        self.testGradLeft = 0
        self.testGradRight = 0

        self.form_sight.sightSignal.connect(self.setList)
        self.slm=QStringListModel()
        self.qlist=[]
        self.idlist=[]
        #self.tele_flag=True
        #self.initUi()
    def initUi(self):
        #self.sight_ui.pushButton_2.setStyleSheet('background-color:yellow')
        self.form_sight.setWindowIcon(Gui.QIcon('favicon.png'))
        self.form_sight.showMaximized()
        qlistid=[]
        i=0
        for x in self.idlist:
            qlistid.append(str(i)+':  '+x)
            i+=1
        self.slm.setStringList(qlistid)
        self.sight_ui.listView.setModel(self.slm)
        self.teleSignal1.emit('message_start')
        self.sight_ms.initUi('测试右眼，请遮住左眼')
        #threading.Thread(target=self.teleThread).start()
        #print(threading.Thread.name)
        #print('ka')
        self.teleSignal1.emit('message_stop')
        self.teleSignal1.emit('sight_start')
        self.form_sight.exec_()
        self.teleSignal1.emit('sight_stop')

    def setList(self,connect):
        if connect not in self.idlist:
            self.idlist.append(connect)
            self.qlist.append(str(len(self.qlist))+':  '+connect)
            self.slm.setStringList(self.qlist)
            self.sight_ui.listView.setModel(self.slm)

    def messageTips(self):
        #print('实际方向：',self.picture.direct)
        if self.buttonValue!=self.picture.direct:
            self.wrong += 1
        elif self.testGrad>=5.2:
            self.wrong=2
        if self.wrong == 2 :
            if self.message:
                self.teleSignal1.emit('sight_stop')
                self.teleSignal1.emit('message_start')
                #self.m_ui.pushButton.setStyleSheet('')
                self.sight_ms.initUi('开始左眼测试')
                self.teleSignal1.emit('message_stop')
                self.teleSignal1.emit('sight_start')
                self.wrong=2
                self.message = False
            else :
                self.teleSignal1.emit('sight_stop')
                self.teleSignal1.emit('message_start')
                self.sight_ms.initUi('视力测试结束!!')
                self.teleSignal1.emit('message_stop')
                    #self.messageEnd = False
    def run(self):
        #print('错误次数：',self.wrong)
        if self.wrong == 2 :
            #print('end')
            self.endTest()
        elif self.wrong==1 :
            self.setNewTestPicture()
        else:
            self.sight_ui.label_6.setText(
                    '<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">' + str(round(
                        self.testGrad,1)) + '</span></p></body></html>')
            self.testGrad+=0.1
            self.setNewTestPicture()

    def sightUpSlot(self):
        self.buttonValue = '上'
        self.messageTips()
        self.start()

    def sightDownSlot(self):
        self.buttonValue = '下'
        self.messageTips()
        self.start()

    def sightLeftSlot(self):
        self.buttonValue = '左'
        self.messageTips()
        self.start()

    def sightRightSlot(self):
        self.buttonValue = '右'
        self.messageTips()
        self.start()

    def setNewTestPicture(self):
        self.sight_ui.label_7.setPixmap(Gui.QPixmap(''))
        file_path=self.picture.getSightPicture(self.testGrad)
        #print(file_path)
        image=Gui.QImage(file_path)
        self.sight_ui.label_7.setPixmap( Gui.QPixmap(image))
        self.testNum += 1
        #print('测试次数', self.testNum)
        self.sight_ui.label_8.setText('<html><head/><body><p align=\"center\">第' + str(self.testNum) + '张</p></body></html>')

    def teleSignaldeal1(self,connect):
        #print(connect)
        if connect=='009f0e':
            self.sightRightSlot()
        elif connect=='009f06':
            self.sightLeftSlot()
        elif connect=='009f43':
            self.sightUpSlot()
        elif connect=='009f0a':
            self.sightDownSlot()
    # 测试结束处理
    def endTest(self):
        if self.testObject != '左':
            #print('右结束')
            self.testGradRight = round(self.testGrad,1)
            self.testGrad = 4.4
            self.testObject = '左'
            self.wrong=0
            self.messageEnd=True
            # self.showMessage('开始左眼测试')
            self.sight_ui.label_6.setText(
                '<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">' + str(
                    0.0) + '</span></p></body></html>')
            self.sight_ui.label_5.setText(
                '<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">左眼</span></p></body></html>')
            self.testNum = 0
            self.setNewTestPicture()
        else:
            #print('左结束')
            self.testGradLeft = round(self.testGrad,1)
            self.teleSignal1.emit(str(self.testGradLeft)+'_'+str(self.testGradRight)+'_su')
            #self.testData()
            self.sleep(1)
            #print(self.tele_flag)
            self.form_sight.close()

class TestPicture():
    def __init__(self,path):
        self.sigtPicture={}
        self.direct=''
        self.testGradNum=0.0
        self.baseSightPath =path
        self.loadSightPicture()

    #加载视力测试图片
    def loadSightPicture(self):
        pictureName=os.listdir(self.baseSightPath)
        #print(pictureName)
        for x in pictureName:
            key=x.split('_')[-2]
            if key  not in self.sigtPicture.keys():
                self.sigtPicture[key]=[]
                self.sigtPicture[key].append(x)
            else:
                self.sigtPicture[key].append(x)
        #print(self.sigtPicture)
    #抽取图片测试
    def getSightPicture(self,i):
        s=round(i,2)
        filename=random.choice(self.sigtPicture[str(s)])
        self.direct=filename.split('_')[-1][0]
        return self.baseSightPath+'/'+filename