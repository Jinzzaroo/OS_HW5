#정렬 전 문자열, 정렬 후 문자열
ss = ""
ssSwap = ""

if __name__ == "__main__":
    ss = input("문자열을 입력하세요 : ")

#2019038030 김진영
    
    #문자열의 길이만큼 실행시킨다. 만약 대문자면 소문자로, 소문자면 대문자로, 그 외엔 그대로 둔다.
    for i in range(0, len(ss)) :
        if ss[i] == ss[i].upper() :
            ssSwap += ss[i].lower()
        elif ss[i] == ss[i].lower() :
            ssSwap += ss[i].upper()
        else :
            ssSwap += ss[i]
    print("대소문자 변환 결과 --> ", ssSwap)
