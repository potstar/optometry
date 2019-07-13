from PyQt5.QtWidgets import QDialog
import pwd
import dateserverse

class pwdWin(QDialog):
    def __init__(self):
        super().__init__()
        self.pwdUi=pwd.Ui_Dialog()
        self.pwdUi.setupUi(self)
        self.setWindowTitle('密码修改')
        self.userid=''
        self.pwdUi.pushButton.clicked.connect(self.post)
    def showPwdWin(self):
        self.show()
        self.exec_()
    def post(self):
        serv = dateserverse.MySQLControl()
        pwd1 = self.pwdUi.lineEdit.text()
        pwd2 = self.pwdUi.lineEdit_2.text()
        if pwd1!=pwd2:
            self.pwdUi.label_4.setText('请输入两次相同密码！！！')
        elif not pwd1 or not pwd2:
            self.pwdUi.label_4.setText('请输入密码')
        else:
            sql1 = 'update manager set pwd=%s where username=%s'%(pwd1,self.userid)
            sql2 = 'update manager set firstLog=%d where username=%s'%(0, self.userid)
            serv.deleteBase(sql1)
            serv.deleteBase(sql2)
            self.close()

