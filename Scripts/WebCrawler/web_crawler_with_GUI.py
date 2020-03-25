# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from selenium import webdriver
import matplotlib.pyplot as plt
import pandas as pd


class Ui_BuildFileSizeChecker(QWidget):

    def setupUi(self, BuildFileSizeChecker):

        # 윈도우 타이틀+테마
        BuildFileSizeChecker.setObjectName("BuildFileSizeChecker")
        BuildFileSizeChecker.resize(777, 580)
        # BuildFileSizeChecker.setStyleSheet(open("lib/style.qss", "r").read())
        #BuildFileSizeChecker.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(BuildFileSizeChecker)
        self.centralwidget.setObjectName("centralwidget")

        # 로그인정보
        self.LoginInfoGb = QtWidgets.QGroupBox(self.centralwidget)
        self.LoginInfoGb.setGeometry(QtCore.QRect(30, 20, 301, 61))
        self.LoginInfoGb.setObjectName("LoginInfoGb")
        # 로그인:ID
        self.ID = QtWidgets.QLabel(self.LoginInfoGb)
        self.ID.setGeometry(QtCore.QRect(10, 30, 50, 12))
        self.ID.setObjectName("ID")
        self.idITextField = QtWidgets.QLineEdit(self.LoginInfoGb)
        self.idITextField.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.idITextField.setObjectName("idITextField")  # 로그인 텍스트필드
        # 로그인:Password
        self.PW = QtWidgets.QLabel(self.LoginInfoGb)
        self.PW.setGeometry(QtCore.QRect(160, 30, 16, 16))
        self.PW.setObjectName("PW")
        self.pwTextField = QtWidgets.QLineEdit(self.LoginInfoGb)
        self.pwTextField.setGeometry(QtCore.QRect(180, 30, 113, 20))
        self.pwTextField.setObjectName("pwTextField")   # 패스워드 텍스트필드
        self.pwTextField.setEchoMode(QtWidgets.QLineEdit.Password)

        # 타겟빌드
        self.TargetBuildGb = QtWidgets.QGroupBox(self.centralwidget)
        # 타겟빌드: iOS
        self.TargetBuildGb.setGeometry(QtCore.QRect(30, 90, 301, 381))
        self.TargetBuildGb.setObjectName("TargetBuildGb")
        self.targetBuildIos = QtWidgets.QGroupBox(self.TargetBuildGb)
        self.targetBuildIos.setGeometry(QtCore.QRect(20, 20, 120, 341))
        self.targetBuildIos.setObjectName("targetBuildIos")
        self.targetBuildIosTextField = QtWidgets.QTextEdit(self.targetBuildIos)
        self.targetBuildIosTextField.setGeometry(QtCore.QRect(10, 20, 104, 311))
        self.targetBuildIosTextField.setObjectName("targetBuildIosTextField")  # 아이폰빌드 텍스트필드
        # 타겟빌드: Android
        self.targetBuildAndroid = QtWidgets.QGroupBox(self.TargetBuildGb)
        self.targetBuildAndroid.setGeometry(QtCore.QRect(160, 20, 120, 341))
        self.targetBuildAndroid.setObjectName("targetBuildAndroid")
        self.targetBuildAndroidTextField = QtWidgets.QTextEdit(self.targetBuildAndroid)
        self.targetBuildAndroidTextField.setGeometry(QtCore.QRect(10, 20, 104, 311))
        self.targetBuildAndroidTextField.setObjectName("targetBuildAndroidTextField")  # 안드로이드빌드 텍스트필드

        # 실행버튼
        self.ExecuteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ExecuteBtn.setGeometry(QtCore.QRect(100, 490, 171, 60))
        self.ExecuteBtn.setObjectName("ExecuteBtn")

        # 파일사이즈 로우데이터
        self.FileSizeRawDataGb = QtWidgets.QGroupBox(self.centralwidget)
        self.FileSizeRawDataGb.setGeometry(QtCore.QRect(350, 90, 411, 381))
        self.FileSizeRawDataGb.setObjectName("FileSizeRawDataGb")
        # 파일사이즈 로우데이터:iOS
        self.FileSizeIos = QtWidgets.QGroupBox(self.FileSizeRawDataGb)
        self.FileSizeIos.setGeometry(QtCore.QRect(20, 20, 181, 341))
        self.FileSizeIos.setObjectName("FileSizeIos")
        self.FileSizeIosTextField = QtWidgets.QTextEdit(self.FileSizeIos)
        self.FileSizeIosTextField.setGeometry(QtCore.QRect(10, 20, 161, 311))
        self.FileSizeIosTextField.setObjectName("FileSizeIosTextField")
        # 파일사이즈 로우데이터:Android
        self.FileSizeAndroid = QtWidgets.QGroupBox(self.FileSizeRawDataGb)
        self.FileSizeAndroid.setGeometry(QtCore.QRect(220, 20, 181, 341))
        self.FileSizeAndroid.setObjectName("FileSizeAndroid")
        self.FileSizeAndroidTextField = QtWidgets.QTextEdit(self.FileSizeAndroid)
        self.FileSizeAndroidTextField.setGeometry(QtCore.QRect(10, 20, 161, 311))
        self.FileSizeAndroidTextField.setObjectName("FileSizeAndroidTextField")

        BuildFileSizeChecker.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BuildFileSizeChecker)
        self.statusbar.setObjectName("statusbar")
        BuildFileSizeChecker.setStatusBar(self.statusbar)

        # 버튼이벤트
        self.ExecuteBtn.clicked.connect(self.executeBtn_on_click)

        self.retranslateUi(BuildFileSizeChecker)
        QtCore.QMetaObject.connectSlotsByName(BuildFileSizeChecker)

    def retranslateUi(self, BuildFileSizeChecker):
        _translate = QtCore.QCoreApplication.translate
        BuildFileSizeChecker.setWindowTitle(_translate("BuildFileSizeChecker", "Build File Size Checker"))
        self.LoginInfoGb.setTitle(_translate("BuildFileSizeChecker", "Login Info"))
        self.ID.setText(_translate("BuildFileSizeChecker", "ID"))
        self.PW.setText(_translate("BuildFileSizeChecker", "PW"))
        self.ExecuteBtn.setText(_translate("BuildFileSizeChecker", "Execute"))
        self.TargetBuildGb.setTitle(_translate("BuildFileSizeChecker", "Target Build"))
        self.targetBuildIos.setTitle(_translate("BuildFileSizeChecker", "iOS"))
        self.targetBuildAndroid.setTitle(_translate("BuildFileSizeChecker", "Android"))
        self.FileSizeRawDataGb.setTitle(_translate("BuildFileSizeChecker", "File Size Raw Data"))
        self.FileSizeIos.setTitle(_translate("BuildFileSizeChecker", "iOS"))
        self.FileSizeAndroid.setTitle(_translate("BuildFileSizeChecker", "Android"))

    @pyqtSlot()
    def executeBtn_on_click(self):
        QMessageBox.about(self, "Info", "파일사이즈 데이터 수집을 시작합니다. 수집동안에는 PC조작을 삼가주세요")
        self.FileSizeIosTextField.clear()

        # App deploy login info
        DRIVER_PATH = 'lib/driver/chromedriver.exe'
        TARGET_URL = 'https://appdeploy.linecorp.com/'
        CONNECT_ID = self.idITextField.text()
        CONNECT_PW = self.pwTextField.text()
        driver = webdriver.Chrome(DRIVER_PATH)
        # Target Build List
        target_build_android = self.targetBuildAndroidTextField.toPlainText().split('\n')
        target_build_ios = self.targetBuildIosTextField.toPlainText().split('\n')
        # Android
        file_size_list_android = []
        file_size_list_android_raw_data = []
        # iOS
        file_size_list_iOS = []
        file_size_list_iOS_raw_data = []

        ##### web driver 조작 시작
        driver.get(TARGET_URL)  # App Deploy 접속
        # 약관동의
        driver.find_element_by_class_name('agree-btn').click()  # 약관 동의

        for index in target_build_ios:
            # 빌드페이지 1 접속
            driver.get(TARGET_URL + "/download/yuki/iphone/" + index + "/beta/")

            # 커넥트 로그인
            if index == target_build_ios[0]:
                driver.find_element_by_id('uid').send_keys(CONNECT_ID)
                driver.find_element_by_id('upw').send_keys(CONNECT_PW)
                driver.find_element_by_id('loginBtn').click()
            driver.implicitly_wait(5)

            # 빌드페이지 2 접속
            driver.find_element_by_xpath("//*[@id='list']/tbody/tr[2]/td[1]/a").click()
            driver.implicitly_wait(5)
            # 테이블 텍스트 취득 > 파일사이즈 취득
            table_data = driver.find_element_by_id('list').text
            file_size = table_data.split('sdk_size_ios.log')[1].split(' ')[1]
            # Raw Data 저장
            file_size_list_iOS_raw_data.append(int(file_size))
            # 그래프표시용 값으로 변환 후 저장
            file_size_list_iOS.append(int(file_size[0:7]))

        # Android 데이터 취득
        for index in target_build_android:
            driver.get(TARGET_URL + "/download/yuki/android/" + index + "/beta/")

            driver.find_element_by_xpath("//*[@id='list']/tbody/tr[2]/td[1]/a").click()
            driver.implicitly_wait(5)
            table_data = driver.find_element_by_id('list').text
            file_size = table_data.split('sdk_size_android.log')[1].split(' ')[1]
            file_size_list_android_raw_data.append(int(file_size))
            file_size_list_android.append(int(file_size[0:7]))

        driver.quit()
        ##### web driver 조작 끝

        # Raw Data 데이터프레임 작성
        data_android = {'Build ver.': target_build_android, 'File Size': file_size_list_android_raw_data}
        df_android = pd.DataFrame(data_android, columns=['Build ver.', 'File Size'])
        data_ios = {'Build ver.': target_build_ios, 'File Size': file_size_list_iOS_raw_data}
        df_ios = pd.DataFrame(data_ios, columns=['Build ver.', 'File Size'])

        # Raw Data 화면출력
        self.FileSizeIosTextField.insertPlainText(df_ios.to_string())
        self.FileSizeAndroidTextField.insertPlainText(df_android.to_string())

        # 그래프 표시
        plt.figure(figsize=(15, 7))
        plt.style.use(['seaborn-dark'])
        plt.title('yuki-Demo App file size')
        plt.subplot(2, 1, 1)
        plt.ylabel("ipa file size(MB)")
        plt.plot(target_build_ios, file_size_list_iOS, color='blue', marker='o', linestyle="--")
        plt.grid()
        plt.subplot(2, 1, 2)
        plt.ylabel("apk file size(MB)")
        plt.plot(target_build_android, file_size_list_android, color='green', marker='o', linestyle="--")
        plt.grid()
        plt.xlabel('Build ver')
        plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BuildFileSizeChecker = QtWidgets.QMainWindow()
    ui = Ui_BuildFileSizeChecker()
    ui.setupUi(BuildFileSizeChecker)
    BuildFileSizeChecker.show()
    sys.exit(app.exec_())

