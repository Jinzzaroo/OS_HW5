q,r = 0,0

#10진수 -> 2진수
#입력받은 10진수를 몫이 1이 될 때까지 2로 나눈다.
#몫이 1이 되면 몫과 나머지 출력 그리고 스택에 쌓인 나머지 출력
def base2(decNum) :
    q = decNum//2
    r = decNum%2
    
    if q >1 :
        base2(q)
        print(r, " ", end = "")
        
    else :
        print(q, " ", end = "")
        print(r, " ", end = "")

#10진수 -> 8진수
#입력받은 10진수를 몫이 8이하가 될 때까지 8로 나눈다.
#몫이 8이하가 되면 몫과 나머지 출력 그리고 스택에 쌓인 나머지 출력
def base8(decNum) :
    q = decNum//8
    r = decNum%8
    
    if q >7 :
        base8(q)
        print(r, " ", end = "")
        
    else :
        print(q, " ", end = "")
        print(r, " ", end = "")

#10진수 -> 16진수
#입력받은 10진수를 몫이 16이하가 될 때까지 16로 나눈다.
#몫이 16이하가 되면 몫과 나머지 출력 그리고 스택에 쌓인 나머지 출력
def base16(decNum) :
    q = decNum//16
    r = decNum%16

    if r == 10 :
        r = 'A'
    elif r == 11 :
        r = 'B'
    elif r == 12:
        r = 'C'
    elif r == 13:
        r = 'D'
    elif r == 14:
        r = 'E'
    elif r == 15:
        r = 'F'
        
    if q >15 :
        base16(q)
        print(r, " ", end = "")
        
    else :
        print(q, " ", end = "")
        print(r, " ", end = "")


#2019038030 김진영
        
if __name__ == "__main__" :
    decNum = int(input("10진수 입력 --> "))
    print("\n2진수 : ", end = "")
    base2(decNum)
    print("\n8진수 : ", end = "")
    base8(decNum)
    print("\n16진수 : ", end = "")
    base16(decNum)
    
    
