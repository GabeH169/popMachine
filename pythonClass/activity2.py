import random
MAXNUM = 20

userNum = int(input("Choose a number between 1 and 20: "))
randNum = random.randint(1, MAXNUM)

while userNum != randNum :
    if userNum > randNum :
        print("Guess is too high")
        userNum = int(input("Choose a number between 1 and 20: "))
    else :
        print("Guess is too low")
        userNum = int(input("Choose a number between 1 and 20: "))

print("You got it right,", randNum)