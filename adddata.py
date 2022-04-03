#adddata.py
f = open(r"C:\Users\Stefano Bang\방대성\[1] 프로그램 작업 파일\Python 공부\newFile.txt",'a')
for i in range(11,20):
    data = "%d 번째 줄입니다.\n" %i
    f.write(data)

f.close()
