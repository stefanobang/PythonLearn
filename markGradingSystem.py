#markGradingSystem.py

marks = [90, 25, 67, 45, 80]
number = 0


for number in range(len(marks)):
    if marks[number] < 60:
        continue

    print("%d번 student passed the test! The student grade is %d" %(number+1,marks[number]))

#for mark in marks:
    #number += 1
    #if mark >= 60: 
        #print("%d student passed the test by %d!" %(number,mark))

    #else:
      #   continue 
       # print("%d student did not passed. The mark is %d!" %(number,mark))
