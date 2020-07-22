# coding=utf-8
# !/usr/bin/python

import os, time

device_num = 1
deviceID = 'a'
AndroidVersion = 'b'

def checkDeviceConn():
    global device_num
    deviceInfo = os.popen("adb devices").read()
    if deviceInfo.splitlines()[1] == '':
        print("***********************")
        print("* Device Connect Fail *")
        print("***********************")
        time.sleep(100)
    elif deviceInfo.splitlines()[2] != '':
        device_num = 2
        print("2 Device Connected")
    else:
        device_num=1
        print("1 Device Connected")

def get_DeviceID():
    device_Info = os.popen("adb devices").read()
    if device_Info.splitlines()[1] == '':
        print("***********************")
        print("* Device Connect Fail *")
        print("***********************")
        time.sleep(100)
    else:
        ID = device_Info.splitlines()[1]
        global deviceID
        deviceID = ID.split("	")[0]

def get_AndroidVersion():
    global AndroidVersion
    AndroidVersion = os.popen("adb shell getprop ro.build.version.release").read()
    AndroidVersion = AndroidVersion.splitlines()[0]
    print(AndroidVersion)