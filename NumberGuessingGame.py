import random

comp_number = random.randrange(10,20)
numsel = 0
tries = 0
while numsel != comp_number:
    numsel = int(input("insert a number between 10 and 20"))
    tries = tries + 1
    if  numsel < 10 or numsel  > 20:
        print("out of range")
    elif comp_number > numsel :
        print("number is smaller")
    elif comp_number < numsel :
        print("number is greater")   
    else:
        print("number matched")
print("number of tries" ,tries)
