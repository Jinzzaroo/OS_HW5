import operator

text = ""
countDic ={}
countList = []

if __name__ == "__main__" :
    
    #원문을 입력 받는다.
    text = input("원문\n")


    #원문 속 문자가 " "(공백)이 아닐 때 그리고 카운트하는 딕셔너리(countDic)안에 있을 때마다 1씩 카운트(증가)한다.
    for ch in text :
        if ch != " ":
            if ch in countDic :
                countDic[ch] += 1
            #처음 세는 거면 1로 둔다.
            else :
                countDic[ch] = 1
                
#2019038030 김진영

    #딕셔너리 배열을 값을 기준으로 내림차순 정렬한다.
    countList = sorted(countDic.items(), key = operator.itemgetter(1), reverse = True)

    print("--------------------------")
    print("문자\t빈도수")
    print("--------------------------")
    for i in range(0, len(countList)) :
        print(countList[i][0], "\t", countList[i][1])
