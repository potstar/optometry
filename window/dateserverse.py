'''
文件：dataserverse.py 数据上传服务
作者：potstar
版权：
日期：2019.2.25
'''
import urllib.request as request
import urllib.parse as parse
import urllib.error as error
import json

class MySQLControl():
    def __init__(self,config):
        self.loginURL=config.url
        self.URL='http://129.28.117.138:8085/AeyeBackend/testvalues/add'
        self.token=''
        self.valid=0 #token失效
        self.login(config.username,config.password)
    def login(self,username,password):
        data={'username':username,'password':password}
        rData=parse.urlencode(data).encode()
        try:
           respose=request.urlopen(request.Request(self.loginURL,data=rData))
        except:
            return None
        value=json.loads(respose.read().decode('utf-8'))
        if value['code']==200:
            self.token=value['data']['token']
    def writeData(self,data):
        requeryData=self.dataToJson(data).encode('utf-8')
        if self.token:
            header={'auth':self.token,'Content-Type': 'application/json;charset=UTF-8',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
        else:
            return False
        requestBody=request.Request(self.URL,headers=header,data=requeryData)
        succuss=self.upLoadData(requestBody)
        if succuss==1:
            succuss = self.upLoadData(requestBody)
        return succuss
    def upLoadData(self,requestBody):
        try:
            response=request.urlopen(requestBody)
        except error as e:
            return False
        value = json.loads(response.read().decode('utf-8'))
        if value['code']==200:
            return True
        elif self.valid==0:
            self.valid=1
            self.login()
            return 1
        return False
    def dataToJson(self,data):
        body1={'studentid':'','lefteyes':'','righteys':'','leftasti':'','rightasti':'','color':'','leftnoeyes':'','rightnoeyes':'','issutiable':''}
        body={}
        i=0
        for item in body1.keys():
            body[item]=data[i]
            i+=1
        return json.dumps(body)
