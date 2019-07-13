from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog,QProgressBar
import Change
import sys
import xlsxwriter
import xlrd
import time
from pystrich.code128 import Code128Encoder


class win(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Change.Ui_Dialog()
        self.ui.setupUi(self)
        #self.ui.pushButton.clicked.connect(self.new)
        self.ui.pushButton.clicked.connect(self.new1)

        self.step = 0
    def new1(self):
        pbar = QProgressBar(self)
        pbar.setGeometry(30, 50, 200, 25)
        pbar.show()
        while True:
            if self.step==100:
                pbar.close()
                break
            time.sleep(0.5)
            self.step+=1
            pbar.setValue(self.step)



    def new(self):
        s, t = QFileDialog.getOpenFileName(self, '选择文件', './', 'All Files(*);;Text Files (*.xlsx')
        excel = xlrd.open_workbook(s)
        print(s)
        sql = 'INSERT INTO user(userID,userName,pwd,userSex,userAge,userSchool) values(%s,%s,%s,%s,%s,%s)'
        col = []
        for x in excel.sheet_names():
            sheet = excel.sheet_by_name(x)
            for x in range(sheet.nrows - 1):
                c = sheet.row_values(x + 1, 0, 4)
                col.append(c)
        i = 2
        book = xlsxwriter.Workbook('sd.xlsx')
        sheet1 = book.add_worksheet('code')
        b = book.add_format({'align': 'center'})
        for x in col:
            code = x[0]
            coder = Code128Encoder(code)
            coder.save('条码.png')
            print(12)
            sheet1.set_row(i-1,100)
            sheet1.set_column(1,2,50)
            sheet1.write('A' + str(i), x[1], b)
            sheet1.insert_image('B' + str(i), '条码.png', { 'x_offset': 5, 'y_offset': 5})
            i += 1
        book.close()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=win()
    w.show()
    sys.exit(app.exec_())