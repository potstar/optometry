
import LogWin
from PyQt5.QtWidgets import QDialog,QMessageBox

import RootLogic
import WorkWinLogic
import dateserverse

class LogWinForm(QDialog):
    def __init__(self):
        super().__init__()
        #self.user='19009'
        #self.passw='zhou13145deng'
        self.log_ui=LogWin.Ui_Dialog()
        self.log_ui.setupUi(self)

        self.setWindowTitle('登陆')
        self.log_ui.pushButton.clicked.connect(self.login)
        self.sql=dateserverse.MySQLControl()
    def login(self):
        id = self.log_ui.lineEdit.text()
        password = self.log_ui.lineEdit_2.text()
        if id=='admin':
            if self.sql.connectDB(password):
                print(12)
                root = RootLogic.RootWinLogic()
                #self.log_ui.lineEdit_2.setText('')
                #self.log_ui.lineEdit.setText('')
                self.close()
                root.initUi()
            else:
                self.log_ui.lineEdit_2.setText('')
                self.log_ui.label_3.setText( '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">用户名或密码错误，请重试！！！</span></p></body></html>')
        elif id:
            data=self.sql.queryData('select username,pwd,firstLog from manager where username=' + id)
            if data[0][0]==id and data[0][1] == password:
                workWin = WorkWinLogic.WorkWindowLogic()
                #self.log_ui.lineEdit_2.setText('')
                #self.log_ui.lineEdit.setText('')
                self.close()
                workWin.user_id=id
                workWin.firstLog=data[0][2]
                workWin.initUi()
            else:
                self.log_ui.lineEdit_2.setText('')
                self.log_ui.label_3.setText( '<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">用户名或密码错误，请重试！！！</span></p></body></html>')
    def initUi(self):
        self.exec()
    def checkUser(self):
        pass

