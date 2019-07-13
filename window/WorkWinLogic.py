from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox,QGraphicsScene,QSizePolicy,QFileDialog,QProgressBar
from PyQt5.QtCore import QTimer,Qt,QBasicTimer
import sys
import os
import WorkWin1
import pwdLogic
import dateserverse
import xlsxwriter
import xlrd
from pystrich.code128 import Code128Encoder
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as fcq
from matplotlib.figure import Figure
import threading

class WorkWindowLogic(QDialog):
    def __init__(self):
        super().__init__()
        self.work_ui=WorkWin1.Ui_Dialog()
        self.work_ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setWindowTitle('数据查询下载')
        self.serv=dateserverse.MySQLControl()
        self.begin=0
        self.user_id=''
        self.firstLog=bytes(0)
        self.flag=False
        self.f = FigureCanvas()
        self.sence = QGraphicsScene()
        self.sence.addWidget(self.f)
        self.work_ui.graphicsView.setScene(self.sence)
        self.fc=FigureCanvas()
        self.sence1 = QGraphicsScene()
        self.sence1.addWidget(self.fc)
        self.work_ui.graphicsView_2.setScene(self.sence1)

        self.fa = FigureCanvas()
        self.sence2 = QGraphicsScene()
        self.sence2.addWidget(self.fa)
        self.work_ui.graphicsView_3.setScene(self.sence2)

        self.fts= FigureCanvas()
        self.sence3 = QGraphicsScene()
        self.sence3.addWidget(self.fts)
        self.work_ui.graphicsView_4.setScene(self.sence3)

        self.ftsr = FigureCanvas()
        self.sence4 = QGraphicsScene()
        self.sence4.addWidget(self.ftsr)
        self.work_ui.graphicsView_5.setScene(self.sence4)

        self.ftsc= FigureCanvas()
        self.sence5 = QGraphicsScene()
        self.sence5.addWidget(self.ftsc)
        self.work_ui.graphicsView_6.setScene(self.sence5)

        self.work_ui.pushButton.clicked.connect(self.loadData)
        self.work_ui.pushButton_7.clicked.connect(self.prePage)
        self.work_ui.pushButton_5.clicked.connect(self.nextPage)
        self.work_ui.pushButton_2.clicked.connect(self.exportExcel)
        self.work_ui.pushButton_4.clicked.connect(self.createNewRecord)
        self.work_ui.pushButton_6.clicked.connect(self.createNews)
        self.work_ui.pushButton_3.clicked.connect(self.reSetPwd)
        self.work_ui.pushButton_9.clicked.connect(self.pwd_win)
        #self.model=QStandardItemModel()
        self.header = ['学号', '姓名', '年龄', '性别', '单位', '左眼视力', '右眼视力', '左眼闪光', '右眼闪光', '辨色','测试时间']
        self.baseSQL="select user.userID,user.userName,user.userAge,user.userSex,user.userSchool,optometry.sightleft," \
                     "optometry.sightright,optometry.leftasti,optometry.rightasti," \
                     "optometry.color,optometry.createTime from user inner join optometry on user.userID=optometry.userID"
        self.excelData=[]
        self.timer=QBasicTimer()
        self.step=0
        self.pbar = QProgressBar(self)
    def edit(self):
        #self.model.itemChanged.disconnect()
        data=self.work_ui.tableView.currentIndex().data()
        reply=QMessageBox.information(self, '修改提示', '确定修改为'+data,QMessageBox.Yes|QMessageBox.No)
        if reply==QMessageBox.Yes:
            #self.model.itemChanged.connect(self.edit)
            pass
        else:
            pass
            '''row=self.work_ui.tableView.currentIndex().row()
            column=self.work_ui.tableView.currentIndex().column()
            pre=self.model.index(column,row).data()
            self.model.setItem(column,row,QStandardItem(''))
            print(99)
            self.work_ui.tableView.setModel(self.model)
            self.model.itemChanged.connect(self.edit)'''
    def loadData(self):
        userID=self.work_ui.lineEdit_6.text()
        if userID:
            sql=self.baseSQL+' where user.userID='+userID

            sightSQL = "select optometry.averages,count(*) from user inner join optometry on user.userID=optometry.userID"+" where user.userID="+userID+" group by optometry.averages"
            colorSQL = "select optometry.color,count(*) from user inner join optometry on user.userID=optometry.userID"+" where user.userID="+userID+" group by optometry.color"
            astiSQL = "select optometry.leftasti,count(*) from user inner join optometry on user.userID=optometry.userID"+" where user.userID="+userID+" group by optometry.leftasti"
            single_data=self.login(sql)
            threading.Thread(target=self.s_barView, args=(sightSQL, colorSQL, astiSQL,single_data)).start()
        else:
            age=self.work_ui.comboBox_4.currentText()
            sex = self.work_ui.comboBox.currentText()
            collection = self.work_ui.comboBox_2.currentText()
            city=self.work_ui.comboBox_5.currentText()
            province=self.work_ui.comboBox_6.currentText()
            sql = self.baseSQL
            sightSQL="select averages,count(*) from optometry x where CreateTime=(select max(CreateTime) from optometry y where x.userID=y.userID) and x.userID in (select userID from user"
            colorSQL="select optometry.color,count(distinct optometry.userID) from user inner join optometry on user.userID=optometry.userID"
            astiSQL="select optometry.leftasti,count(distinct optometry.userID) from user inner join optometry on user.userID=optometry.userID"
            averagesql="select avg(optometry.averages),date_format(optometry.CreateTime,'%Y-%m')  from user inner join optometry on user.userID=optometry.userID "
            if age!='所有':
                stEnd=age.split('-')
                sql=sql+' where userAge<=%s and userAge>%s'%(stEnd[1],stEnd[0])
                sightSQL=sightSQL+" where userAge<=%s and userAge>%s"%(stEnd[1],stEnd[0])
                colorSQL+=' where userAge<=%s and userAge>%s'%(stEnd[1],stEnd[0])
                astiSQL+=' where userAge<=%s and userAge>%s'%(stEnd[1],stEnd[0])
                averagesql+=' where userAge<=%s and userAge>%s'%(stEnd[1],stEnd[0])
                if sex!='所有':
                    sql=sql + " and userSex='%s'"%sex
                    sightSQL+= " and userSex='%s'"%sex
                    colorSQL +=" and userSex='%s'"%sex
                    astiSQL +=" and userSex='%s'"%sex
                    averagesql +=" and userSex='%s'"%sex
                    if collection != '所有':
                        sql = sql + " and userSchool='%s'"%collection
                        sightSQL+=" and userSchool='%s'"%collection
                        colorSQL +=" and userSchool='%s'"%collection
                        astiSQL +=" and userSchool='%s'"%collection
                        averagesql +=" and userSex='%s'" % collection
                        if city!='所有':
                            sql = sql + " and userCity='%s'" % city
                            sightSQL += " and userCity='%s'" % city
                            colorSQL += " and userCity='%s'" % city
                            astiSQL += " and userCity='%s'" % city
                            averagesql +=" and userCity='%s'" % city
                        else:
                            if province!='所有':
                                sql = sql + " and userAddress='%s'" % province
                                sightSQL += " and userAddress='%s'" % province
                                colorSQL += " and userAddress='%s'" % province
                                astiSQL += " and userAddress='%s'" % province
                                averagesql +=" and userCity='%s'" %province
                    else:
                        if city!='所有':
                            sql = sql + " and userCity='%s'" % city
                            sightSQL += " and userCity='%s'" % city
                            colorSQL += " and userCity='%s'" % city
                            astiSQL += " and userCity='%s'" % city
                            averagesql +=" and userCity='%s'" % city
                        else:
                            if province!='所有':
                                sql = sql + " and userAddress='%s'" % province
                                sightSQL += " and userAddress='%s'" % province
                                colorSQL += " and userAddress='%s'" % province
                                astiSQL += " and userAddress='%s'" % province
                                averagesql +=" and userCity='%s'" % province
                else:
                    if collection!='所有':
                        sql = sql + " and userSchool='%s'"%collection
                        sightSQL +=" and userSchool='%s'"%collection
                        colorSQL += " and userSchool='%s'"%collection
                        astiSQL += " and userSchool='%s'"%collection
                        averagesql +=" and userSchool='%s'"%collection
                        if city!='所有':
                            sql = sql + " and userCity='%s'" % city
                            sightSQL += " and userCity='%s'" % city
                            colorSQL += " and userCity='%s'" % city
                            astiSQL += " and userCity='%s'" % city
                            averagesql +=" and userSchool='%s'" % city
                        else:
                            if province!='所有':
                                sql = sql + " and userAddress='%s'" % province
                                sightSQL += " and userAddress='%s'" % province
                                colorSQL += " and userAddress='%s'" % province
                                astiSQL += " and userAddress='%s'" % province
                                averagesql +=" and userAddress='%s'" % province
                    else:
                        if city!='所有':
                            sql = sql + " and userCity='%s'" % city
                            sightSQL += " and userCity='%s'" % city
                            colorSQL += " and userCity='%s'" % city
                            astiSQL += " and userCity='%s'" % city
                            averagesql +=" and userAddress='%s'" %city
                        else:
                            if province!='所有':
                                sql = sql + " and userAddress='%s'" % province
                                sightSQL += " and userAddress='%s'" % province
                                colorSQL += " and userAddress='%s'" % province
                                astiSQL += " and userAddress='%s'" % province
                                averagesql +=" and userAddress='%s'" % province
            else:
                if sex!='所有':
                    sql=sql +  " where userSex='%s'"%sex
                    sightSQL +=" where userSex='%s'"%sex
                    colorSQL +=" where userSex='%s'"%sex
                    astiSQL +=" where userSex='%s'"%sex
                    averagesql +=" where userSex='%s'"%sex
                    if collection != '所有':
                        sql = sql + " and userSchool='%s'"%collection
                        sightSQL +=" and userSchool='%s'"%collection
                        colorSQL +=" and userSchool='%s'"%collection
                        astiSQL +=" and userSchool='%s'"%collection
                        averagesql +=" and userSchool='%s'"%collection
                        if city!='所有':
                            sql = sql + " and userCity='%s'" % city
                            sightSQL += " and userCity='%s'" % city
                            colorSQL += " and userCity='%s'" % city
                            astiSQL += " and userCity='%s'" % city
                            averagesql +=" where userCity='%s'" % city
                        else:
                            if province!='所有':
                                sql = sql + " and userAddress='%s'" % province
                                sightSQL += " and userAddress='%s'" % province
                                colorSQL += " and userAddress='%s'" % province
                                astiSQL += " and userAddress='%s'" % province
                                averagesql +=" where userAddress='%s'" % province
                    else:
                        if city!='所有':
                            sql = sql + " and userCity='%s'" % city
                            sightSQL += " and userCity='%s'" % city
                            colorSQL += " and userCity='%s'" % city
                            astiSQL += " and userCity='%s'" % city
                            averagesql +=" where userCity='%s'" % city
                        else:
                            if province!='所有':
                                sql = sql + " and userAddress='%s'" % province
                                sightSQL += " and userAddress='%s'" % province
                                colorSQL += " and userAddress='%s'" % province
                                astiSQL += " and userAddress='%s'" % province
                                averagesql +=" where userAddress='%s'" % province
                else:
                    if collection!='所有':
                        sql = sql + " where userSchool='%s'"%collection
                        sightSQL +=" where userSchool='%s'"%collection
                        colorSQL += " where userSchool='%s'"%collection
                        astiSQL += " where userSchool='%s'"%collection
                        averagesql +=" and userSchool='%s'"%collection
                        if city!='所有':
                            sql = sql + " and userCity='%s'" % city
                            sightSQL += " and userCity='%s'" % city
                            colorSQL += " and userCity='%s'" % city
                            astiSQL += " and userCity='%s'" % city
                            averagesql +=" where userCity='%s'" % city
                        else:
                            if province!='所有':
                                sql = sql + " and userAddress='%s'" % province
                                sightSQL += " and userAddress='%s'" % province
                                colorSQL += " and userAddress='%s'" % province
                                astiSQL += " and userAddress='%s'" % province
                                averagesql +=" where userAddress='%s'" % province
                    else:
                        if city!='所有':
                            sql = sql + " where userCity='%s'" % city
                            sightSQL += " where userCity='%s'" % city
                            colorSQL += " where userCity='%s'" % city
                            astiSQL += " where userCity='%s'" % city
                            averagesql +=" where userCity='%s'" % city
                        else:
                            if province!='所有':
                                sql = sql + " where userAddress='%s'" % province
                                sightSQL += " where userAddress='%s'" % province
                                colorSQL += " where userAddress='%s'" % province
                                astiSQL += " where userAddress='%s'" % province
                                averagesql +=" where userAddress='%s'" % province
            if collection!='所有' or sex!='所有' or age!='所有':
                sightSQL = sightSQL + ") group by averages"
            else:
                sightSQL="select averages,count(*) from optometry x where CreateTime=(select max(CreateTime) from optometry y where x.userID=y.userID) group by averages"
            colorSQL+=" group by optometry.color"
            astiSQL+=" group by optometry.leftasti"
            averagesql+=" group by date_format(optometry.CreateTime,'%Y-%m')"
            self.login(sql)
            threading.Thread(target=self.barView,args=(sightSQL,colorSQL,astiSQL,averagesql)).start()
    def login(self,sql):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(self.header)
        data=self.serv.queryData(sql)
        self.excelData=data
        #data = self.serv.post(sql)
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
            self.begin-=6
            QMessageBox.information(self, '错误提示', '网络连接失败或查询不存在', QMessageBox.Yes)
        self.work_ui.tableView.setModel(self.model)
        self.model.itemChanged.connect(self.edit)
        return data
    def nextPage(self):
        self.begin+=6
        self.login(self.baseSQL+' limit '+str(self.begin)+',6')
    def prePage(self):
        self.begin-=6
        if self.begin>=0:
            self.login(self.baseSQL+' limit '+str(self.begin)+',6')
        else:self.begin=0
    def exportExcel(self):
        r=len(self.excelData)
        filepath,filetype=QFileDialog.getSaveFileName(self,'选择文件','./','All Files(*);;Text Files (*.xlsx')
        if filepath:
            workbook = xlsxwriter.Workbook(filepath)
            b = workbook.add_format({'align': 'center'})
            worksheet = workbook.add_worksheet('例子')
            worksheet.write_row('A1',self.header, b)
            for i in range(r):
                worksheet.write_row('A'+str(i+2),self.excelData[i], b)
            workbook.close()
            reply=QMessageBox.information(self,'提示','导出成功',QMessageBox.Yes)
            print('导出成功')
    def createNewRecord(self):
        userName=self.work_ui.lineEdit_3.text()
        userSex=self.work_ui.comboBox_7.currentText()
        userAge=self.work_ui.lineEdit_5.text()
        userProvince = self.work_ui.comboBox_3.currentText()
        usercity = self.work_ui.lineEdit_7.text()
        userSchool=self.work_ui.lineEdit_2.text()
        if userName:
            pwd='123456'
            pre_id = serv.queryData('select max(userID) from user')
            userID = 's' + str(int(pre_id[0][0][1:]) + 1)
            reply=QMessageBox.information(self,'创建提示','确定创建用户'+userName+'档案?',QMessageBox.Yes|QMessageBox.No)
            if reply==QMessageBox.Yes:
                sql='INSERT INTO user(userID,userName,pwd,userSex,userAge,userSchool,userAddress,userCity) values(%s,%s,%s,%s,%s,%s,%s,%s)'
                succss=self.serv.writeData((userID,userName,pwd,userSex,userAge,userSchool,userProvince,usercity),sql)
                if succss:
                    path=os.getcwd()
                    coder=Code128Encoder(userID)
                    coder.save(path+'/'+userID+'条码.jpg')
                    QMessageBox.information(self,'成功提示','创建成功,请在当前路径查看条码',QMessageBox.Yes)
            self.work_ui.lineEdit.setText('')
            self.work_ui.lineEdit_3.setText('')
            self.work_ui.lineEdit_7.setText('')
            self.work_ui.lineEdit_5.setText('')
            self.work_ui.lineEdit_2.setText('')
        else:
            QMessageBox.information(self,'输入提示','请输入用户ID或姓名',QMessageBox.Yes)

    def timerEvent(self, e):
        if self.step>=100:
            self.step=0
            self.timer.stop()
            return
        self.step+=1
        self.pbar.setValue(self.step)

    def createNews(self):
        s, t = QFileDialog.getOpenFileName(self, '选择文件', './', 'All Files(*);;Text Files (*.xlsx')
        if s:
            file=s.split('/')[-1]
            reply = QMessageBox.information(self,'创建提示','确定导入'+file, QMessageBox.Yes | QMessageBox.No)
            if reply:
                self.pbar.setGeometry(600,700,600,25)
                self.pbar.show()
                excel = xlrd.open_workbook(s)
                sql = 'INSERT INTO user(userID,userName,pwd,userSex,userAge,userAddress,userCity,userSchool) value(%s,%s,%s,%s,%s,%s,%s,%s)'
                col = []
                self.timer.start(100,self)
                pre_id=self.serv.queryData('select max(userID) from user')
                if pre_id:
                    id_num=int(pre_id[0][0][1:])
                    for x in excel.sheet_names():
                        sheet = excel.sheet_by_name(x)
                        for x in range(sheet.nrows - 1):
                            id_num+=1
                            c = sheet.row_values(x + 1, 0, 7)
                            c.insert(2,'123456')
                            c[0]='s'+str(id_num)
                            col.append(tuple(c))
                    i = 2
                    book = xlsxwriter.Workbook('sd.xlsx')
                    sheet1 = book.add_worksheet('code')
                    b = book.add_format({'align': 'center'})
                    self.serv.writeData(tuple(col),sql)
                    for x in col:
                        code = x[0]
                        coder = Code128Encoder(code)
                        coder.save('条码.png')
                        print(12)
                        sheet1.set_row(i - 1, 100)
                        sheet1.set_column(1, 2, 50)
                        sheet1.write('A' + str(i), x[1], b)
                        sheet1.insert_image('B' + str(i), '条码.png', {'x_offset': 5, 'y_offset': 5})
                        i += 1

                    book.close()
                    if self.timer.isActive():
                        self.timer.stop()
                        self.pbar.close()
                    box = QMessageBox()
                    box.setText('数据上传成功')
                    box.setWindowTitle('提示')
                    timer = QTimer()
                    timer.singleShot(1500, box.close)
                    box.exec_()
    def dropRecord(self):
        userID=self.work_ui.lineEdit.text()
        if userID:
            reply = QMessageBox.information(self, '删除提示', '确定删除用户' + userID, QMessageBox.No | QMessageBox.Yes)
            if reply==QMessageBox.Yes:
                sql='select userID from user where userID='+userID
                data=self.serv.queryData(sql)
                if data:
                    self.serv.deleteBase('delete from user where userID ='+userID)
                else:
                    QMessageBox.information(self,'错误提示','删除用户不存在，请检查输入ID',QMessageBox.Yes)
        else:
            QMessageBox.information(self,'输入提示','请输入用户ID',QMessageBox.Yes)
    def reSetPwd(self):
        userID = self.work_ui.lineEdit.text()
        if userID:
            reply = QMessageBox.information(self, '重置提示', '确定重置密码' , QMessageBox.No | QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                sql = 'select userID from user where userID=' + userID
                data = self.serv.queryData(sql)
                if data:
                    r=self.serv.deleteBase('update user set pwd=%s where userID =%s'%(userID[-3:-1]+userID[1],userID))
                    if r:
                        QMessageBox.information(self, '提示', '重置密码成功', QMessageBox.Yes)
                    else:
                        QMessageBox.information(self, '提示', '重置密码失败，请重试', QMessageBox.Yes)
                else:
                    QMessageBox.information(self, '错误提示', '用户不存在，请检查输入ID', QMessageBox.Yes)
        else:
            QMessageBox.information(self, '输入提示', '请输入用户ID', QMessageBox.Yes)
    def barView(self,sightSQL,colorSQL,astiSQL,averagesql):
        sightdata = self.serv.queryData(sightSQL)
        colordata = self.serv.queryData(colorSQL)
        astidata=self.serv.queryData(astiSQL)
        averagedata=self.serv.queryData(averagesql)
        #print(averagedata)
        if sightdata and colordata and astidata and averagedata:
            self.f.plotsight(sightdata)
            self.fc.plotColor(colordata)
            self.fa.plotAsti(astidata)
            self.fts.plotAverage(averagedata)
            self.ftsr.plotPieAsti(astidata)
            self.ftsc.plotPieColor(colordata)
    def s_barView(self,sightSQL,colorSQL,astiSQL,data):
        sightdata = self.serv.queryData(sightSQL)
        colordata = self.serv.queryData(colorSQL)
        astidata = self.serv.queryData(astiSQL)
        if sightdata and colordata and astidata and data:
            time = [x[10] for x in data]
            right = [x[6] for x in data]
            left = [x[5] for x in data]
            self.f.plotsight(sightdata)
            self.fc.plotColor(colordata)
            self.fa.plotAsti(astidata)
            self.fts.plotTimeLeftSight(time,left)
            self.ftsr.plotTimeRightSight(time,right)
            self.ftsc.plotClear(colordata)
    def initUi(self):
        #rootApp=QApplication()
        city=self.serv.queryData('select distinct userCity from user')
        school=self.serv.queryData('select distinct userSchool from user')
        if city and school:
            self.work_ui.comboBox_2.addItems(['所有']+[x[0] for x in school])
            self.work_ui.comboBox_5.addItems(['所有']+[y[0] for y in city])
        #self.work_ui.comboBox_2.addItems(['所有','社会','南京第九中学','南京师范附小'])
        self.work_ui.comboBox_6.addItems(['所有','北京市','天津市','河北省','山西省','内蒙古自治区','上海市','江苏省','浙江省','安徽省','福建省','江西省',
                                          '山东省','辽宁省','吉林省','黑龙江省','河南省','湖北省','湖南省','广东省','广西壮族自治区','海南省'
                                          ,'重庆市','四川省','贵州省','云南省','西藏自治区','陕西省','甘肃省','青海省','宁夏回族自治区','新疆维吾尔自治区'])
        self.work_ui.comboBox_3.addItems(
            ['北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '上海市', '江苏省', '浙江省', '安徽省', '福建省', '江西省',
             '山东省', '辽宁省', '吉林省', '黑龙江省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省'
                , '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区'])
        self.showMaximized()
        if self.firstLog:
           self.pwd_win()
        self.login(self.baseSQL+' limit 0,6')
        self.work_ui.label_2.setText('工作人员： %s'%self.user_id)
        threading.Thread(target=self.barView,args=('select averages,count(*) from optometry x where CreateTime=(select max(CreateTime) from optometry y where x.userID=y.userID)  group by averages',
                                                   'select color,count(distinct userID) from optometry group by color',
                                                   'select leftasti,count(distinct userID) from optometry group by leftasti',
                                                   "select avg(averages),date_format(CreateTime,'%Y-%m')  from optometry group by date_format(CreateTime,'%Y-%m')")).start()
        self.exec()
    def pwd_win(self):
        pwdwin=pwdLogic.pwdWin()
        pwdwin.userid=self.user_id
        pwdwin.showPwdWin()
class FigureCanvas(fcq):
    def __init__(self, parent=None, width=6, height=5, dpi=100):
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
        self.axes.bar(x,y,width=0.03)
        self.axes.set_title('视力分布',fontproperties='STSong',fontsize=14)
        self.draw()
    def plotAverage(self,data):
        x = []
        y = []
        for i in data:
            x.append(i[1])
            y.append(i[0])
        # self.axes = self.figure.add_subplot(111)
        # self.axes.plot(data, 'r-')
        x1=sorted(x)
        self.axes.cla()
        self.axes.plot(x1, y)
        self.axes.set_title('视力趋势', fontproperties='STSong', fontsize=14)
        self.draw()
    def plotColor(self,data):
        x=[]
        y=[]
        for i in data:
            x.append(i[0])
            y.append(i[1])
        x.append('红绿辨色')
        y.append(0)
        self.axes.cla()
        self.axes.bar(x,y,width=0.2)
        self.axes.set_xticks(x)
        self.axes.set_xticklabels(x, rotation=45, fontproperties='STSong')
        self.axes.set_title('红绿色盲情况',fontproperties='STSong',fontsize=14)
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
        self.axes.set_xticklabels(x, rotation=45, fontproperties='STSong')
        self.axes.set_title('散光分布', fontproperties='STSong', fontsize=14)
        self.draw()
    def plotTimeLeftSight(self,datax,datay1):
        x1=sorted(datax)
        x=[x.strftime('%Y-%m-%d %H:%M:%S') for x in x1]
        long = len(x)
        xlabel = ['第%s次'% (i+1) for i in range(long)]
        y = [float(i) for i in datay1]
        self.axes.cla()
        self.axes.plot(x, y)
        self.axes.grid(color='lightgreen', linestyle='-', linewidth=1)
        self.axes.set_xticks(x)
        self.axes.set_xticklabels(xlabel,rotation=30,fontproperties='STSong')
        self.axes.set_title('左眼视力变化', fontproperties='STSong', fontsize=14)
        self.draw()
    def plotTimeRightSight(self,datax,datay):
        x1 = sorted(datax)
        x = [x.strftime('%Y-%m-%d %H:%M:%S') for x in x1]
        long = len(x)
        xlabel = ['第%s次' % (i + 1) for i in range(long)]
        y = [float(i) for i in datay]
        self.axes.cla()
        self.axes.plot(x, y)
        self.axes.grid(color='lightgreen', linestyle='-', linewidth=1)
        self.axes.set_xticks(x)
        self.axes.set_xticklabels(xlabel, rotation=45, fontproperties='STSong')
        self.axes.set_title('右眼视力变化', fontproperties='STSong', fontsize=14)
        self.draw()
    def plotPieAsti(self,data):
        labels=[]
        sizes=[]
        colors=['lightgreen','gold','lightskyblue','lightcoral']
        for x in data:
            labels.append(x[0])
            sizes.append(x[1])
        self.axes.cla()
        self.axes.set_label(labels)
        explode = [0.1, 0.1, 0.1, 0.1, 0.1]
        self.axes.pie(sizes,explode=explode[0:len(sizes)],colors=colors[0:len(sizes)],labels=labels,textprops={'fontproperties':'STSong','fontsize':'14'},shadow=True,autopct='%1.1f%%',startangle=50)
        self.axes.set_title('散光分布',fontproperties='STSong', fontsize=18)
        self.draw()
    def plotPieColor(self,data):
        labels=[]
        sizes=[]
        colors=['lightgreen','gold','lightskyblue','lightcoral','b','m','deeppink']
        for x in data:
            labels.append(x[0])
            sizes.append(x[1])
        self.axes.cla()
        self.axes.set_label(labels)
        explode = [0.1, 0.1, 0.1, 0.1, 0.1,0.1,0.1]
        self.axes.pie(sizes,explode=explode[0:len(sizes)],colors=colors[0:len(sizes)],labels=labels,textprops={'fontproperties':'STSong','fontsize':'14'},shadow=True,autopct='%1.1f%%',startangle=50)
        self.axes.set_title('辨色分布',fontproperties='STSong', fontsize=18)
        self.draw()
    def plotClear(self,data):
        labels = []
        sizes = []
        colors = ['lightgreen', 'gold', 'lightskyblue', 'lightcoral', 'b', 'm', 'deeppink']
        for x in data:
            labels.append(x[0])
            sizes.append(x[1])
        self.axes.cla()
        self.axes.set_label(labels)
        explode=[0.1,0.1,0.1,0.1,0.1,0.1]
        self.axes.pie(sizes, explode=explode[0:len(sizes)], colors=colors[0:len(sizes)], labels=labels,
                      textprops={'fontproperties': 'STSong', 'fontsize': '14'}, shadow=True, autopct='%1.1f%%',
                      startangle=50)
        self.axes.set_title('辨色分布', fontproperties='STSong', fontsize=18)
        self.draw()