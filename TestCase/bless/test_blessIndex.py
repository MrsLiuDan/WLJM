
#+++++++++++++++++  进入祈福页面   ++++++++++++++++
# 用例  ID: BlessIndex
# 用例标题: 进入祈福页面
#流程：
    #1、登录
    #2、进入祈福页面

# coding:utf-8
import unittest
import requests,yaml
from common import WLJM_Comm

#读取配置文件中的数据
userData=yaml.load(open('../../config/ApiUrl','r',encoding='utf-8'),Loader=yaml.FullLoader)

class BlessIndex(unittest.TestCase):
    def setUp(self):   #前置条件
        pass

    def test_blessIndex(self):  #进入祈福页面接口用例

        datajson={'userId': 10000,
                  'pageSize': 1,
                  'pageIndex': 1,
                  'offerIds': '1'
        }
        bless_url =userData['host']+userData['blessIndex_url']
        # res = requests.post(bless_url, headers="",data =datajson)

        #封装了进入祈福接口
        res=WLJM_Comm.bless(bless_url,headers="",datas=datajson)
        res_code=res.json()['code']
        print (bless_url)
        print (res.json())
        self.assertEqual(res_code,0)

    def tearDown(self):  #还原测试环境
        pass

if __name__=='__main__':
    unittest.main()

