
import HTMLTestReportCN
import time
import os
import unittest,sys

# def all_case(TestCase="TestCase"):  #TestCase存放用例的文件夹
#     '''加载指定目录下的所有的用例'''
#     # 待执行用例的目录
#     # case_dir = "D:\\test\\jiekou\\testcase"
#     case_dir = os.path.join(os.getcwd(), "TestCase")
#     testcase = unittest.TestSuite()
#
#     discover = unittest.defaultTestLoader.discover(case_dir,
#                                                    pattern="test*.py",
#                                                    top_level_dir=None)
#     # discover方法筛选出来的用例，循环添加到测试套件中
#     for test_suite in discover:
#         for test_case in iter(test_suite):
#             # 添加用例到testcase
#             testcase.addTests(test_case)
#     print (testcase)
#     return testcase

case_path = os.path.join(os.getcwd(), "TestCase")
def all_case():

    discover = unittest.defaultTestLoader.discover(case_path,pattern="test_*.py",top_level_dir=None)

    print(discover)

    return discover



if __name__ == "__main__":

    # 报告的路径
    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(os.getcwd(), "report", nowtime + ".html")
    fp = open(report_path, "wb")
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                             title=u'接口自动化测试报告',
                                             description=u'用例执行情况：')

    runner.run(all_case())
    fp.close()