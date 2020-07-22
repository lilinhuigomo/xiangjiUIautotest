# coding:utf-8

import unittest, time, HTMLTestRunner
from config.globalparameter import test_case_path, report_name, report_path
from src.common import send_email
from src.common import device_info
import os
import threading

# 构建测试集,包含src/test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test_appium.py')
suite2 = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test2_appium.py')

def device_test():
    if not os.path.isdir(report_path):  # 判定测试报告文件夹是否存在
        os.makedirs(report_path)  # 创建测试报告文件夹
    report = report_name + "Report_华为P10.html"
    fb = open(report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=u'相机变变变自动化测试报告_华为P10',
        description=u'项目描述：相机变变变'
    )
    runner.run(suite)
    fb.close()
    # 发送邮件
    time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕（这里被坑了＝＝）
    email = send_email.send_email()
    email.sendReport()

def device2_test():
    report2 = report_name + "Report_vivo.html"
    fb2 = open(report2, 'wb')
    runner2 = HTMLTestRunner.HTMLTestRunner(
        stream=fb2,
        title=u'相机变变变自动化测试报告_vivo',
        description=u'项目描述：相机变变变'
    )
    runner2.run(suite2)
    fb2.close()
    # 发送邮件
    time.sleep(10)  # 设置睡眠时间，等待测试报告生成完毕（这里被坑了＝＝）
    email2 = send_email.send_email()
    email2.sendReport()

threads = []
t1 = threading.Thread(target=device_test)
threads.append(t1)

t2 = threading.Thread(target=device2_test)
threads.append(t2)

# 执行测试
if __name__ == "__main__":
    print("————————————————start")
    device_info.checkDeviceConn()
    if device_info.device_num == 1:
        device_test()
    elif device_info.device_num ==2:
        for t in threads:
            t.start()