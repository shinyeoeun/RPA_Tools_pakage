# RPA Tools pakage
반복노가다 업무 or 로그 분석업무등을 자동화하기 위한 시도들을 모아놓은 패키지<br/>

* Tool List
  1. 빌드별 파일사이즈 측정 자동화 
  2. LINE api Log Parser

## 1. 빌드별 파일사이즈 측정 자동화
앱 파일사이즈(apk/ipa)의 변동을 모니터링하기 위해<br/>
빌드배포 사이트에서 빌드의 파일사이즈값을 크롤링하여 그래프로 표시해주는 프로그램<br/>
사실 android-apk-size-watcher같은 젠킨스 플러그인 쓰면 되지만 RPA연습용으로 작성  

* Using Tools
  > PyQt5, Selenium, Pyinstaller, PowerMockup, matplotlib, pandas

### Usage
GUI 프로그램 실행파일(.exe) 클릭하여 아래와 같이 조작
![2020-03-24_12h48_37](https://user-images.githubusercontent.com/25470405/77386291-d35c8280-6dcd-11ea-8cd9-1b42f15362fa.png)

### Demo
![ezgif com-video-to-gif (1)](https://user-images.githubusercontent.com/25470405/77300000-b58d1000-6d30-11ea-98d9-eb412cd8724a.gif)

### Description
와이어프래임 작성 후 GUI프로그램으로 패키징 하기까지의 흐름
![2020-03-24_16h47_19](https://user-images.githubusercontent.com/25470405/77400826-2561d000-6def-11ea-9e96-962300b11184.png)

### Trouble Shooting

* PyQt 관련 
  + PyDesiner.exe 경로
  
    PyDesigner는 UI레이아웃을 하드코딩하는 시간을 절약시켜주지만 실행파일이 넘나 숨겨져있음<br/>
    삽질방지를 위해 경로를 메모해둠

    > C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python37\Lib\site-packages\pyqt5_tools\designer.exe

  + PyDesiner로 작성한 .ui파일을 .py로 컨버트 하는 커맨드
  
   ```sh
        pyuic5 {input 파일명}.ui -o {output 파일명}.py
   ```
    
  + pyqt 버튼이벤트 작성방법
  
    디자이너에서 생성된 코드를 동작시키려면 @pyqtSlot으로 event lisner를 작성해서 버튼에 연결시켜 줘야함
   ```python
      # 실행버튼 이벤트 
      @pyqtSlot()
      def executeBtn_on_click(self):
          QMessageBox.about(self, "Info", "파일사이즈 데이터 수집을 시작합니다. 수집동안에는 PC조작을 삼가주세요")
          # (중략)
          
      # 이벤트 연결    
      def setupUi(self, BuildFileSizeChecker):
          self.ExecuteBtn.clicked.connect(self.executeBtn_on_click)
    ```
* pyinstaller 관련
  + 로컬에 작성한 GUI프로그램을 다른사람들도 사용할수 있게 exe로 패키징해주는 커맨드
   ```sh
      pyinstaller --onefile {파일명}.py
   ```
  ※icon옵션지정으로 커스텀 이미지로 실행파일 아이콘변경도 가능


## 2. LINE api Log Parser
LINE api 로그를 파싱하여 테스트에 필요한 데이터수집 후 csv파일로 출력하는 스크립트
  * Using Tools
    > parse

* 로그추출값 리스트

  - 로그기록시간: YYYY-MM-DD hh:mm:ss
  - ID
  - 응답타입: res/req
  - 이벤트명
  - 소요시간(ms)
  - 결과: Success/Callback/Failure

### Usage
같은 폴더에 LINE_api_logParser.py와 타겟 로그파일을 넣은 뒤 아래 커맨드 입력
```sh
  python LINE_api_logParser.py {로그파일명} {출력파일명(.csv)}
```

### Result Sample
로그에서 추출된 값들이 csv에 작성됨
![2020-03-25_17h09_36](https://user-images.githubusercontent.com/25470405/77515336-b56d4b80-6ebb-11ea-9503-b16281d3e406.png)


### Demo
![2020-03-25_16h52_37](https://user-images.githubusercontent.com/25470405/77514103-8950cb00-6eb9-11ea-8907-23f64e0f3e43.gif)


### Description
parse패키지로 추출하는 처리는 아래와 같음

```python
  def parse(line):

      # LOG에서 추출하고자 하는 값이 포함된 문자열 존재여부 확인. 여기서는 ”elapsed”로 판단
      if line.find("elapsed") == -1:
          return

      # LOG 표시시각 취득
      time = line[0:19]

      # 추출대상 값들을 Parser의 {:w}로 파싱 > 각 값들은 배열로 반환됨
      result = search("[{:w}][id={:w}] {:w}[elapsed={:w}ms] result={:w}", line)

      # 파싱결과값들을 CSV형식으로 편집
      if result:
          data = time + "," + result[0] + "," + str(result[1]) + ","  + result[2] + ","  + str(result[3]) + ","  + result[4] + "\n"
          return data

      # 파싱에 실패한 라인 출력
      print("Error >> ".format(line))
      return
```
    

### References
* 예제로 배우는PyQt
> https://opentutorials.org/module/544/4998

* pyinstaller를 이용한 Python exe 실행 파일 만들기
> http://hongku.tistory.com/338

* parse 1.15.0
> https://pypi.org/project/parse/
