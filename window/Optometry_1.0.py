'''
文件：optometry.py 主程序入口
作者：potstar
版权：
日期：2019.3.25
'''
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog,QWidget,QMessageBox
import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui as Gui
import sys
import os
import threading
import time
import mainWindow
import messagelogic
import testLogLogic
import registerLogic
import sightlogic
import suitableLogic
import AstimatismLogic
import ColorLogic
import settingLogic
import dateserverse
import configparser
import serialServe

#继承主窗口类
class SubMainWin(QMainWindow):
    #teleSignal=PyQt5.QtCore.pyqtSignal(str)
    mainSignal = PyQt5.QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.id=''
        self.rangekey = [x for x in range(48, 58)] + [x for x in range(65, 91)]
        #键盘事件
    def keyPressEvent(self, event):
        keys=event.key()
        if keys in self.rangekey:
            self.id += chr(keys)
        elif keys==16777217:
            self.mainSignal.emit(self.id)
            #print('组窗口',self.id)
            self.id=''
#新建窗口类并初始化，管理控件与窗口逻辑运行
class MainWindow(mainWindow.Ui_MainWindow):
    #初始化
    def __init__(self):
        super().__init__()
        self.form = SubMainWin()
        self.setupUi(self.form)
        # 主窗口绑定事件
        self.pushButton_2.clicked.connect(self.slot)
        self.pushButton_4.clicked.connect(self.slot_asti)
        self.pushButton.clicked.connect(self.slot_color)
        self.pushButton_3.clicked.connect(self.windowSetting)
        self.pushButton_5.clicked.connect(self.suitable)
        # 失能按钮焦点
        self.pushButton_2.setFocusPolicy(PyQt5.QtCore.Qt.NoFocus)
        self.pushButton_4.setFocusPolicy(PyQt5.QtCore.Qt.NoFocus)
        self.pushButton.setFocusPolicy(PyQt5.QtCore.Qt.NoFocus)
        self.pushButton_3.setFocusPolicy(PyQt5.QtCore.Qt.NoFocus)
        self.pushButton_5.setFocusPolicy(PyQt5.QtCore.Qt.NoFocus)
        #绑定主窗口信号处理函数
        self.form.mainSignal.connect(self.mainDataDeal)
        #初始化遥控器服务
        self.ser=serialServe.SerialServes()
        #绑定遥控信号主窗口处理函数
        self.ser.main_signal.connect(self.serialDeal)
        #初始化消息提示窗口
        self.ms=messagelogic.MessageWindow()
        #初始化账号输入窗口
        self.testwin = testLogLogic.testWin()

        #self.testwin.testUi.pushButton_2.clicked.connect(self.registSolt)
        #输入方式：False为扫描输入，Ture为手动输入
        #self.flag=False
        #扫码编码信息存储
        self.userInformation=[]
        #姓名
        self.name=''
        #读取当前测试距离
        self.config('r')
        #按钮值
        self.select=['sight','suitable','asti','color','exit']
        #当前按钮值
        self.ok='sight'
        self.buttons=[self.pushButton_2,self.pushButton_5,self.pushButton_4,self.pushButton,self.pushButton_3]#按钮
        self.button=self.pushButton_2
        #当前测试项目
        self.testProhject=0
        #已完成项目
        self.finishNum=0
        self.tipValue=['开始适配检测','开始散光检测','开始辨色检测','开始视力检测']
        #测试结果
        self.sightValue=''
        self.suitableValue=''
        self.astiValue=''
        self.colorValue=''
        #初始化网络服务
        self.dataserver = dateserverse.MySQLControl()
        #self.t_mainFlag=True
    #读/写测试距离设置
    def config(self,model,value=None):
        x = configparser.ConfigParser()
        path_ini=os.getcwd() + '\opt.ini'
        x.read(path_ini)
        if model == 'r':
            self.sightPath = x.get('sightpath', 'base')
            if not self.sightPath:
                self.sightPath = os.getcwd() + '\sight3'
        elif  model=='w':
            x.set('sightpath','base',value)
            x.write(open(path_ini,'w'))
    #开启主窗口，并开启遥控信号处理线程
    def showUi(self):
        self.ser.mainServe=True
        t = threading.Thread(target=self.ser.teleControl)
        t.setDaemon(True)
        t.start()
        self.form.setIconSize(PyQt5.QtCore.QSize(64,64))
        self.form.setWindowIcon(Gui.QIcon('favicon.png'))
        self.form.showMaximized()
        self.dataReHand()
        #self.teleThread()
    #新线程监测扫码输入
    def newThread(self):
        while True:
            if self.testwin.user_id:
                #print('kaishi')账号有效性判断
                if 'stu' in self.testwin.user_id:
                    self.userInformation.append(self.testwin.user_id)
                    self.testwin.close()
                    self.testwin.user_id=''
                    break
                else:
                    self.testwin.user_id = ''
                    self.testwin.testUi.label_3.setText('用户不存在，请重新输入!!!')
            else:
                time.sleep(0.5)
    #开启消息提示框
    def showMessageWin(self,tip):
        #self.form_sight.hide()
        self.m_Ui.label.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">'+tip+'</span></p></body></html>')
        self.messageWindow.show()
        self.messageWindow.exec_()
    #账号网络验证：功能暂定
    def checkID(self,userid):
        sql="select userID,userName from user where userID='"+userid+"'"
        #serve=dateserverse.MySQLControl()
        data=self.dataserver.queryData(sql)
        if data:
            if data[0][0]==userid:
                self.flag=True
                self.name=data[0][1]
                self.testwin.testUi.lineEdit.setText('')
                self.testwin.close()
            else:
                del self.userInformation[0]
                self.testwin.testUi.label_3.setText('用户不存在，请重新输入!!!')
        else:
            del self.userInformation[0]
            self.testwin.testUi.lineEdit.setText('')
            self.testwin.testUi.label_3.setText('用户不存在或网络未连接，请重新输入!!!')
    #开启视力检查窗口
    def openNewWindow(self):
        self.testProhject=1
        self.finishNum+=1
        sight = sightlogic.SightWindow(self.sightPath)
        #self.checkID(self.userInformation[0])
        self.form.hide()
        #print('开启新窗口')
        if len(self.userInformation)>=2:
            sight.idlist=self.userInformation[1:]
        sight.sight_ui.label.setText(
            "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt;\">" + '用户信息     姓名：'
            + self.name+ '         账号：' +
            self.userInformation[0] + '         等待人数：' +
            str(len(self.userInformation) - 1) + '</span></p></body></html>')
        sight.setNewTestPicture()
        sight.form_sight.setWindowTitle('视力检测'+self.sightPath[-1]+'米')
        sight.form_sight.sightSignal.connect(self.dataDeal)
        sight.teleSignal.connect(self.teleDeal)
        #self.t_mainFlag=False
        self.ser.mainServe=False
        self.ser.message_signal.connect(sight.sight_ms.closeWin)
        self.ser.sight_signal.connect(sight.teleSignaldeal)
        sight.initUi()
        self.form.show()
        self.ser.message_signal.disconnect(sight.sight_ms.closeWin)
        self.ser.sight_signal.disconnect(sight.teleSignaldeal)
        #self.teleThread()
        self.ser.qbox_signal_3.connect(self.qboxDeal)
        self.ser.QmessageboxSer=True
        self.ser.messageTip='su'
        self.msq = messagelogic.MessageWindow()
        self.msq.m_ui.pushButton.clicked.disconnect()
        self.msq.m_ui.pushButton.clicked.connect(self.continueTest)
        self.mark = 3
        if self.finishNum==4:
            self.testProhject=0
            self.msq.initUi('测试完毕！！！')
        else:
            btn1= PyQt5.QtWidgets.QPushButton('跳过')
            btn=PyQt5.QtWidgets.QPushButton('结束')
            btn.setMinimumSize(PyQt5.QtCore.QSize(100,80))
            btn1.setMinimumSize(PyQt5.QtCore.QSize(100, 80))
            font = Gui.QFont()
            font.setFamily("AcadEref")
            font.setPointSize(24)
            btn.setFont(font)
            btn1.setFont(font)
            btn.clicked.connect(self.contiuneDeal)
            btn1.clicked.connect(self.nextPro)
            self.msq.m_ui.horizontalLayout.addWidget(btn)
            self.msq.m_buttons.append(btn)
            self.msq.m_ui.horizontalLayout.addWidget(btn1)
            self.msq.m_buttons.append(btn1)
            self.msq.initUi('裸眼检测完毕！继续适配测试！')
        self.ser.QmessageboxSer = False
        self.ser.mainServe = True
        #self.form.setEnabled(True)
    #视力检查按钮事件处理
    def slot(self):
        if not self.userInformation:
            t = threading.Thread(target=self.newThread)
            t.setDaemon(True)
            t.start()
            self.ser.mainServe = False
            self.testwin.showTestWin()
            if self.userInformation:
                self.openNewWindow()
        else:
            self.openNewWindow()
    #散光按钮事件处理
    def slot_asti(self):
        if not self.userInformation:
            t=threading.Thread(target=self.newThread)
            t.setDaemon(True)
            t.start()
            #self.ms.m_ui.pushButton.setEnabled(False)
            #self.ms.initUi('请扫码，，，，')
            self.ser.mainServe = False
            self.testwin.showTestWin()
            if self.userInformation:
                self.openAstiWin()
        else:
            self.openAstiWin()
    #开启散光检测窗口
    def openAstiWin(self):
        self.testProhject=3
        self.finishNum+=1
        asti = AstimatismLogic.AstimatismWindow()
        self.form.hide()
        asti.astimatism_ui.label.setText(
            "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt;\">" + '用户信息     姓名：'
            + self.name+ '         账号：' +
            self.userInformation[0] + '         等待人数：' +
            str(len(self.userInformation) - 1) + '</span></p></body></html>')
        image = Gui.QImage(asti.filename)
        pixmap = Gui.QPixmap.fromImage(image)
        asti.astimatism_ui.label_7.setPixmap(pixmap)
        asti.setWindowTitle('散光检测')
        self.ser.mainServe = False
        asti.astiTeleSignal.connect(self.teleDeal)
        self.ser.message_signal.connect(asti.anti_ms.closeWin)
        self.ser.sight_signal.connect(asti.astiTeleControl)
        self.ser.qbox_signal_1.connect(self.qboxDeal)
        asti.initUi()
        self.ser.QmessageboxSer = True
        self.form.show()
        self.ser.message_signal.disconnect(asti.anti_ms.closeWin)
        self.ser.sight_signal.disconnect(asti.astiTeleControl)
        self.ser.messageTip='c'
        self.msq=messagelogic.MessageWindow()
        self.ser.QmessageboxSer = True
        self.msq.m_ui.pushButton.clicked.disconnect()
        self.msq.m_ui.pushButton.clicked.connect(self.continueTest)
        self.mark = 1
        if self.finishNum==4:
            self.testProhject = 0
            self.msq.initUi('测试完毕！！！')
        else:
            btn1 = PyQt5.QtWidgets.QPushButton('跳过')
            btn = PyQt5.QtWidgets.QPushButton('结束')
            btn.setMinimumSize(PyQt5.QtCore.QSize(100, 80))
            btn1.setMinimumSize(PyQt5.QtCore.QSize(100, 80))
            font = Gui.QFont()
            font.setFamily("AcadEref")
            font.setPointSize(24)
            btn.setFont(font)
            btn1.setFont(font)
            btn.clicked.connect(self.contiuneDeal)
            btn1.clicked.connect(self.nextPro)
            self.msq.m_ui.horizontalLayout.addWidget(btn)
            self.msq.m_buttons.append(btn)
            self.msq.m_ui.horizontalLayout.addWidget(btn1)
            self.msq.m_buttons.append(btn1)
            self.msq.initUi('散光测试完毕！继续辨色检测！')
        self.ser.qbox_signal_1.disconnect(self.qboxDeal)
        self.ser.QmessageboxSer = False
        self.ser.mainServe = True
    #辨色按钮事件处理
    def slot_color(self):
        if not self.userInformation:
            t = threading.Thread(target=self.newThread)
            t.setDaemon(True)
            t.start()
            self.ser.mainServe = False
            self.testwin.showTestWin()
            if self.userInformation:
               self.openColorWin()
        else:
            self.openColorWin()
    #开启辨色检测窗口
    def openColorWin(self):
        self.testProhject=4
        self.finishNum+=1
        col = ColorLogic.ColorWindow()
        self.form.hide()
        #print('开启新窗口')
        col.color_ui.label.setText(
            "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt;\">" + '用户信息     姓名：'
            + self.name+ '         账号：' +
            self.userInformation[0] + '         等待人数：' +
            str(len(self.userInformation) - 1) + '</span></p></body></html>')
        col.setPicture()
        col.setWindowTitle('辨色检测')
        self.ser.mainServe=False
        col.colorSignal.connect(self.teleDeal)
        self.ser.message_signal.connect(col.color_ms.closeWin)
        self.ser.sight_signal.connect(col.teleSignaldeal)
        col.initUi()
        self.form.show()
        self.ser.qbox_signal_2.connect(self.qboxDeal)
        self.ser.message_signal.disconnect(col.color_ms.closeWin)
        self.ser.sight_signal.disconnect(col.teleSignaldeal)
        self.ser.messageTip = 's'
        self.ser.QmessageboxSer = True
        self.msq = messagelogic.MessageWindow()
        self.msq.m_ui.pushButton.clicked.disconnect()
        self.msq.m_ui.pushButton.clicked.connect(self.continueTest)
        self.mark = 2
        if self.finishNum==4:
            self.testProhject = 0
            self.msq.initUi('测试完毕！！！')
        else:
            btn1 = PyQt5.QtWidgets.QPushButton('跳过')
            btn = PyQt5.QtWidgets.QPushButton('结束')
            btn.setMinimumSize(PyQt5.QtCore.QSize(100, 80))
            btn1.setMinimumSize(PyQt5.QtCore.QSize(100, 80))
            font = Gui.QFont()
            font.setFamily("AcadEref")
            font.setPointSize(24)
            btn.setFont(font)
            btn1.setFont(font)
            btn.clicked.connect(self.contiuneDeal)
            btn1.clicked.connect(self.nextPro)
            self.msq.m_ui.horizontalLayout.addWidget(btn)
            self.msq.m_buttons.append(btn)
            self.msq.m_ui.horizontalLayout.addWidget(btn1)
            self.msq.m_buttons.append(btn1)
            self.msq.initUi('辨色测试完毕！继续裸眼视力测试！')
        self.ser.QmessageboxSer = False
        self.ser.mainServe=True
    #开启适配检测窗口
    def openSuitWin(self):
        self.testProhject = 2
        self.finishNum+=1
        sight1 = suitableLogic.SightWindow(self.sightPath)
        #self.checkID(self.userInformation[0])
        self.form.hide()
        # print('开启新窗口')
        if len(self.userInformation) >= 2:
            sight1.idlist = self.userInformation[1:]
        sight1.sight_ui.label.setText(
            "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt;\">" + '用户信息     姓名：'
            + self.name + '         账号：' +
            self.userInformation[0] + '         等待人数：' +
            str(len(self.userInformation) - 1) + '</span></p></body></html>')
        sight1.setNewTestPicture()

        sight1.form_sight.setWindowTitle('视力检测'+self.sightPath[-1]+'米')
        sight1.form_sight.sightSignal.connect(self.dataDeal)
        sight1.teleSignal1.connect(self.teleDeal)
        # self.t_mainFlag=False
        self.ser.mainServe = False
        self.ser.message_signal.connect(sight1.sight_ms.closeWin)
        self.ser.sight_signal.connect(sight1.teleSignaldeal1)
        sight1.initUi()
        self.form.show()
        self.ser.message_signal.disconnect(sight1.sight_ms.closeWin)
        self.ser.sight_signal.disconnect(sight1.teleSignaldeal1)
        # self.teleThread()
        self.ser.qbox_signal.connect(self.qboxDeal)
        self.ser.QmessageboxSer = True
        self.ser.messageTip = 'a'
        self.msq = messagelogic.MessageWindow()
        self.msq.m_ui.pushButton.clicked.disconnect()
        self.msq.m_ui.pushButton.clicked.connect(self.continueTest)
        self.mark = 0
        if self.finishNum==4:
            self.testProhject = 0
            self.msq.initUi('测试完毕！！！')
        else:
            btn1 = PyQt5.QtWidgets.QPushButton('跳过')
            btn = PyQt5.QtWidgets.QPushButton('结束')
            btn.setMinimumSize(PyQt5.QtCore.QSize(100, 80))
            btn1.setMinimumSize(PyQt5.QtCore.QSize(100, 80))
            font = Gui.QFont()
            font.setFamily("AcadEref")
            font.setPointSize(24)
            btn.setFont(font)
            btn1.setFont(font)
            btn.clicked.connect(self.contiuneDeal)
            btn1.clicked.connect(self.nextPro)
            self.msq.m_ui.horizontalLayout.addWidget(btn)
            self.msq.m_buttons.append(btn)
            self.msq.m_ui.horizontalLayout.addWidget(btn1)
            self.msq.m_buttons.append(btn1)
            self.msq.initUi('适配检测完毕！继续散光检测！')
        self.ser.QmessageboxSer = False
        self.ser.mainServe = True
    #适配按钮事件处理
    def suitable(self):
        if not self.userInformation:
            t = threading.Thread(target=self.newThread)
            t.setDaemon(True)
            t.start()
            self.ser.mainServe = False
            self.testwin.showTestWin()
            if self.userInformation:
                self.openSuitWin()
        else:
            self.openSuitWin()
    #设置按钮事件处理
    def windowSetting(self):
        #PyQt5.QtCore.QCoreApplication.quit()
        set=settingLogic.settingWin(self.sightPath)
        #self.form.hide()
        self.ser.mainServe = False
        self.ser.sight_signal.connect(set.teleControl)
        set.teleSignal1.connect(self.teleDeal)
        set.initUI()
        set.teleSignal1.disconnect()
        self.ser.mainServe=True
        #self.form.show()
    '''
    def settingSolt(self):
        self.ser.mainServe=False
        log = Loglogic.LogWinForm()
        log.initUi()
        #self.form.close()
        self.ser.mainServe = True
    '''
    #账号注册，功能暂定
    def registSolt(self):
        self.ser.mainServe = False
        self.testwin.testUi.label_3.setText('')
        self.testwin.close()
        regist=registerLogic.registerWin()
        regist.showRegisteWin()
        self.ser.mainServe = True
    #扫码信号处理
    def dataDeal(self,connect):
        #print(connect)
        if connect not in self.userInformation:
            self.userInformation.append( connect)
        '''self.sight.sight_ui.label.setText(
            "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt;\">" + '用户信息     姓名：'
            + self.userInformation[0][0] + '         学籍号：' +
            self.userInformation[0][1] + '         等待人数：' +
            str(len(self.userInformation) - 1) + '</span></p></body></html>')'''
    #主扫码信号处理
    def mainDataDeal(self,connect):
        if connect not in self.userInformation:
           self.userInformation.append( connect)
        #print(self.userInformation)
    #测试值传递，遥控窗口变换处理
    def teleDeal(self,connect):
        if connect=='message_start':
            self.ser.messageServe=True
        elif connect=='message_stop':
            self.ser.messageServe = False
        elif connect=='sight_start':
            self.ser.sightServe = True
        elif connect=='sight_stop':
            self.ser.sightServe = False
        elif 'svalue' in connect:
            self.sightValue=connect
        elif 'avalue' in connect:
            self.astiValue=connect
        elif 'color' in connect:
            self.colorValue=connect
        elif 'su' in connect:
            self.suitableValue=connect
        elif 'setting' in connect:
            self.sightPath=connect.split('_')[0]
            self.config('w',self.sightPath)
    #主窗口信息提示遥控信号处理
    def qboxDeal(self,connect):
        if '009f0e' in connect:
            self.msq.m_button.setStyleSheet('')
            m_index=self.msq.m_values.index(self.msq.m_value)+1
            if m_index>2:
                m_index=0
            self.msq.m_button=self.msq.m_buttons[m_index]
            self.msq.m_value = self.msq.m_values[m_index]
            self.msq.m_button.setStyleSheet('background-color:yellow')
        elif '009f06' in connect:
            self.msq.m_button.setStyleSheet('')
            m_index = self.msq.m_values.index(self.msq.m_value) - 1
            if m_index < 0:
                m_index = 2
            self.msq.m_button = self.msq.m_buttons[m_index]
            self.msq.m_value=self.msq.m_values[m_index]
            self.msq.m_button.setStyleSheet('background-color:yellow')
        elif '009f02' in connect:
            if self.finishNum==4:
                self.contiuneDeal()
            elif self.msq.m_value=='yes':
                self.continueTest()
            elif self.msq.m_value=='next':
                self.nextPro()
            else:
                self.contiuneDeal()
        elif connect=='n009f02':
            self.ser.QmessageboxSer = False
            self.ser.qbox_signal_4.disconnect(self.qboxDeal)
            self.msq.close()
            self.slot()
    #主窗口遥控信号处理
    def serialDeal(self,connect):
        #print(connect)
        if connect=='009f0e':
            self.button.setStyleSheet("background-color: rgb(170, 170, 255);")
            selectIndex = self.select.index(self.ok) + 1
            if selectIndex>4:
                selectIndex=0
            self.button=self.buttons[selectIndex]
            self.ok = self.select[selectIndex]
            self.button.setStyleSheet('background-color:yellow')
        if connect=='009f06':
            self.button.setStyleSheet("background-color: rgb(170, 170, 255);")
            selectIndex=self.select.index(self.ok)-1
            if selectIndex<0:
                selectIndex=4
            self.ok=self.select[selectIndex]
            self.button = self.buttons[selectIndex]
            self.button.setStyleSheet('background-color:yellow')
        elif connect=='009f57':
            self.form.close()
        elif connect=='009f02':
            if self.ok=='asti':
                self.slot_asti()
            elif self.ok=='color':
                self.slot_color()
            elif self.ok=='exit':
                self.windowSetting()
            elif self.ok=='sight':
                self.pushButton_2.setStyleSheet('background-color:yellow')
                self.pushButton_2.setStyleSheet("background-color: rgb(170, 170, 255);")
                self.slot()
            elif self.ok=='suitable':
                self.suitable()
    #主窗口信息提示按钮点击处理
    def contiuneDeal(self):
        self.ser.QmessageboxSer = False
        self.msq.close()
        if self.mark==0:
            self.ser.qbox_signal.disconnect(self.qboxDeal)
        elif self.mark==1:
            self.ser.qbox_signal_1.disconnect(self.qboxDeal)
        elif self.mark==2:
            self.ser.qbox_signal_2.disconnect(self.qboxDeal)
        elif self.mark==3:
            self.ser.qbox_signal_3.disconnect(self.qboxDeal)
        elif self.mark==4:
            self.ser.qbox_signal_4.disconnect(self.qboxDeal)
        self.testdataDeal()
    #继续测试
    def continueTest(self):
        self.ser.QmessageboxSer = False
        self.msq.close()
        if self.mark==0:
            self.ser.qbox_signal.disconnect(self.qboxDeal)
        elif self.mark==1:
            self.ser.qbox_signal_1.disconnect(self.qboxDeal)
        elif self.mark==2:
            self.ser.qbox_signal_2.disconnect(self.qboxDeal)
        elif self.mark==3:
            self.ser.qbox_signal_3.disconnect(self.qboxDeal)
        elif self.mark==4:
            self.ser.qbox_signal_4.disconnect(self.qboxDeal)
        if self.testProhject==1:
            self.suitable()
        elif self.testProhject==2:
            self.slot_asti()
        elif self.testProhject==3:
            self.slot_color()
        elif self.testProhject==4:
            self.slot()
        elif self.testProhject==0:
            self.testdataDeal()
    #跳过
    def nextPro(self):
        self.finishNum+=1
        if self.finishNum<4:
            if self.testProhject>3:
                self.testProhject=0
            self.msq.m_ui.label.setText(
                '<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">' + self.tipValue[self.testProhject] + '</span></p></body></html>')
            self.testProhject+=1
    #测试数据处理
    def testdataDeal(self):
        #print('开始上传数据。。。')
        if self.sightValue:
           sight=self.sightValue.split('_')
           self.sightValue=''
        else:
            sight=['','']
        if self.astiValue:
            asti=self.astiValue.split('_')
            self.astiValue=''
        else:asti=['','']
        if self.colorValue:
            color=self.colorValue.split('_')
            self.colorValue=''
        else:color=['','']
        if self.suitableValue:
            suitables=self.suitableValue.split('_')
            self.suitableValue=''
        else:
            suitables = ['', '']
        if sight[0] <= '4.7' or sight[1] <= '4.7':
            if suitables[0] >= '5.0' and suitables[1] >= '5.0':
                issutiable=1
            else:
                issutiable=0
        else: issutiable=1
        #待完善匹配与否
        data1=[self.userInformation[0],sight[0],sight[1],asti[0],asti[1],color[0],suitables[0],suitables[1],issutiable]
        del self.userInformation[0]
        self.finishNum=0
        r=self.dataserver.writeData(data1)
        if r:
            box = QMessageBox()
            box.setText('数据上传成功')
            box.setWindowTitle('提示')
            timer = PyQt5.QtCore.QTimer()
            timer.singleShot(1000, box.close)
            box.exec_()
        else:
            data1=data1[0:8]+[str(data1[8])]
            dataline='_'.join(data1)
            box=QMessageBox()
            box.setText('网络连接存在问题！！数据保存到本地！！！')
            box.setWindowTitle('提示')
            timer=PyQt5.QtCore.QTimer()
            timer.singleShot(1000,box.close)
            box.exec_()
            file = open('cache.txt', 'a+')
            file.write(dataline+'\n')
            file.close()
        ######待完善功能，检测扫码列表自动切换下一个人检测
        if self.userInformation:
            self.testProhject=4
            self.ser.qbox_signal_4.connect(self.qboxDeal)
            self.ser.messageTip = 'n'
            self.ser.QmessageboxSer = True
            self.msq = messagelogic.MessageWindow()
            self.msq.m_ui.pushButton.clicked.disconnect()
            self.msq.m_ui.pushButton.clicked.connect(self.continueTest)
            self.mark=4
            self.msq.initUi('请'+self.userInformation[0]+'测试')
    def dataReHand(self):
        r=False
        path=os.getcwd()+'/cache.txt'
        with open(path,'r') as fp:
            datas=fp.readlines()
            if datas:
                for x in datas:
                    x=x.strip('\n')
                    line=x.split('_')
                    line=line[0:8]+[int(line[8])]
                    r =self.dataserver.writeData(line)
                    if not r:
                        break
        if r:
            with open('cache.txt', 'w') as fps:
                fps.write('')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWindow=MainWindow()
    mainWindow.form.setWindowTitle('视力检测')
    palette=Gui.QPalette()
    palette.setBrush(Gui.QPalette.Background,Gui.QBrush(Gui.QPixmap('backgrund.jpg')))
    mainWindow.form.setPalette(palette)
    mainWindow.showUi()
    sys.exit(app.exec_())