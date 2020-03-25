#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_MainWindow(QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 529)
        MainWindow.setStyleSheet(open("lib/style.qss", "r").read())
        MainWindow.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # チェック GroupBox
        self.CheckGB = QtWidgets.QGroupBox(self.centralwidget)
        self.CheckGB.setGeometry(QtCore.QRect(20, 10, 281, 491))
        self.CheckGB.setObjectName("CheckGB")

        # 結果出力用　TextEdit
        self.textboxForResult = QtWidgets.QPlainTextEdit(self.CheckGB)
        self.textboxForResult.setGeometry(QtCore.QRect(10, 30, 261, 381))
        self.textboxForResult.setObjectName("textboxForResult")

        # バージョンんチェック Btn
        self.verCheckBtn = QtWidgets.QPushButton(self.CheckGB)
        self.verCheckBtn.setGeometry(QtCore.QRect(10, 420, 261, 23))
        self.verCheckBtn.setObjectName("verCheckBtn")
        self.envCheckBtn = QtWidgets.QPushButton(self.CheckGB)
        self.envCheckBtn.setGeometry(QtCore.QRect(10, 450, 261, 23))
        self.envCheckBtn.setObjectName("envCheckBtn")

        # Log GroupBox
        self.logGB = QtWidgets.QGroupBox(self.centralwidget)
        self.logGB.setGeometry(QtCore.QRect(310, 10, 241, 231))
        self.logGB.setObjectName("logGB")

        # Log取得 List
        self.SelectDeviceForLog = QtWidgets.QListWidget(self.logGB)
        self.SelectDeviceForLog.setGeometry(QtCore.QRect(10, 50, 221, 131))
        self.SelectDeviceForLog.setObjectName("SelectDeviceForLog")
        item = QtWidgets.QListWidgetItem()
        self.SelectDeviceForLog.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.SelectDeviceForLog.addItem(item)

        # Log取得 Btn
        self.getLogBtn = QtWidgets.QPushButton(self.logGB)
        self.getLogBtn.setGeometry(QtCore.QRect(150, 190, 75, 23))
        self.getLogBtn.setObjectName("getLogBtn")

        # Log取得 'Devices List' Label
        self.deviceListLabelForLog = QtWidgets.QLabel(self.logGB)
        self.deviceListLabelForLog.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.deviceListLabelForLog.setObjectName("deviceListLabelForLog")

        # 環境変更 GroupBox
        self.envChangeGB = QtWidgets.QGroupBox(self.centralwidget)
        self.envChangeGB.setGeometry(QtCore.QRect(310, 250, 241, 251))
        self.envChangeGB.setObjectName("envChangeGB")

        #  環境変更 ComboBox
        self.envChangeCB = QtWidgets.QComboBox(self.envChangeGB)
        self.envChangeCB.setGeometry(QtCore.QRect(10, 180, 221, 20))
        self.envChangeCB.setToolTipDuration(-2)
        self.envChangeCB.setObjectName("Select device server")
        self.envChangeCB.addItem("Real")
        self.envChangeCB.addItem("RC")
        self.envChangeCB.addItem("Beta")
        self.envChangeCB.addItem("Alpha")

        #  環境変更 Btn
        self.envChangeBtn = QtWidgets.QPushButton(self.envChangeGB)
        self.envChangeBtn.setGeometry(QtCore.QRect(160, 210, 75, 23))
        self.envChangeBtn.setObjectName("envChangeBtn")

        # 環境変更 List
        self.SelectDeviceForEnvChange = QtWidgets.QListWidget(self.envChangeGB)
        self.SelectDeviceForEnvChange.setGeometry(QtCore.QRect(10, 40, 221, 131))
        self.SelectDeviceForEnvChange.setObjectName("SelectDeviceForEnvChange")
        item = QtWidgets.QListWidgetItem()
        self.SelectDeviceForEnvChange.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.SelectDeviceForEnvChange.addItem(item)

        # Log取得 'Devices List' Label
        self.label = QtWidgets.QLabel(self.envChangeGB)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")

        # Btn Event
        self.envCheckBtn.clicked.connect(self.envCheckBtn_on_click)
        self.verCheckBtn.clicked.connect(self.verCheckBtn_on_click)
        self.envChangeBtn.clicked.connect(self.envChangeBtn_on_click)
        self.getLogBtn.clicked.connect(self.getLogBtn_on_click)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clova ADB Command Controller"))

        self.CheckGB.setTitle(_translate("MainWindow", "Check"))
        self.verCheckBtn.setText(_translate("MainWindow", "Version　Check"))
        self.envCheckBtn.setText(_translate("MainWindow", "Server Check"))
        self.logGB.setTitle(_translate("MainWindow", "Get Log File"))

        __sortingEnabled = self.SelectDeviceForLog.isSortingEnabled()
        self.SelectDeviceForLog.setSortingEnabled(False)

        firstDevice = os.popen('adb devices').read().split('\n')[1].split('\t')[0]
        secondDevice = os.popen('adb devices').read().split('\n')[2].split('\t')[0]

        item = self.SelectDeviceForLog.item(0)
        item.setText(_translate("MainWindow", firstDevice))
        item = self.SelectDeviceForLog.item(1)
        item.setText(_translate("MainWindow", secondDevice))

        self.SelectDeviceForLog.setSortingEnabled(__sortingEnabled)

        self.getLogBtn.setText(_translate("MainWindow", "Execute"))
        self.deviceListLabelForLog.setText(_translate("MainWindow", "Device　Lisｔ"))
        self.envChangeGB.setTitle(_translate("MainWindow", "Change Server"))
        self.envChangeCB.setItemText(0, _translate("MainWindow", "Select device server"))
        self.envChangeCB.setItemText(1, _translate("MainWindow", "Real"))
        self.envChangeCB.setItemText(2, _translate("MainWindow", "RC"))
        self.envChangeCB.setItemText(3, _translate("MainWindow", "Beta"))
        self.envChangeCB.setItemText(4, _translate("MainWindow", "Alpha"))

        self.envChangeBtn.setText(_translate("MainWindow", "Execute"))
        __sortingEnabled = self.SelectDeviceForEnvChange.isSortingEnabled()
        self.SelectDeviceForEnvChange.setSortingEnabled(False)

        item = self.SelectDeviceForEnvChange.item(0)
        item.setText(_translate("MainWindow", firstDevice))
        item = self.SelectDeviceForEnvChange.item(1)
        item.setText(_translate("MainWindow", secondDevice))

        self.SelectDeviceForEnvChange.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Device　Lisｔ"))
        self.actionabout.setText(_translate("MainWindow", "about"))

    @pyqtSlot()
    def envCheckBtn_on_click(self):
        envNo = ''  # CDK 서버 확인용 Flag 변수（3=Real, 4=stage, 5=dev, 9=alpha）
        envString = ''  # envNo > Display 문자변환용
        OtaServerEnv = ''  # OTA Server 확인용

        self.textboxForResult.clear()

        # Device 접속확인
        isDevices = os.popen('adb devices | find /i "device" /c').read()
        if int(isDevices) == 1:  # 디바이스 접속되지 않았을때
            QMessageBox.about(self, "Result: ", "No device connected !!")
            return None

        envNo = os.popen('adb shell cat /data/user/0/ai.clova.cdk.service/shared_prefs/Server.xml | findstr string').read()
        envNo = envNo[24]

        if envNo == '3':
            envString = 'REAL'
        elif envNo == '4':
            envString = 'STG'
        elif envNo == '5':
            envString = 'DEV'
        elif envNo == '9':
            envString = 'Alpha'

        OtaServerEnv = os.popen('adb shell cat /data/user/0/ai.clova.cdk.service/shared_prefs/FotaServerType.xml | findstr string')
        OtaServerEnv = OtaServerEnv.read().split('>')[1].split('<')[0]

        self.textboxForResult.insertPlainText('・Device環境: ' + envString +
                                              '\n\n・OTA向き: ' + OtaServerEnv)

        QMessageBox.about(self, "Result: ", '環境Check完了！')

    @pyqtSlot()
    def verCheckBtn_on_click(self):
        self.textboxForResult.clear()

        # 디바이스 접속확인
        isDevices = os.popen('adb devices | find        /i "device" /c').read()
        if int(isDevices) == 1: # No device connected
            QMessageBox.about(self, "Result: ", "No device connected !!")
            return None
        # 디바이스 종류확인
        modelname = os.popen('adb shell getprop ro.product.brand').read().split('\n')[0]
        # 접속 디바이스가 Clova DESK의 경우
        if modelname == 'DESK':
            os.popen('adb root')
            os.popen('timeout /t 2 > nul')
            # ADB 커맨드 날려서 값 취득
            fwver = os.popen('adb shell getprop ro.build.version.tag').read()
            fwtype = os.popen('adb shell getprop ro.build.type').read()
            cxfwver1 = os.popen('adb shell getprop persist.infr.cx_fwver').read()
            securityver = os.popen('adb shell getprop ro.build.version.security_patch').read()
            ffwver = os.popen('adb shell getprop ro.build.version.fw').read()
            cdkver = os.popen('adb shell dumpsys package ai.clova.cdk.service | findstr versionName').read().split('=')[1]
            appver = os.popen('adb shell dumpsys package ai.clova.display.app | findstr versionName').read().split('=')[1]
            linever = os.popen('adb shell dumpsys package ai.clova.app.line | findstr versionName').read().split('=')[1]
            systemuxver = os.popen('adb shell dumpsys package ai.clova.app.systemux | findstr versionName').read().split('=')[1]
            appdrivever = os.popen('adb shell dumpsys package ai.clova.display.app.drive | findstr versionName').read().split('=')[1]
            youtubever = os.popen('adb shell dumpsys package ai.clova.display.youtube | findstr versionName').read().split('=')[1]
            cameraver = os.popen('adb shell dumpsys package ai.clova.display.camera | findstr versionName').read().split('=')[1]
            # 화면에 뿌림
            self.textboxForResult.insertPlainText('・FW Version : ' + fwver +
                                                  '\n・FW Type : ' + fwtype +
                                                  '\n・Conexant FW : ' + cxfwver1 +
                                                  '\n・Security Ver : ' + securityver +
                                                  '\n・Build Ver : ' + ffwver +
                                                  '\n・CDK : ' + cdkver +
                                                  '\n・Display App : ' + appver +
                                                  '\n・LINE : ' + linever +
                                                  '\n・Systemux  : ' + systemuxver +
                                                  '\n・AppDrive : ' + appdrivever +
                                                  '\n・Youtube  : ' + youtubever +
                                                  '\n・Camera : ' + cameraver)
        # 접속 디바이스가 Clova Friends인 경우
        elif modelname == 'FRIENDSMINI' or 'FRIENDS':
            devicesNo = os.popen('adb devices').read().split('\n')[1].split('\t')[0]
            # ADB 커맨드 날려서 값 취득
            fwver = os.popen('adb shell getprop ro.build.version.tag').read()
            fwtype = os.popen('adb shell getprop ro.build.type').read()
            cxfwver1 = os.popen('adb shell getprop | findstr cx_fwver').read().split(':')[1].split('[')[1].split(']')[0]
            cdkver = os.popen('adb -s ' + devicesNo + ' shell  dumpsys package ai.clova.cdk.service | findstr versionName').read().split('=')[1]
            linever = os.popen('adb shell dumpsys package ai.clova.app.line | findstr versionName').read().split('=')[1]
            # 화면에 뿌림
            self.textboxForResult.insertPlainText('・Clova FW Version : ' + fwver +
                                                  '\n・Clova FW Version : ' + fwver +
                                                  '\n・Clova FW Mode : ' + fwtype +
                                                  '\n・Conexant FW Version : ' + cxfwver1 +
                                                  '\n\n・CDK Version: ' + cdkver +
                                                  '\n・Clova Line App : ' + linever)
        QMessageBox.about(self, "Result: ", 'Ver Check完了！')

    @pyqtSlot()
    def envChangeBtn_on_click(self):

        # Device 接続確認
        isDevices = os.popen('adb devices | find /i "device" /c').read()
        if int(isDevices) == 1: # No device connected
            QMessageBox.about(self, "Result: ", "No device connected !!")
            return None

        # ComboBox selected Item取得
        selectedDevice = self.SelectDeviceForEnvChange.currentItem().text()
        if selectedDevice == '':
            QMessageBox.about(self, "Result", "Please, Select Device!")
            return None

        selectedEnv = self.envChangeCB.currentText()
        if selectedEnv == '':
            QMessageBox.about(self, "Result", "Please, Select Server!")
            return None

        changeEnvTarget = ''
        if selectedEnv == 'Please, Select Server!':
            QMessageBox.about(self, "Result", "Please, Select Server!")
            return None
        elif selectedEnv == 'Production':
            changeEnvTarget = '3'
            serverType = 'real'
        elif selectedEnv == 'RC':
            changeEnvTarget = '4'
            serverType = 'stage'
        elif selectedEnv == 'Beta':
            changeEnvTarget = '5'
            serverType = 'dev'
        elif selectedEnv == 'Alpha':
            changeEnvTarget = '9'
            serverType = 'dev'

        os.popen('adb root')
        os.popen('timeout /t 2 > nul')
        os.popen('adb remount')
        os.popen('timeout /t 1 > nul')
        os.popen('adb shell am startservice -n ai.clova.cdk.service/.fota.FotaService -a SERVER -e type ' + serverType)
        os.popen('timeout /t 3 > nul')

        modelname = os.popen('adb shell getprop ro.product.brand').read()
        if modelname == 'DESK\n':
            os.popen('adb shell am start -a android.intent.action.VIEW -d clovadevice://server_setting/' + changeEnvTarget + ' ai.clova.display.app')
            os.popen('timeout /t 2 > nul')
        elif modelname == 'FRIENDSMINI ' or 'FRIENDS ':
            os.popen('adb shell am start -a android.intent.action.VIEW -d clovadevice://server_setting/' + changeEnvTarget)
            os.popen('timeout /t 2 > nul')

        QMessageBox.about(self, "Result", "Sever Changed to [Beta]\n Device will be reboot")

    @pyqtSlot()
    def getLogBtn_on_click(self):

        # 콤보박스 선택 아이템 취득
        selectedDevice = self.SelectDeviceForLog.currentItem().text()
        if selectedDevice == '':
            QMessageBox.about(self, "Result", "Please, select Device!")
            return None

        # 디바이스 접속확인
        isDevices = os.popen('adb devices | find /i "device" /c').read()
        if int(isDevices) == 1: # No device connected
            QMessageBox.about(self, "Result: ", "No device connected")
            return None

        os.popen('adb root')
        os.popen('timeout /t 2 > nul')

        # 클로바 모델 취득：Friends/Desk
        modelname = os.popen('adb shell getprop ro.product.brand').read().split('\n')[0]

        os.popen('adb -s' + selectedDevice + 'root')
        os.popen('adb logcat -P " "')
        os.popen('timeout /t 1 > nul')
        os.popen('cls')

        # Logcat 취득
        os.popen('adb logcat -d -v time > %userprofile%\Desktop\Log_' + modelname + '_%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%.txt')
        # CDK Log 취득(디바이스에서 직접 Pull)
        os.popen('adb pull /sdcard/logging/ %userprofile%\Desktop\CDK_' + modelname + '_%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%')

        QMessageBox.about(self, "Result: ", 'Successful log export. Check your Desktop')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())