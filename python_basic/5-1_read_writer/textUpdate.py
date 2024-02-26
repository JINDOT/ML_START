# textUpdate.py
f = open("C:/pyBeginner/newFile.txt", 'a')
for i in range(11,20):
    data = "%d 등!!! \n" %i
    f.write(data)
f.close()
