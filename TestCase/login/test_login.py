#######登录接口#############
# coding:utf-8
import unittest
import requests,yaml
from common import WLJM_Comm

#读取配置文件中的数据
# userData=yaml.load(open('../../config/ApiUrl','r',encoding='utf-8'))

with open('../../config/ApiUrl', encoding="utf-8") as f:
    yml_data=f.read()
    userData = yaml.load(yml_data,Loader=yaml.FullLoader)


class login(unittest.TestCase):
    def setUp(self):   #前置条件
        pass

    def test_Login(self):  #登录接口

        datajson={'username': userData['username'],
                  'password': userData['password'],
        }
        login_url =userData['host_login']+userData['login_url']
        #登录的接口封装在WLJM_Comm.py,可以直接调用
        res=WLJM_Comm.login(login_url,headers="",datas=datajson)
        res_code=res.json()['code']
        print (login_url)
        print (res.json())
        self.assertEqual(res_code,0)

    def tearDown(self):  #还原测试环境
        pass

if __name__=='__main__':
    unittest.main()

