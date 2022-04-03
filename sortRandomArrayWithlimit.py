import random

array = [0] * 20 #global value

def sortArray():
    total = 1
    final = 0
    min = 0
    max = 20
    i = 0
    aNum = 0

    while True:
        if min == 50:
            break
        num1 = random.randint(min+1,max)
        max = num1
     
        for x in range(min ,max+1):
            array[aNum] = x
            aNum = aNum + 1
        if min == 50:
            break
        else:
            print('[%d]-->'%total,end=" ")
            for y in range(0,aNum):
                print(array[y],end=" ")
            print(" ")
            min = max +1
            max = min + 20
            if(max>50):
                max = 50
            aNum = 0
            total = total +1


sortArray()

