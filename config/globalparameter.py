# coding:utf-8
'''
description:配置全局参数
'''
import time, os

# 获取项目路径
# project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_case_path = project_path + "/src/test_case"
# print u'日志路径：'+log_path
# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path + "/report/"
report_name = report_path + time.strftime('%Y%m%d%H%S', time.localtime())
# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.exmail.qq.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_name = "lilinhui@himobi.net"  # 发件人名称
email_password = "Llh1312"  # 发件人登录密码
email_To = 'lilinhui@himobi.net'  # 收件人
screenshot_path = project_path + "/screenshot/"