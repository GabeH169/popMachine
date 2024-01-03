counter = 0

userValue = int(input("Enter an integer: "))
min = userValue
max = userValue
total = userValue

while userValue != -99999 :
    total += userValue
    counter += 1
    if userValue < min :
        min = userValue
    if userValue > max :
        max = userValue
    userValue = int(input("Enter an integer: "))

avg = total / counter
print("Your avg is:", avg, "your min is:", min, "your max is:", max)