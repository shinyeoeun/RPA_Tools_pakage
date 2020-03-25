# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import matplotlib.pyplot as plt
import pandas as pd
import time

class _fileSizeScrapperWithoutGUI():

    # App deploy login info
    TARGET_URL = '### confidential ###'
    CONNECT_ID = '### confidential ###'
    CONNECT_PW = '### confidential ###'

    # Target Build List
    target_build_android = ["2.16.1.1423", "2.16.1.1425", "2.16.1.1426"]
    target_build_ios = ["2.16.1.1423"]

    # path
    DRIVER_PATH = 'lib/driver/chromedriver.exe'

    # Android
    file_size_list_android = []
    file_size_list_android_raw_data = []
    # iOS
    file_size_list_iOS = []
    file_size_list_iOS_raw_data = []
    driver = webdriver.Chrome(DRIVER_PATH)

    def access_target_url(self):
        # App Deploy 접속
        self.driver.get(self.TARGET_URL)
        # 약관 동의
        self.driver.find_element_by_class_name('agree-btn').click()
        # 서비스 검색란 입력: yuki
        self.driver.find_element_by_id("search").send_keys("yuki")
        self.driver.find_element_by_id("search").send_keys(Keys.ENTER)
        self.driver.implicitly_wait(3)
        # 서비스 리스트 아코디언 요소 탭
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="Public Service (0)"])[1]/following::div[5]')))
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Public Service (0)'])[1]/following::div[5]").click()
        # 서비스 리스트 탭: yuki
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         '(.//*[normalize-space(text()) and normalize-space(.)="Private Service (1)"])[1]/following::span[3]')))
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Private Service (1)'])[1]/following::span[3]").click()

    def get_android_data(self):
        # 플랫폼 리스트 탭: Android
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="iPhone"])[1]/following::div[5]')))
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='iPhone'])[1]/following::div[5]").click()
        self.driver.implicitly_wait(5)
        time.sleep(2)

        for index in self.target_build_android:
            # 검색창에 타겟빌드 리스트의 빌드 입력
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'search')))
            self.driver.find_element_by_id("search").send_keys(index)
            time.sleep(2)

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="RELEASE"])[1]/following::span[1]')))
            self.driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='RELEASE'])[1]/following::span[1]").click()
            self.driver.implicitly_wait(5)
            time.sleep(2)

            # 다운로드 버튼 탭
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="EFFECT -"])[2]/following::i[1]')))
            self.driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='EFFECT -'])[2]/following::i[1]").click()
            time.sleep(1)

            # 첫 다운로드시에만 커넥트 로그인
            if index == self.target_build_android[0]:
                self.driver.find_element_by_id('uid').send_keys(self.CONNECT_ID)
                self.driver.find_element_by_id('upw').send_keys(self.CONNECT_PW)
                self.driver.find_element_by_id('loginBtn').click()
                self.driver.implicitly_wait(5)
            time.sleep(2)
            self.driver.implicitly_wait(5)

            # 테이블 값 취득
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'list')))
            table = self.driver.find_element_by_id('list')
            table_data = table.text
            # 테이블 값에서 파일사이즈 추출
            file_size = table_data.split('sdk_size_android.log')[1].split(' ')[1]
            self.file_size_list_android_raw_data.append(int(file_size))
            time.sleep(1)
            # 파일사이즈 리스트에 추가 (파일사이즈는 7자리수만 표시)
            self.file_size_list_android.append(int(file_size[0:7]))
            # 바이너리 리스트 페이지로 복귀
            self.driver.get("https://appdeploy.linecorp.com/yuki/android/BETA")
            self.driver.implicitly_wait(5)

    def get_ios_data(self):

        # iPhone 데이터 취득
        self.driver.get("https://appdeploy.linecorp.com/yuki/iphone/BETA")
        time.sleep(2)

        for index in self.target_build_ios:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'search')))
            self.driver.find_element_by_id("search").send_keys(index)
            time.sleep(2)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="RELEASE"])[1]/following::span[1]')))
            self.driver.find_element_by_xpath("xpath=(.//*[normalize-space(text()) and normalize-space(.)='RELEASE'])[1]/following::span[1]").click()
            time.sleep(1)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, '(.//*[normalize-space(text()) and normalize-space(.)="EFFECT -"])[2]/following::i[1]')))
            self.driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='EFFECT -'])[2]/following::i[1]").click()
            time.sleep(1)
            self.driver.implicitly_wait(5)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'list')))
            table = self.driver.find_element_by_id('list')
            table_data = table.text
            file_size = table_data.split('sdk_size_ios.log')[1].split(' ')[1]
            self.file_size_list_iOS_raw_data.append(int(file_size))
            time.sleep(1)
            self.file_size_list_iOS.append(int(file_size[0:7]))
            self.driver.get("https://appdeploy.linecorp.com/yuki/iphone/BETA")
            self.driver.implicitly_wait(5)

    def generate_report(self):

        # 데이터프레임 작성
        data_ios = {'BuildVer': self.target_build_ios, 'ipaFileSize': self.file_size_list_iOS_raw_data}
        df = pd.DataFrame(data_ios, columns=['BuildVer', 'ipaFileSize'])
        df.to_html('fileSize_ios.html')
        print(df)
        data_android = {'BuildVer': self.target_build_android,'apkFileSize': self.file_size_list_android_raw_data}
        df = pd.DataFrame(data_android, columns=['BuildVer', 'apkFileSize'])
        df.to_html('fileSize_android.html')
        print(df)

        # 그래프 표시
        plt.figure(figsize=(15, 7))
        plt.style.use(['seaborn-dark'])
        plt.subplot(2, 1, 1)
        plt.plot(self.target_build_ios, self.file_size_list_iOS, color='blue', marker='o', linestyle="--")
        plt.grid()
        plt.title('yuki-Demo App file size')
        plt.ylabel("ipa file size(MB)")
        plt.subplot(2, 1, 2)
        plt.plot(self.target_build_android, self.file_size_list_android, color='green', marker='o', linestyle="--")
        plt.grid()
        plt.ylabel("apk file size(MB)")
        plt.xlabel('Build ver')
        plt.show()

if __name__ == '__main__':
    getFileSize().access_target_url()
    getFileSize().get_android_data()
    getFileSize().get_ios_data()
    getFileSize().generate_report()
    getFileSize().driver.quit()