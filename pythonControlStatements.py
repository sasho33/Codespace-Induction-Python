# Activity 1: Number Checker
def oneA(num1, num2, num3):

    if (num1 != num2 and num1 != num3 and num2 != num3): # checking if all numbers are different
        print("All numbers are different.")
    elif (num1 == num2 and num1 == num3): # checking if all numbers are equal
        print("All numbers are equal")
    else:
        print("Neither all are equal or different")
oneA(2,3,4)

# Activity 2: Number Sequence Checker
def twoA(num1, num2, num3):
    
    if(num1 < num2 < num3):
        print("Increasing order")
    elif(num1 > num2 > num3):
        print("Decreasing order")
    else:
        print("Neither increasing or decreasing order")
twoA(1524,2345,3321)