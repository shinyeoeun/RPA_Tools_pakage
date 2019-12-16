# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import matplotlib.pyplot as plt
import pandas as pd
import time

class Ui_BuildFileSizeChecker(QWidget):

    def setupUi(self, BuildFileSizeChecker):

        # 윈도우 타이틀+테마
        BuildFileSizeChecker.setObjectName("BuildFileSizeChecker")
        BuildFileSizeChecker.resize(777, 618)
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
        self.ExecuteBtn.setGeometry(QtCore.QRect(160, 560, 171, 23))
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

        # 타겟플렛폼
        self.TargetPlatform = QtWidgets.QGroupBox(self.centralwidget)
        self.TargetPlatform.setGeometry(QtCore.QRect(30, 489, 301, 61))
        self.TargetPlatform.setObjectName("TargetPlatform")
        # 타겟플렛폼 체크박스:iOS
        self.TargetPlatformIosCheckBox = QtWidgets.QCheckBox(self.TargetPlatform)
        self.TargetPlatformIosCheckBox.setGeometry(QtCore.QRect(20, 30, 75, 16))
        self.TargetPlatformIosCheckBox.setObjectName("TargetPlatformIosCheckBox")
        # 타겟플렛폼 체크박스:Android
        self.TargetPlatformAndroidCheckBox = QtWidgets.QCheckBox(self.TargetPlatform)
        self.TargetPlatformAndroidCheckBox.setGeometry(QtCore.QRect(80, 30, 75, 16))
        self.TargetPlatformAndroidCheckBox.setObjectName("TargetPlatformAndroidCheckBox")
        # 내보내기:CSV
        self.ExportToCsvBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ExportToCsvBtn.setGeometry(QtCore.QRect(590, 530, 171, 23))
        self.ExportToCsvBtn.setObjectName("ExportToCsvBtn")
        # 내보내기:Excel
        self.ExportToExcel = QtWidgets.QPushButton(self.centralwidget)
        self.ExportToExcel.setGeometry(QtCore.QRect(590, 560, 171, 23))
        self.ExportToExcel.setObjectName("ExportToExcel")
        BuildFileSizeChecker.setCentralWidget(self.centralwidget)
        # 스테이터스바 없애면 화면 어그러짐
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
        self.TargetPlatform.setTitle(_translate("BuildFileSizeChecker", "Target Platform"))
        self.TargetPlatformIosCheckBox.setText(_translate("BuildFileSizeChecker", "iOS"))
        self.TargetPlatformAndroidCheckBox.setText(_translate("BuildFileSizeChecker", "Android"))
        self.ExportToCsvBtn.setText(_translate("BuildFileSizeChecker", "Export to CSV"))
        self.ExportToExcel.setText(_translate("BuildFileSizeChecker", "Export to Excel"))

    @pyqtSlot()
    def executeBtn_on_click(self):
        QMessageBox.about(self, "Info", "파일사이즈 데이터 수집을 시작합니다. 수집동안에는 PC조작을 삼가주세요")
        self.FileSizeIosTextField.clear()

        # App deploy login info
        DRIVER_PATH = 'lib/driver/chromedriver.exe'
        TARGET_URL = 'https://appdeploy.linecorp.com/'
        CONNECT_ID = self.idITextField.text()
        CONNECT_PW = self.pwTextField.text()

        # Target Build List
        target_build_android = []
        target_build_ios = self.targetBuildIosTextField.toPlainText().split('\n')

        # Android
        file_size_list_android = []
        file_size_list_android_raw_data = []
        # iOS
        file_size_list_iOS = []
        file_size_list_iOS_raw_data = []

        driver = webdriver.Chrome(DRIVER_PATH)

        # App Deploy 접속
        driver.get(TARGET_URL)
        # 약관 동의
        driver.find_element_by_class_name('agree-btn').click()
        # 서비스 검색란 입력: yuki
        driver.find_element_by_id("search").send_keys("yuki")
        driver.find_element_by_id("search").send_keys(Keys.ENTER)
        driver.implicitly_wait(3)
        # 서비스 리스트 아코디언 요소 탭
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="Public Service (0)"])[1]/following::div[5]')))
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Public Service (0)'])[1]/following::div[5]").click()
        # 서비스 리스트 탭: yuki
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         '(.//*[normalize-space(text()) and normalize-space(.)="Private Service (1)"])[1]/following::span[3]')))
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Private Service (1)'])[1]/following::span[3]").click()

        # iPhone 데이터 취득
        driver.get("https://appdeploy.linecorp.com/yuki/iphone/BETA")
        time.sleep(2)

        for index in target_build_ios:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'search')))
            driver.find_element_by_id("search").send_keys(index)
            time.sleep(2)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="RELEASE"])[1]/following::span[1]')))
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='RELEASE'])[1]/following::span[1]").click()
            time.sleep(1)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="EFFECT -"])[2]/following::i[1]')))
            driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='EFFECT -'])[2]/following::i[1]").click()
            time.sleep(1)

            # 첫 다운로드시에만 커넥트 로그인
            if index == target_build_ios[0]:
                driver.find_element_by_id('uid').send_keys(CONNECT_ID)
                driver.find_element_by_id('upw').send_keys(CONNECT_PW)
                driver.find_element_by_id('loginBtn').click()
                driver.implicitly_wait(5)
            time.sleep(2)

            driver.implicitly_wait(5)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'list')))
            table = driver.find_element_by_id('list')
            table_data = table.text
            file_size = table_data.split('sdk_size_ios.log')[1].split(' ')[1]
            file_size_list_iOS_raw_data.append(int(file_size))
            time.sleep(1)
            file_size_list_iOS.append(int(file_size[0:7]))
            driver.get("https://appdeploy.linecorp.com/yuki/iphone/BETA")
            driver.implicitly_wait(5)

        driver.quit()

        # 데이터프레임 작성
        data_ios = {'BuildVer': target_build_ios, 'ipaFileSize': file_size_list_iOS_raw_data}
        df = pd.DataFrame(data_ios, columns=['BuildVer', 'ipaFileSize'])
        print(df)

        self.FileSizeIosTextField.insertPlainText(df.to_string())

        # 그래프 표시
        plt.figure(figsize=(15, 7))
        plt.style.use(['seaborn-dark'])
        plt.plot(target_build_ios, file_size_list_iOS, color='blue', marker='o', linestyle="--")
        plt.grid()
        plt.title('yuki-Demo App file size')
        plt.ylabel("ipa file size(MB)")
        plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BuildFileSizeChecker = QtWidgets.QMainWindow()
    ui = Ui_BuildFileSizeChecker()
    ui.setupUi(BuildFileSizeChecker)
    BuildFileSizeChecker.show()
    sys.exit(app.exec_())

