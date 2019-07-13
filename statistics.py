'''
需要下载三方库xlrd,xlsxwirter
pip install ***；或pycharm中添加等
本程序文件路径使用相对路径，注意修改文件路径
作者：potstar
'''
#引入三方库对excel进行读写操作
import xlrd
import xlsxwriter
#引入时间库
import datetime
#创建员工工时处理类
class StaffTimeHanding():
    def __init__(self):
        self.path = 'timeTable.xlsx'                                             # 文件位置
        self.excel = xlrd.open_workbook(self.path)
        self.sheetNum =self.excel.sheet_names()                                  # 获取全部sheet名
        self.sheet = self.excel.sheet_by_name(self.sheetNum[0])
        self.staffName = self.sheet.col_values(0)[1:]                             # 获取员工名
        self.staffA = ['王刚', '李刚', '陈四', '陈五', '陈六']                    #部门A
        self.staffB =list( filter(lambda x: x not in self.staffA, self.staffName))#部门B
        # A组员工平均时间
        self.avrageATime = []
        # B组员工平均时间
        self.avrageBTime = []
        #A,B部门初始工作时间为0
        self.total_A_time=datetime.timedelta(hours=0, minutes=0, seconds=0)
        self.total_B_time=datetime.timedelta(hours=0, minutes=0, seconds=0)
    #读取excel数据
    def readExcel(self):
        self.readData(self.staffA)
        self.readData(self.staffB)
    #读取数据
    def readData(self,nameList):
        nowTime = datetime.timedelta(hours=0, minutes=0, seconds=0)
        for name in nameList:
            for i in self.sheetNum:
                sheet = self.excel.sheet_by_name(i)
                for rowsNum in range(sheet.nrows - 1):
                    if sheet.cell_value(rowsNum + 1, 0) == name:
                        times = sheet.cell_value(rowsNum + 1, 2)
                        if type(times) == str:
                            times = 0
                        hour, minute, seconds = xlrd.xldate_as_tuple(times, 0)[3:]
                        nowTime += datetime.timedelta(hours=hour, minutes=minute, seconds=seconds)  #计算每个员工工作总时间
            #判断员工所属团队
            if name in self.staffA:
                self.total_A_time+=(nowTime / len(self.sheetNum))  #将员工平均时间加和
                self.avrageATime.append(nowTime / len(self.sheetNum))#将平均时间写入列表，之后进行比较
            else:
                self.total_B_time+=(nowTime / len(self.sheetNum))
                self.avrageBTime.append(nowTime / len(self.sheetNum))
            nowTime = datetime.timedelta(hours=0, minutes=0, seconds=0)#清零
    #数据时间处理
    def dataHanding(self):
        self.readExcel()
        maxA = max(self.avrageATime)                            #A组最大工时
        maxAName = self.staffA[self.avrageATime.index(maxA)]    #最大工时对应的人名
        minA = min(self.avrageATime)  #A组最小工时
        minAName = self.staffA[self.avrageATime.index(minA)]
        maxB = max(self.avrageBTime)  #B组最大
        maxBName = self.staffB[self.avrageBTime.index(maxB)]
        minB = min(self.avrageBTime)  #B组最小
        minBName = self.staffB[self.avrageBTime.index(minB)]
        avrage_A_time=self.total_A_time/len(self.avrageATime)#A组平均
        avrage_B_time=self.total_B_time/len(self.avrageBTime)#B组平均
        #拼接A组数据;其中avrage_A_time.seconds 得到总的秒数
        dataA=('A组',str(len(self.staffA))+'人',str(round(avrage_A_time.seconds/3600,2))+'小时',maxAName+'('+str(round(maxA.seconds/3600,2))+'小时)',
               minAName+'('+str(round(minA.seconds/3600,2))+'小时)')
        #拼接B组数据
        dataB=('B组',str(len(self.staffB))+'人',str(round(avrage_B_time.seconds/3600,2))+'小时',maxBName+'('+str(round(maxB.seconds/3600,2))+'小时)',
               minBName+'('+str(round(minB.seconds/3600,2))+'小时)')
        book=xlsxwriter.Workbook('staffData.xlsx')     #新建excel文件,相对路径
        sheet1 = book.add_worksheet('statisticData')   #添加sheet
        b = book.add_format({'align': 'center'})       #设置格式
        sheet1.write_row('A1', ['团队','人数','平均最工时','团队MAX','团队Min'],b)  #按行写数据
        sheet1.write_row('A2',dataA, b)
        sheet1.write_row('A3',dataB,b)
        book.close()
#创建实例
s=StaffTimeHanding()
s.dataHanding()