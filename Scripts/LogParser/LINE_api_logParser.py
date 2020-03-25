# -*- coding: utf-8 -*-

import sys
from parse import *
from parse import compile

"""
LINE api 로그에서 아래의 값들을 추출

- 로그기록시간: YYYY-MM-DD hh:mm:ss
- ID
- 응답타입: res/req
- 이벤트명
- 소요시간(ms)
- 결과: Success/Callback/Failure

【 LOG SAMPLE 】
2020-03-24 17:32:45(pid=14069,tid=1354) : TalkApi (D) : [res][id=170997684] sendChatChecked[elapsed=55ms] result=Success[null]
"""

"""
csv 헤더 작성
"""
def get_csv_header():
    return "TIME,TYPE,ID,EVENT,ELAPSED(ms),RESULT"

"""
로그 파싱
"""
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

"""
csv파일 작성
@Param
input_file 파싱하려는 로그파일명
output_file 출력파일명(.csv)
"""
def write_csv(input_file, output_file):
    # csv파일 작성
    csv_name = output_file
    csv = open(csv_name, 'w', encoding='utf-8')

    # csv 헤더 작성
    csv_head = get_csv_header() + "\n"
    csv.write(csv_head)

    # 로그파일 파싱 및 csv파일에 기록
    with open(input_file, 'r', encoding='utf-8') as log:

        while True:
            # 로그 라인 존재여부 확인
            line = log.readline()
            if not line: break

            # 해당 라인에 파싱 키워드 존재여부 확인
            csv_data = parse(line)
            if csv_data:

                while True:
                    line = log.readline()
                    if not line: break

                    # csv 기록
                    value = parse(line)
                    if value:
                        csv_data += value
                        csv.write(csv_data)
                        break

    csv.close()
    print('    ====== End ======')
    print('    >> Intput={}'.format(input_file))
    print('    >> Outputs={}'.format(csv_name))
    return


if __name__=='__main__':
    print("    ====== Start ======")
    write_csv(sys.argv[1], sys.argv[2])
