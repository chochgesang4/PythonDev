#Author:Christopher Hochgesang
#Filename: M02 lab.py
#Prints stuff depending on a while

#bool to control the while looping, ZZZ also makes this false.
looping = True
while(looping):
    #read last name
    print("Enter a student's last name. ZZZ will terminate the program")
    lastName = input()
    #processRecords is a bool to restrict access to the post-execution stop lines, set to false if student's last name is ZZZ
    processRecords = True
    if lastName == "ZZZ":
        processRecords = False
        looping = False
    if processRecords:
        print("Enter a student's first name.")
        firstName=input()
        print("Enter a student's GPA.")
        GPA=float(input())
        print (firstName,lastName,"has a GPA of",GPA)
        if GPA >= 3.25:
            print (firstName,lastName,"Has made the Honor Roll")
        if GPA >= 3.5:
            print (firstName,lastName,"Has made the Dean's list!")