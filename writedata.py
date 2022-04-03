#writedata.py
f = open(r"C:\Users\Stefano Bang\방대성\[1] 프로그램 작업 파일\Python 공부\newFile.txt",'w')
for i in range (1,11):      
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()
