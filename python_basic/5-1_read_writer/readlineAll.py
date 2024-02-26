f = open("C:/pyBeginner/newFile.txt", 'r')
while True:
    line = f.readline()
    if not line: break # line 없으면 탈출!
    print(line)
f.close()