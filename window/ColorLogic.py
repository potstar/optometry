'''
文件：colorlogic.py 辨色测试逻辑
作者：potstar
版权：
日期：2019.1.28
'''
from PyQt5.QtWidgets import QDialog
import color
import messagelogic
import PyQt5.QtGui as Gui
from PyQt5.QtCore import pyqtSignal
import os
import random
import time

class ColorWindow(QDialog):
    colorSignal=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.testNum=0
        self.color_ui=color.Ui_Dialog()
        self.color_ui.setupUi(self)
        self.color_ui.pushButton.clicked.connect(self.dealA)
        self.color_ui.pushButton_4.clicked.connect(self.dealB)
        self.color_ui.pushButton_3.clicked.connect(self.dealC)
        self.color_ui.pushButton_2.clicked.connect(self.dealD)

        #self.colorButtons=[self.color_ui.pushButton,self.color_ui.pushButton_4,self.color_ui.pushButton_3,self.color_ui.pushButton_2]
        #self.colorButton=self.color_ui.pushButton
        #self.selectButtons=['A','B','C','D']
        #self.selectButton='A'

        self.color_ms=messagelogic.MessageWindow()
        self.color_ms.m_ui.pushButton.clicked.connect(self.color_ms.close)
        self.basepath=os.getcwd()
        self.picFileName = os.listdir(self.basepath+'/color')
        self.rightValue='B、'
        self.rightValueStr=''
        self.wrongValue=''
        self.wrongValue_1=''

    def setPicture(self,filename='98_示教_n.jpg'):

        filePath=self.basepath+'/color/'+filename
        self.picFileName.remove('98_示教_n.jpg')
        self.values = filename.split('_')
        image = Gui.QImage(filePath)
        self.color_ui.label_7.setPixmap(Gui.QPixmap(image))
        self.testNum += 1
        #print('测试次数', self.testNum)
        self.color_ui.label_8.setText(
            '<html><head/><body><p align=\"center\">第' + str(self.testNum) + '张    '+
            '     待测'+str(len(self.picFileName))
            +'张'+'</p></body></html>')
        self.color_ui.label_9.setText( '<html><head/><body<p align=\"center\"><span style=\" font-size:24pt;\">'
                                       'A、88</p><p>   B、98  </p><p>   C、 99  </p><p> D、什么都没有</span></p></body></html>')
    def initUi(self):
        self.color_ui.label_5.setText('<html><head/><body><p align=\"center\">读取图中数字，选择你读到的</p>'
                                      '<p>数字的对应选项，例如示教图中</p><p>可以读到98，则你应该选择B</p></body></html>')
        self.showMaximized()
        self.colorSignal.emit('message_start')
        self.color_ms.initUi('测试开始，第一张为测试示例图！')
        self.colorSignal.emit('message_stop')
        self.colorSignal.emit('sight_start')
        self.exec_()
        self.colorSignal.emit('sight_stop')
    def setNewTestPic(self):
        if self.picFileName:
            if self.testNum==1:
                fileName='66_色盲_n.jpg'
                self.picFileName.remove(fileName)
            else:
                fileName=self.loadPictureName()
            s_values=['A、','B、','C、']
            self.values=fileName.split('_')
            self.rightValue=random.choice(s_values)+self.values[0]
            if 'A' in self.rightValue:
                text='<html><head/><body<p align=\"center\"><span style=\" font-size:24pt;\">'+ self.rightValue+\
                     '</p><p>B、8</p><p>C、60</p><p> D、什么都没有</span></p></body></html>'
            elif 'B' in self.rightValue:
                text='<html><head/><body<p align=\"center\"><span style=\" font-size:24pt;\">A、60</p><p>'+ self.rightValue+\
                     '</p><p>C、86</p><p> D、什么都没有</span></p></body></html>'
            elif 'C' in self.rightValue:
                text='<html><head/><body<p align=\"center\"><span style=\" font-size:24pt;\">A、00</p><p>B、986</p><p>'+self.rightValue +\
                     '</p><p> D、什么都没有</span></p></body></html>'
            file_path=self.basepath+'/color/'+fileName
            self.color_ui.label_7.setPixmap(Gui.QPixmap(''))
            image = Gui.QImage(file_path)
            self.color_ui.label_7.setPixmap(Gui.QPixmap(image))
            self.testNum += 1
            #print('测试次数', self.testNum)
            self.color_ui.label_8.setText(
                '<html><head/><body><p align=\"center\">第' + str(self.testNum) + '张    ' + '     待测' + str(
                    len(self.picFileName)) + '张' + '</p></body></html>')
            self.color_ui.label_9.setText(text)
        else:
            self.testData()
    def loadPictureName(self):
        fileName=random.choice(self.picFileName)
        self.picFileName.remove(fileName)
        return fileName
    def testData(self):
        if self.testNum==1:
            self.setNewTestPic()
        elif self.rightValueStr=='示教':
            self.rightValueStr = '正常'
            self.colorSignal.emit(self.rightValueStr+'_color')
            self.colorSignal.emit('sight_stop')
            self.colorSignal.emit('message_start')
            self.color_ms.initUi('测试结束！！！')
            self.colorSignal.emit('message_stop')
            time.sleep(0.5)
            self.close()
        elif self.testNum==6:
            self.rightValueStr = '正常'
            self.colorSignal.emit(self.rightValueStr + '_color')
            self.colorSignal.emit('sight_stop')
            self.colorSignal.emit('message_start')
            self.color_ms.initUi('测试结束！！！')
            self.colorSignal.emit('message_stop')
            time.sleep(0.5)
            self.close()
        else:
            self.colorSignal.emit(self.rightValueStr + '_color')
            self.colorSignal.emit('sight_stop')
            self.colorSignal.emit('message_start')
            self.color_ms.initUi('测试结束！！！')
            self.colorSignal.emit('message_stop')
            time.sleep(0.5)
            self.close()
    def dealA(self):
        if 'A' not in self.rightValue:
            self.rightValueStr = self.values[1]
            self.testData()
        else:
            self.setNewTestPic()
    def dealB(self):
        if 'B' not in self.rightValue:
            self.rightValueStr = self.values[1]
            self.testData()
        else:
            self.setNewTestPic()
    def dealC(self):
        if 'C' not in self.rightValue:
            self.rightValueStr = self.values[1]
            self.testData()
        else:
            self.setNewTestPic()
    def dealD(self):
        self.rightValueStr = self.values[1]
        self.testData()

    def teleSignaldeal(self,connect):
        #print(connect)
        if connect=='009f0a':
            self.dealD()
        elif connect=='009f43':
            self.dealA()
        elif connect=='009f06':
            self.dealB()
        elif connect=='009f0e':
            self.dealC()

