import os,time
import unittest
from appium import webdriver
from time import sleep
import HTMLTestRunner
from src.common import gesture_mainpulation
from src.common import device_info
from config.globalparameter import screenshot_path

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class test_appium(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1.0'
        # desired_caps['platformVersion'] = device_info.AndroidVersion
        desired_caps['deviceName'] = '854D7PHUOV9HZDHU'
        # desired_caps['deviceName'] = device_info.deviceID
        #desired_caps['app'] = PATH(
        #    '../../../sample-code/apps/ContactManager/ContactManager.apk'
        #)
        desired_caps['appPackage'] = 'com.face.camera'
        desired_caps['appActivity'] = '.mvp.view.activity.SplashActivity'
        # adb shell dumpsys activity
        # adb shell dumpsys activity |find "mFocusedActivity"
        self.driver = webdriver.Remote('http://localhost:4725/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_case1(self):
        print("————————————————testcase1")
        time.sleep(5)
        self.driver.find_element_by_id("com.face.camera:id/fd").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.face.camera:id/a0w").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.android.wallpaper.livepicker:id/apply_button").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.face.camera:id/k9").click()
        time.sleep(5)
        gesture_mainpulation.gesture_mainpulation.swipe_down(self,500,2)
        time.sleep(5)
        gesture_mainpulation.gesture_mainpulation.swipe_up(self,500,2)
        try:
            info_message = self.driver.find_element_by_id("com.face.camera:id/a1c").text  # 获取到元素中的文本信息
            self.assertEqual(info_message, "热门功能1")
        except Exception as e:
            self.driver.save_screenshot(screenshot_path + 'test_case1.png')
            print("进入主页失败！", format(e))
            raise Exception("进入主页失败！")
        else:
            print("进入主页成功！")

        #el = self.driver.find_element_by_accessibility_id("Add Contact")
        #el.click()
        #textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        #textfields[0].send_keys("Appium User")
        #textfields[2].send_keys("someone@appium.io")

        #self.assertEqual('Appium User', textfields[0].text)
        #self.assertEqual('someone@appium.io', textfields[2].text)

        #self.driver.find_element_by_accessibility_id("Save").click()

        # for some reason "save" breaks things
        #alert = self.driver.switch_to_alert()

        # no way to handle alerts in Android
        #self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        #self.driver.press_keycode(3)

    def test_case2(self):
        print("————————————————testcase2")
        time.sleep(5)

# if __name__ == '__main__':
#     print("————————————————start")
#     suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
#     #unittest.TextTestRunner(verbosity=2).run(suite)
#     #suite = unittest.TestSuite()
#     #suite.addTest(ContactsAndroidTests('test_add_contacts'))
#     #suite.addTest(ContactsAndroidTests('test_add_contacts1'))
#     #runner = unittest.TextTestRunner()
#     #runner.run(suite)
#     # 执行测试,使用HTMLTestRunner生成测试报告
#     path = os.path.abspath(os.path.dirname(os.getcwd()))  # 此脚本的父级目录
#     now = time.strftime("%Y-%m-%d %H:%M:%S")
#     #filename = open(os.getcwd() + '/report' + '/ testResult_report'+ now + '.html', 'wb')
#     filename = open(path + '/test/report' + '/testResult_report' + now + '.html', 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(stream=filename, title='Report_title', description='Report_description', verbosity=2)
#     result=runner.run(suite)
#     result.success_count  # 运行成功的数目
#     result.testsRun  # 运行测试用例的总数
#     result.failure_count  # 运行失败的数目
#     filename.close()