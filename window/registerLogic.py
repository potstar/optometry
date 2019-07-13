
from PyQt5.QtWidgets import QDialog,QMessageBox
import register
import dateserverse
from pystrich.code128 import Code128Encoder
import os

class registerWin(QDialog):
    def __init__(self):
        super().__init__()
        self.registerUi=register.Ui_Dialog()
        self.registerUi.setupUi(self)
        self.setWindowTitle('注册')
        self.registerUi.pushButton.clicked.connect(self.dataDeal)
        self.registerUi.pushButton_2.clicked.connect(self.close)
    def showRegisteWin(self):
        self.registerUi.comboBox.addItems(
            ['北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '上海市', '江苏省', '浙江省', '安徽省', '福建省', '江西省',
             '山东省', '辽宁省', '吉林省', '黑龙江省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省'
                , '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区'])
        self.registerUi.comboBox_2.addItems(['男','女'])
        self.show()
        self.exec_()
    def dataDeal(self):
        serv=dateserverse.MySQLControl()
        userName=self.registerUi.lineEdit_2.text()
        userSex=self.registerUi.comboBox_2.currentText()
        userAge=self.registerUi.lineEdit_4.text()
        userSchool = self.registerUi.lineEdit_5.text()
        userProvince=self.registerUi.comboBox.currentText()
        usercity=self.registerUi.lineEdit_6.text()
        if userName :
            pre_id=serv.queryData('select max(userID) from user')
            pwd='123456'
            userID='s'+str(int(pre_id[0][0][1:])+1)
            reply=QMessageBox.information(self,'创建提示','确定创建用户'+userID+'档案?',QMessageBox.Yes|QMessageBox.No)
            if reply==QMessageBox.Yes:
                sql='INSERT INTO user(userID,userName,pwd,userSex,userAge,userSchool,userAddress,userCity) values(%s,%s,%s,%s,%s,%s,%s,%s)'
                #print((userID,userName,pwd,userSex,userAge,userSchool,userProvince,usercity))
                succss=serv.writeData((userID,userName,pwd,userSex,userAge,userSchool,userProvince,usercity),sql)
                #print(succss)
                if succss:
                    path=os.getcwd()
                    coder=Code128Encoder(userID)
                    coder.save(path+'/'+userID+'条码.jpg')
                    QMessageBox.information(self,'成功提示','创建成功,请在当前路径查看条码',QMessageBox.Yes)
                else:
                    self.registerUi.label.setText('注册失败')
                self.registerUi.lineEdit.setText('')
            self.close()
        else:
            QMessageBox.information(self,'输入提示','请输入用户ID或姓名',QMessageBox.Yes)