import random
#things to do #4.1
def guessingGame():
    secret = random.randrange(10)+1
    print("Guess an integer between and including 1 to 10,or -1 to quit.")
    guessing = True
    while guessing:
        guess = int(input())
        if(guess==-1):
            break
        if(guess==secret):
            print("Congratulations!")
            break
        elif(guess>secret):
            print("Too high")
        else:
            print("Too low")
#things to do #4.2
def smallGreen():
    print("Is your choice small? True or false.")
    small = bool(input())
    print("Is your choice green? True or false.")
    green = bool(input())
    if(small):
        if(green):
            print("A small green object is a pea!")
        else:
            print("A small non-green object is a cherry!")
    else:
        if(green):
            print("A large green object is a watermelon!")
        else:
            print("A large non-green object is a pumpkin!")
#things to do 6.1
def printList():
    for x in [3,2,1,0]:
        print(x)
#things to do 6.2
def guessMe62():
    guessMe = 7
    number =1
    while(True):
        print("Number is",number)
        if(number <guessMe):
            print("Too low")
        if(number == guessMe):
            print("Found it")
        if(number>guessMe):
            print("oops")
            break
        number= number+1
def guessMe63():
    guessMe = 5
    number =1
    for number in range(10):
        print("Number is",number)
        if(number <guessMe):
            print("Too low")
        if(number == guessMe):
            print("Found it")
            break
        if(number>guessMe):
            print("oops")
            break            
guessingGame()
smallGreen()
printList()
guessMe62()
guessMe63()