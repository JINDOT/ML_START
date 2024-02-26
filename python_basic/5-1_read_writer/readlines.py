f = open("C:/pyBeginner/newFile.txt", 'r')
lines = f.readlines() # 1등, 2등,... list 생성
for line in lines: # list에 저장된 line들
    print(line) # 반복해서 출력
f.close