'''
文件：messagelogic.py 测试信息提示逻辑
作者：potstar
版权：
日期：2019.1.26
'''
import sys
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5 import QtCore
import PyQt5.QtGui as Gui
import message
from PyQt5.QtCore import *

class MessageWindow(QDialog):
    def __init__(self,ok):
        super().__init__()
        self.s = ''
        #遥控信号确定值
        self.ok=ok
        self.name=''
        self.m_ui = message.Ui_Dialog()
        self.m_ui.setupUi(self)
        self.m_ui.pushButton.setFocusPolicy(Qt.ClickFocus)
        #self.t_flag=True
        #self.m_ui.pushButton.clearFocus()
        self.setWindowTitle('消息提示')
        self.m_ui.pushButton.clicked.connect(self.close)
        self.setWindowModality(Qt.ApplicationModal)
        self.m_buttons=[self.m_ui.pushButton]
        self.m_button=self.m_ui.pushButton
        self.m_values=['yes','no','next']
        self.m_value='yes'
        #self.initUi()
    def initUi(self,tip):
        #self.t_flag=True
        #threading.Thread(target=self.tele_mControl).start()
        self.m_ui.label.setText(
            '<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">' + tip + '</span></p></body></html>')
        self.setWindowIcon(Gui.QIcon('favicon.png'))
        self.show()
        self.exec()

    def keyPressEvent(self,e):
        if e.key() != Qt.Key_Tab:
            self.s += chr(e.key())
        else:
            self.name=self.s
            print('消息输入信息是：', self.s)
            self.s=''
        #print(self.name)
    def closeWin(self,connect):
        #print(connect)
        if connect=='009f02':
            self.m_ui.pushButton.setStyleSheet('background-color:yellow')
            self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MessageWindow()
    #window.initUi('as')
    #sys.exit(app.exec_())
