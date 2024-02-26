# coffee.py
coffee = 10 # 판매할 커피의 갯수
while True: # 조건에 false가 없으면 계속해서 반복
    money = int(input("insert coin ")) # money에 값 지정
    if money == 300: # 300원
        print("커피")
        coffee = coffee - 1 # coffee count -1
    elif money > 300: # 300원 초과
        print("커피" + ", 잔돈: %d 원" %(money - 300))
        coffee = coffee - 1
    elif money < 300: # 300원 미만
        print("금액부족. 결제를 취소합니다.")300
    if coffee == 0: # coffee count 0
        print("매진")
        break # 반복문 탈출

    # 무한루프
    # while True:
    #   수행 1

    # ctrl + c 로 종료