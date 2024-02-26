# continue
# while문의 맨 처음으로 복귀
# 홀수 출력기
a = 0
while a < 10: # a가 10미만일 경우 반복, 이상일 경우 종료
    a = a + 1 # 반복문 실행마다 a count +1
    if a % 2 == 0: continue # 2를 나눈 나머지가 0이면 처음으로
    print(a) # 0이 아닌 경우 실행
