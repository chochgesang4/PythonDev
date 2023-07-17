from datetime import date
import os
import subprocess
import multiprocessing
import random
import time
#13.1
today = date.today()
file =""
if(os.path.exists("dateFile.txt")):
    file = open("dateFile.txt","r+")
else:
    file = open("dateFile.txt","x")
    file = open("dateFile.txt","r+")
print(today,file=file)
file.close()

#13.2
readFile = open("dateFile.txt","r")
today_string = readFile.read()
print("today_string:",today_string)
readFile.close()

#13.3
readFile = open("dateFile.txt","r")
today_string = readFile.read()
todayDateList=today_string.split("-")
todayDate = date(int(todayDateList[0]),int(todayDateList[1]),int(todayDateList[2]))
print("todayDate:",todayDate)


#15.1
def printtime():
    #waits between 0 and 1 seconds to print the current time
    time.sleep(random.random())
    print(time.time())
if __name__=="__main__":
    for x in range(3):
        p = multiprocessing.Process(target=printtime,)
        p.start()