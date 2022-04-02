#time, datetime 모듈
from time import *
from datetime import *

#date1과 date2의 날짜 차이값 반환
def countDays(date1, date2):
    retDays = 0
    #date1에 날짜 입력(연월일로 분리) 후 sDay 객체 생성
    year, month, day = date1.split('/')
    sDay = date(int(year), int(month), int(day))
    #date2에 날짜 입력(연월일로 분리) 후 eDay 객체 생성
    year, month, day = date2.split('/')
    eDay = date(int(year), int(month), int(day))
    diffDays = eDay - sDay
    #날짜 차이 반환(days 값으로 치환)
    retDays = diffDays.days
    return retDays

#해당 요일 추출
def getDays(t) :
    weeks = ['월', '화', '수', '목', '금', '토', '일']
    return weeks[t.tm_wday]

startDate, curDate, tm = '', '', None

#2019038030 김진영

if __name__ == "__main__" :
    startDate = input("시작 날짜(연/월/일) --> ")
    
    #현재 날짜 입력
    tm = localtime()
    curDate = str(tm.tm_year) + "/" + str(tm.tm_mon) + "/" + str(tm.tm_mday)

    print(startDate, "부터 오늘(", curDate, ")까지는 ", countDays(startDate, curDate), "일이 지났습니다.")
    print("그리고 오늘은", getDays(tm), "요일입니다.")
