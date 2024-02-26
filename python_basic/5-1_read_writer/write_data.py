# write_data.py
f = open("C:/pyBeginner/newFile.txt", 'w')
for i in range(1, 11):
    data = "%d 등!!! \n" % i
    f.write(data)
f.close