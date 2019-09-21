

####封装的登录接口####
import requests
import json



#封装的登录接口
def login(url,headers="",datas=""):
    res=requests.post(url,headers="",data=datas)
    return res


#封装的祈福接口
def bless(url,headers="",datas=""):
    res=requests.post(url,headers="",data=datas)
    return res


