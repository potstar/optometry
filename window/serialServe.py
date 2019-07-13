'''
文件：serialServe.py 接收红外串口信号
作者：potstar
版权：
日期：2019.2.20
'''
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog
import serial
import serial.tools.list_ports
import time
class SerialServes(QDialog):
    main_signal=pyqtSignal(str)
    message_signal=pyqtSignal(str)
    sight_signal=pyqtSignal(str)
    qbox_signal=pyqtSignal(str)
    qbox_signal_1=pyqtSignal(str)
    qbox_signal_2=pyqtSignal(str)
    qbox_signal_3 = pyqtSignal(str)
    qbox_signal_4 = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.mainServe=False
        self.messageServe=False
        self.sightServe=False
        self.QmessageboxSer=False
        self.messageTip='a'
    def teleControl(self):
        p1 = self.scanSerial()
        time.sleep(0.5)
        ser = serial.Serial(p1, 9600, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        while True:
                try:
                    data = ser.read_all().hex()
                    if data:
                        if self.mainServe:
                           self.main_signal.emit(data)
                        elif self.messageServe:
                            self.message_signal.emit(data)
                            time.sleep(0.5)
                        elif self.sightServe:
                            self.sight_signal.emit(data)
                            time.sleep(0.5)
                        elif self.QmessageboxSer:
                            if self.messageTip=='c':
                                self.qbox_signal_1.emit(self.messageTip+data)
                                time.sleep(0.5)
                            elif self.messageTip=='a':
                                self.qbox_signal.emit(self.messageTip+data)
                                #print(data)
                                time.sleep(0.5)
                            elif self.messageTip=='su':
                                self.qbox_signal_3.emit(self.messageTip + data)
                                time.sleep(0.5)
                            elif self.messageTip=='n':
                                self.qbox_signal_4.emit(self.messageTip + data)
                                time.sleep(0.5)
                            else:
                                self.qbox_signal_2.emit(self.messageTip+data)
                                time.sleep(0.5)
                except:
                    print('拔出')
                    p1 =self.scanSerial()
                    ser = serial.Serial(p1, 9600, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
                time.sleep(0.3)
    def scanSerial(self):
        while True:
            port = list(serial.tools.list_ports.comports())
            if port:
                p0 = list(port[0])
                p1 = p0[0]
                return p1
                break
            else:time.sleep(1)