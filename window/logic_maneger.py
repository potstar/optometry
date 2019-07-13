'''
Code utf-8
Created by: python3.6
Version:1.0.1
Authoer:potstar

'''
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog,QWidget,QMessageBox
import PyQt5.QtCore
import PyQt5.QtGui as Gui
import sys
import threading
import os
import time
import json
import random
import mainWindow
import sightable
import astimatism
import color
import message
import messagelogic
import dateserverse

#新建窗口类并初始化，管理控件与窗口逻辑运行
class MainWindow(QMainWindow,mainWindow.Ui_MainWindow):
    #初始化
    def __init__(self,parent=None,):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.slot)#绑定事件
        self.pushButton_4.clicked.connect(self.slot_asti)
        self.pushButton.clicked.connect(self.slot_color)
        self.pushButton_3.clicked.connect(self.windowExit)
        self.form=self

        self.ms=messagelogic.MessageWindow()

        self.userInformation=[('','12')]
        self.id=''
        self.asti=AstimatismManeger()
        self.col=ColorManeger()
    #事件处理函数
    def newThread(self):
        print('xiancheng')
        while True:
            if self.ms.name:
                print('kaishi')
                self.userInformation=[('',self.ms.name)]
                self.ms.close()
                break
            else:
                time.sleep(0.5)
    def showMessageWin(self,tip):
        #self.form_sight.hide()
        self.m_Ui.label.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">'+tip+'</span></p></body></html>')
        self.messageWindow.show()
        self.messageWindow.exec_()
    def keyPressEvent(self, event):
        if event.key()!=PyQt5.QtCore.Qt.Key_A:
            self.id+=chr(event.key())
        else:
            self.userInformation.append(('',self.id))
            print(self.userInformation)
    def getUserInformation(self):
        while True:
            pass
    def openNewWindow(self):
        self.sight = SightManeger(self.userInformation)
        self.form.hide()
        print('at')
        self.sight.sight_ui.label.setText(
            "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt;\">" + '用户信息     姓名：'
            + self.userInformation[0][0] + '         学籍号：' +
            self.userInformation[0][1] + '         等待人数：' +
            str(len(self.userInformation) - 1) + '</span></p></body></html>')
        self.sight.setNewTestPicture()
        del self.userInformation[0]
        print(self.userInformation)
        self.sight.form_sight.setWindowTitle('视力检测')
        self.sight.form_sight.showMaximized()
        print(66)
        self.sight.form_sight.exec_()
        self.form.show()
    def slot(self):
        if not self.userInformation:
            threading.Thread(target=self.newThread).start()
            self.ms.initUi()
            self.openNewWindow()
        else:
            self.openNewWindow()
    def slot_asti(self):
        self.form.hide()
        pixmap=Gui.QPixmap(self.asti.filename)
        self.asti.astimatism_ui.label_7.setPixmap(pixmap)
        self.asti.form_astimatism.setWindowTitle('散光检测')
        self.asti.form_astimatism.showMaximized()
        self.asti.form_astimatism.exec_()
        self.form.show()
    def slot_color(self):
        self.form.hide()
        self.col.form_color.setWindowTitle('辨色检测')
        self.col.form_color.showMaximized()
        self.col.form_color.exec_()
        self.form.show()
    def windowExit(self):
        PyQt5.QtCore.QCoreApplication.quit()
#视力测试界面逻辑处理
class SightManeger(PyQt5.QtCore.QThread):
    def __init__(self,user=('',''),parent=None):
        super(SightManeger,self).__init__(parent)
        self.user=user[0]#用户
        self.testNum=0#测试图数
        self.buttonValue=''
        self.preDirect=''
        self.wrong=0   #错误次数
        self.testObject='右' #测试对象

        self.message=False
        self.messageEnd=False

        self.form_sight = QDialog()  #窗口初始化
        self.sight_ui = sightable.Ui_Dialog()
        self.sight_ui.setupUi(self.form_sight)

        self.message_form = QDialog()
        self.messageUi=message.Ui_Dialog()
        self.messageUi.setupUi(self.message_form)
        self.messageUi.pushButton.clicked.connect(self.message_form.close)
        #绑定事件
        self.sight_ui.pushButton.clicked.connect(self.sightRightSlot)
        self.sight_ui.pushButton_2.clicked.connect(self.sightUpSlot)
        self.sight_ui.pushButton_4.clicked.connect(self.sightDownSlot)
        self.sight_ui.pushButton_3.clicked.connect(self.sightLeftSlot)
        #初始化图片类
        self.picture = TestPicture()

        self.testGrad=4.5
        self.testGradLeft=0
        self.testGradRight=0
    #处理函数
    def showMessage(self,tip):
        #self.form_sight.hide()
        self.messageUi.label.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">'+tip+'</span></p></body></html>')
        self.message_form.show()
        self.message_form.exec_()
    def messageTips(self):
        if self.buttonValue != self.picture.direct:
            self.wrong += 1
            # print('wrong'+self.wrong)
            if self.wrong == 2:
                self.message = True
                if self.message:
                    self.showMessage('开始左眼测试')
                    self.message = False
            elif self.wrong == 4:
                self.messageEnd = True
                if self.messageEnd:
                    self.showMessage('结束测试,上传数据。。。')
                    self.messageEnd = False
    def run(self):
        print(self.wrong)
        if self.wrong == 2:
            print('end')
            self.endTest()
        elif self.wrong==4:
            self.endTest()
        else:
            self.sight_ui.label_6.setText(
                    '<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">' + str(round(
                        self.testGrad,1)) + '</span></p></body></html>')
            self.testGrad+=0.1
            self.setNewTestPicture()
    def sightUpSlot(self):
        self.buttonValue='上'
        self.messageTips()
        self.start()
    def sightDownSlot(self):
        self.buttonValue='下'
        self.messageTips()
        self.start()
    def sightLeftSlot(self):
        self.buttonValue='左'
        self.messageTips()
        self.start()
    def sightRightSlot(self):
        self.buttonValue='右'
        self.messageTips()
        self.start()
#更新图片
    def setNewTestPicture(self):
        self.sight_ui.label_7.setPixmap(Gui.QPixmap(''))
        file_path=self.picture.getSightPicture(self.testGrad)
        pixmap=Gui.QPixmap(file_path)
        self.sight_ui.label_7.setPixmap(pixmap)
        self.testNum += 1
        print('ta=est', self.testNum)
        self.sight_ui.label_8.setText('<html><head/><body><p align=\"center\">第' + str(self.testNum) + '张</p></body></html>')
    #测试结束处理
    def endTest(self):
        if self.testObject!='左':
            print('右结束')
            self.testGradRight = self.testGrad
            self.testGrad=4.5
            self.testObject='左'
            #self.wrong=0
            #self.showMessage('开始左眼测试')
            self.sight_ui.label_6.setText(
                '<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">' + str(0.0) + '</span></p></body></html>')
            self.sight_ui.label_5.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">左眼</span></p></body></html>')
            self.testNum=0
            self.setNewTestPicture()
        else:
            print('左结束')
            self.testGradLeft=self.testGrad
            self.testData()
            self.sleep(1)
            self.form_sight.close()
    #测试数据处理
    def testData(self):
        print('开始上传数据。。。')
        try:
            dataserver=dateserverse.MySQLControl()
            dataserver.writeData([self.user,self.testGradRight,self.testGradLeft])
            dataserver.queryData()
        except:
            print('上传失败。。。')
            print('数据保存到本地。。。')
            s = {self.user: {'右眼': self.testGradRight, '左眼': self.testGradLeft}}
            file = open(self.user, 'w')
            json.dump(s, file)
            file.close()
            print('数据保存成功。')
        else:
            print('上传成功。')

#散光测试界面逻辑管理
class AstimatismManeger():
    def __init__(self):
        self.testNum1=1
        self.form_astimatism = QDialog()
        self.astimatism_ui = astimatism.Ui_Dialog()
        self.astimatism_ui.setupUi(self.form_astimatism)
        self.astimatism_ui.pushButton_4.clicked.connect(self.astimatism_slot)
        self.picture_asti = TestPicture()
        self.filename='image_4.5_右.jpg'

    def astimatism_slot(self):
        yes='是'
        print(2)

#颜色检测界面逻辑
class ColorManeger():
    def __init__(self):
        self.form_color=QDialog()
        self.color_ui=color.Ui_Dialog()
        self.color_ui.setupUi(self.form_color)

class TestPicture():
    def __init__(self):
        self.sigtPicture={}
        self.astigmatismPicture=[]
        self.colorPicture=[]
        self.direct=''
        self.testGradNum=0.0
        self.loadSightPicture()
        #self.i='5.0'
    #加载视力测试图片
    def loadSightPicture(self):
        pictureName=os.listdir('f:/python/qiutu')
        #print(pictureName)
        for x in pictureName:
            key=x.split('_')[-2]
            if key  not in self.sigtPicture.keys():
                self.sigtPicture[key]=[]
                self.sigtPicture[key].append(x)
            else:
                self.sigtPicture[key].append(x)
        print(self.sigtPicture)
    #抽取图片测试
    def getSightPicture(self,i):
        s=round(i,1)
        filename=random.choice(self.sigtPicture[str(s)])
        self.direct=filename.split('_')[-1][0]
        return 'f:/python/qiutu/'+filename
    # 加载散光测试图片
    def load_astimatismPicture(self):
        pass
    # 加载辨色检测图片
    def load_colorPicture(self):
        pass


if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWindow=MainWindow()
    mainWindow.setWindowTitle('视力检测')
    mainWindow.showMaximized()
    sys.exit(app.exec_())