import random

#16진수를 문자열로 취급하여 그 안의 수만 추출하여 정수화
def getNumber(stdData):
    numStr = ''
    for ch in stdData :
        if ch.isdigit() :
            numStr += ch

    return int(numStr)


data = []
i,k =0,0
n = 0

#2019038030 김진영

if __name__ == "__main__" :

    n = 10

    print("정렬 전 데이터 : ", end = "")

    #data 리스트 안에 10개의 임의의 16진수 생성
    for i in range(0, n) :
        tmp = hex(random.randrange(0, 100000))
        tmp = tmp[2:]
        data.append(tmp)
        print(data[i], " ", end ="")

    #선택 정렬
    for i in range(0, n-1) :
        for k in range(i+1, n) :
            if getNumber(data[i]) > getNumber(data[k]) :
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp
                
    print("\n정렬 후 데이터 : ", end = "")
    for i in range(0, n) :
        print(data[i], " ", end = "")

                
            
        

