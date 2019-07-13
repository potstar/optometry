from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox,QGraphicsScene,QSizePolicy,QFileDialog
import sys
import os
from PyQt5.QtCore import QStringListModel
from PyQt5.QtCore import Qt
import RootWin
import dateserverse
import xlsxwriter
from pystrich.code128 import Code128Encoder
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as fcq
from matplotlib.figure import Figure
import threading
class RootWinLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.root_ui=RootWin.Ui_Dialog()
        self.root_ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setWindowTitle('管理员')
        self.root_ui.pushButton.clicked.connect(self.newCreate)
        self.root_ui.pushButton_2.clicked.connect(self.deleteData)
        self.root_ui.pushButton_7.clicked.connect(self.nextUserPage)
        self.root_ui.pushButton_8.clicked.connect(self.preUserPage)
        self.root_ui.pushButton_5.clicked.connect(self.exportUserExcel)
        self.root_ui.pushButton_4.clicked.connect(self.createNewUserRecord)
        self.root_ui.pushButton_3.clicked.connect(self.reSetUserPwd)
        self.root_ui.pushButton_9.clicked.connect(self.loadDataSql)
        self.root_ui.pushButton_6.clicked.connect(self.dropUserRecord)
        self.root_ui.pushButton_10.clicked.connect(self.updatePWD)

        self.f = FigureCanvas()
        self.sence = QGraphicsScene()
        self.sence.addWidget(self.f)
        self.root_ui.graphicsView.setScene(self.sence)
        self.fc = FigureCanvas()
        self.sence1 = QGraphicsScene()
        self.sence1.addWidget(self.fc)
        self.root_ui.graphicsView_2.setScene(self.sence1)

        self.fa = FigureCanvas()
        self.sence2 = QGraphicsScene()
        self.sence2.addWidget(self.fa)
        self.root_ui.graphicsView_3.setScene(self.sence2)

        self.rootserve=dateserverse.MySQLControl()
        self.slm = QStringListModel()
        self.qlist=[]
        #self.root_ui.pushButton.clicked.connect(self.login)
        self.userBegin=0
        self.userHeader = ['学号', '姓名', '年龄', '性别', '单位', '左眼视力', '右眼视力', '左眼闪光', '右眼闪光', '辨色']
        self.baseSql="select user.userID,user.userName,user.userAge,user.userSex,user.userSchool,optometry.sightleft," \
                     "optometry.sightright,optometry.leftasti,optometry.rightasti," \
                     "optometry.color from user inner join optometry on user.userID=optometry.userID"
        self.title = ['UserID', 'n', 'a', 's', 's', 'sightleft', 'sightright', 'leftasti', 'rightasti', 'color']
    def login(self,sql):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(self.userHeader)
        data=self.rootserve.queryData(sql)
        #model.itemChanged.connect(self.edit)
        if data:
            r,c=len(data),len(data[0])
            for i in range(r):
                for j in range(c):
                    if j==10:
                        cell=QStandardItem(data[i][j].strftime('%Y-%m-%d %H:%M:%S'))
                    else:
                       cell=QStandardItem(str(data[i][j]))
                    if j<=4:
                         cell.setEditable(False)
                    self.model.setItem(i,j,cell)
        else:
            self.userBegin-=6
        self.root_ui.tableView.setModel(self.model)
        self.model.itemChanged.connect(self.userEdit)
    def userEdit(self):
        data=self.root_ui.tableView.currentIndex().data()
        column = self.root_ui.tableView.currentIndex().column()
        row = self.root_ui.tableView.currentIndex().row()
        user_id = self.model.index(row, 0).data()
        reply=QMessageBox.information(self, '修改提示', '确定修改为'+data,QMessageBox.Yes|QMessageBox.No)
        if reply==QMessageBox.Yes:
            updateSQL = 'update optometry set ' + self.title[column] + '=' + data + ' where userID =' + user_id
            self.rootserve.deleteBase(updateSQL)
    def initUi(self):
        self.dataQuery('select username from manager')
        self.root_ui.comboBox_3.addItems(['所有', '社会', '南京第九中学', '南京师范附小'])
        self.showMaximized()
        self.login(self.baseSql+' limit ' + str(self.userBegin) + ',6')
        threading.Thread(target=self.barView,args=('select sightright,count(distinct userID) from optometry group by sightright',
                                                   'select color,count(distinct userID) from optometry group by color',
                                                   'select leftasti,count(distinct userID) from optometry group by leftasti',
                                                   )).start()
        self.exec_()
    def nextUserPage(self):
        self.userBegin+=6
        self.login(self.baseSql+' limit '+str(self.userBegin)+',6')
    def preUserPage(self):
        self.userBegin-=6
        if self.userBegin>=0:
            self.login(self.baseSql+' limit '+str(self.userBegin)+',6')
        else:self.userBegin=0
    def exportUserExcel(self):
        data=self.rootserve.queryData(self.baseSql)
        r=len(data)
        filepath, filetype = QFileDialog.getSaveFileName(self, '选择文件', './', 'All Files(*);;Text Files (*.xlsx')
        if filepath:
            workbook = xlsxwriter.Workbook(filepath)
            b = workbook.add_format({'align': 'center'})
            worksheet = workbook.add_worksheet('例子')
            worksheet.write_row('A1',self.userHeader, b)
            for i in range(r):
                worksheet.write_row('A'+str(i+2),data[i], b)
            workbook.close()
            reply=QMessageBox.information(self,'提示','导出成功',QMessageBox.Yes)
    def loadDataSql(self):
        userID=self.root_ui.lineEdit_7.text()
        if userID:
            sql = self.baseSQL + ' where user.userID=' + userID
            sightSQL = "select optometry.sightright,count(*) from user inner join optometry on user.userID=optometry.userID" + " where user.userID=" + userID + " group by optometry.sightright"
            colorSQL = "select optometry.color,count(*) from user inner join optometry on user.userID=optometry.userID" + " where user.userID=" + userID + " group by optometry.color"
            astiSQL = "select optometry.leftasti,count(*) from user inner join optometry on user.userID=optometry.userID" + " where user.userID=" + userID + " group by optometry.leftasti"
            threading.Thread(target=self.barView, args=(sightSQL, colorSQL, astiSQL, sql)).start()
            # self.login(sql)
            self.root_ui.lineEdit_7.setText('')
        else:
            age=self.root_ui.comboBox_2.currentText()
            sex = self.root_ui.comboBox.currentText()
            collection = self.root_ui.comboBox_3.currentText()
            sql = self.baseSql
            sightSQL = "select optometry.sightright,count(distinct optometry.userID) from user inner join optometry on user.userID=optometry.userID"
            colorSQL = "select optometry.color,count(distinct optometry.userID) from user inner join optometry on user.userID=optometry.userID"
            astiSQL = "select optometry.leftasti,count(distinct optometry.userID) from user inner join optometry on user.userID=optometry.userID"
            if age!='所有':
                stEnd=age.split('-')
                sql=sql+' where userAge<=%s and userAge>%s'%(stEnd[1],stEnd[0])
                sightSQL=sightSQL+' where userAge<=%s and userAge>%s'%(stEnd[1],stEnd[0])
                colorSQL+=' where userAge<=%s and userAge>%s'%(stEnd[1],stEnd[0])
                astiSQL+=' where userAge<=%s and userAge>%s'%(stEnd[1],stEnd[0])
                if sex!='所有':
                    sql=sql + " and userSex='%s'"%sex
                    sightSQL+= " and userSex='%s'"%sex
                    colorSQL +=" and userSex='%s'"%sex
                    astiSQL +=" and userSex='%s'"%sex
                    if collection != '所有':
                        sql = sql + " and userSchool='%s'"%collection
                        sightSQL+=" and userSchool='%s'"%collection
                        colorSQL +=" and userSchool='%s'"%collection
                        astiSQL +=" and userSchool='%s'"%collection
                else:
                    if collection!='所有':
                        sql = sql + " and userSchool='%s'"%collection
                        sightSQL +=" and userSchool='%s'"%collection
                        colorSQL += " and userSchool='%s'"%collection
                        astiSQL += " and userSchool='%s'"%collection
            else:
                if sex!='所有':
                    sql=sql +  " where userSex='%s'"%sex
                    sightSQL +=" where userSex='%s'"%sex
                    colorSQL +=" where userSex='%s'"%sex
                    astiSQL +=" where userSex='%s'"%sex
                    if collection != '所有':
                        sql = sql + " and userSchool='%s'"%collection
                        sightSQL +=" and userSchool='%s'"%collection
                        colorSQL +=" and userSchool='%s'"%collection
                        astiSQL +=" and userSchool='%s'"%collection
                else:
                    if collection!='所有':
                        sql = sql + " where userSchool='%s'"%collection
                        sightSQL +=" where userSchool='%s'"%collection
                        colorSQL += " where userSchool='%s'"%collection
                        astiSQL += " where userSchool='%s'"%collection
            sightSQL=sightSQL+" group by optometry.sightright"
            colorSQL+=" group by optometry.color"
            astiSQL+=" group by optometry.leftasti"
            self.login(sql)
            threading.Thread(target=self.barView, args=(sightSQL, colorSQL, astiSQL,sql)).start()
    def createNewUserRecord(self):
        userName = self.root_ui.lineEdit_2.text()
        userSex = self.root_ui.lineEdit_3.text()
        userAge = self.root_ui.lineEdit_4.text()
        userSchool = self.root_ui.lineEdit_5.text()
        if userName:
            self.root_ui.lineEdit_2.setText('')
            self.root_ui.lineEdit_6.setText('')
            self.root_ui.lineEdit_3.setText('')
            self.root_ui.lineEdit_4.setText('')
            self.root_ui.lineEdit_5.setText('')
            pre_id = serv.queryData('select max(userID) from user')
            pwd = '123456'
            userID = 's' + str(int(pre_id[0][0][1:]) + 1)
            reply = QMessageBox.information(self, '创建提示', '确定创建用户' + userName + '档案?', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                sql = 'INSERT INTO user(userID,userName,pwd,userSex,userAge,userSchool) values(%s,%s,%s,%s,%s,%s)'
                succss = self.rootserve.writeData((userID, userName, pwd, userSex, userAge, userSchool), sql)
                if succss:
                    path = os.getcwd()
                    coder = Code128Encoder(userID)
                    coder.save(path + '/' + userID + '条码.jpg')
                    QMessageBox.information(self, '成功提示', '创建成功,请在当前路径查看条码', QMessageBox.Yes)
        else:
            QMessageBox.information(self, '输入提示', '请输入用户ID或姓名', QMessageBox.Yes)
    def dropUserRecord(self):
        row=self.root_ui.tableView.currentIndex().row()
        userID=self.model.index(row,0).data()
        if userID:
            reply = QMessageBox.information(self, '删除提示', '确定删除用户' + userID, QMessageBox.No | QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.model.removeRow(row)
                data=self.rootserve.deleteBase('delete from optometry where userID =' + userID)
                if data:
                    self.rootserve.deleteBase('delete from user where userID =' + userID)
                else:
                    QMessageBox.information(self, '错误提示', '删除失败，可能网络存在问题', QMessageBox.Yes)
    def reSetUserPwd(self):
        userID = self.root_ui.lineEdit_6.text()
        if userID:
            reply = QMessageBox.information(self, '重置提示', '确定重置密码', QMessageBox.No | QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                sql = 'select userID from user where userID=' + userID
                data = self.rootserve.queryData(sql)
                if data:
                    r = self.rootserve.deleteBase(
                        'update user set pwd=%s where userID =%s' % (userID[-3:-1] + userID[1], userID))
                    if r:
                        QMessageBox.information(self, '提示', '重置密码成功', QMessageBox.Yes)
                    else:
                        QMessageBox.information(self, '提示', '重置密码失败，请重试', QMessageBox.Yes)
                else:
                    QMessageBox.information(self, '错误提示', '用户不存在，请检查输入ID', QMessageBox.Yes)
        else:
            QMessageBox.information(self, '输入提示', '请输入用户ID', QMessageBox.Yes)
    def dataQuery(self,sql):
        data = self.rootserve.queryData(sql)
        for x in data:
            if 'ID:'+x[0] not in self.qlist:
                self.qlist.append('ID:'+x[0])
        self.slm.setStringList(self.qlist)
        self.root_ui.listView.setModel(self.slm)
    def deleteData(self):
        for i in self.root_ui.listView.selectedIndexes():
            id=i.data().split(':')[-1]
            if id:
                self.rootserve.deleteBase('delete from manager where username =%s'%id)
                self.qlist.remove('ID:'+id)
        #self.dataQuery('select username,pwd from manager')
    def newCreate(self):
        sql= 'INSERT INTO manager(username,pwd ) values(%s,%s)'
        ids=self.root_ui.lineEdit.text()
        self.root_ui.lineEdit.setText('')
        dateid=(ids,'123')
        if ids:
            print(123)
            self.qlist.append('ID:'+ids)
            self.slm.setStringList(self.qlist)
            self.root_ui.listView.setModel(self.slm)
            self.rootserve.writeData(dateid,sql)

    def barView(self,sightSQL,colorSQL,astiSQL):

        sightdata = self.rootserve.queryData(sightSQL)
        colordata = self.rootserve.queryData(colorSQL)
        astidata=self.rootserve.queryData(astiSQL)
        self.f.plotsight(sightdata)
        self.fc.plotColor(colordata)
        self.fa.plotAsti(colordata)
    def updatePWD(self):
        for i in self.root_ui.listView.selectedIndexes():
            id=i.data().split(':')[-1]
        self.rootserve.deleteBase('update manager set pwd=%s where username=%s'%(id[-3:-1]+id[-1],id))
        self.rootserve.deleteBase('update manager set firstLog=%d where username=%s' % (1, id))
class FigureCanvas(fcq):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        fcq.__init__(self, fig)
        self.setParent(parent)
        fcq.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        fcq.updateGeometry(self)
    def plotsight(self,data):
        x=[]
        y=[]
        for i in data:
            x.append(float(i[0]))
            y.append(i[1])
        #self.axes = self.figure.add_subplot(111)
        # self.axes.plot(data, 'r-')
        self.axes.cla()
        self.axes.bar(x,y,width=0.08)

        self.axes.set_title('视力分布',fontproperties='STSong',fontsize=13)
        self.draw()
    def plotColor(self,data):
        x=[]
        y=[]
        for i in data:
            x.append(i[0])
            y.append(i[1])
        self.axes.cla()
        self.axes.bar(x,y,width=0.2)
        self.axes.set_xticks(x)
        self.axes.set_xticklabels(x, rotation=45, fontproperties='STSong')
        self.axes.set_title('红绿色盲情况',fontproperties='STSong',fontsize=13)
        self.draw()
    def plotAsti(self,data):
        x = []
        y = []
        for i in data:
            x.append(i[0])
            y.append(i[1])
        self.axes.cla()
        self.axes.bar(x, y, width=0.2)
        self.axes.set_xticks(x)
        self.axes.set_xticklabels(x, rotation=30, fontproperties='STSong')
        self.axes.set_title('闪光分布', fontproperties='STSong', fontsize=13)
        self.draw()

