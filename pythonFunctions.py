# Functions are code blocks that only run when called
# Use the def keyword to create a function

# # Creating a function
# def firstFunction():
#     print("Hello world from function")

# # Calling a function
# firstFunction()

# # Passing in an argument to a function
# def myFunction(firstName):
#     print(firstName + " West")
# myFunction("Richard")
# myFunction("Robert")
# myFunction("Roger")

# # Using Return Values
# def myFunction(x):
#     return 10 * x
# print(myFunction(5))
# print(myFunction(10))
# print(myFunction(15))

# # Passing a list as an argument
# def myFunction(drinks):
#     for x in drinks:
#         print(x)
# alcoholic = ["mojito", "old fashioned", "martini, shaken not stirred"]
# myFunction(alcoholic)

# #==========

# # Activity 1: Contents and Max Values in Lists
# def showList(numList):
#     print("The content of the list is: ", numList) 

#     print("The max value in the list: ", max(numList)) # Using the max function to find max value
# sampleList = [10,2,3,4,7] # This list will be passed in as an arg (numList)
# showList(sampleList) # calling the showList function, and passing in sampleList

# #==========

# # Activity 2: Factorials

# def factorialCheck(x):

#     currentNum = 1 # Setting a local variable with the factorial result of 0
#     if x < 0: # Checking for 0
#         print("Not defined for negative numbers")
#     elif x == 0: # Checking for negatives
#         print(1)
#     else:
#         for x in range(1, x+1):
#             currentNum = currentNum * x # Recursively multiplies from 1 to x+1
#     print(currentNum)

# factorialCheck(6)

# #==========

# # Activity 3: Prime Check

# def primeChecker(x):
#     if x > 1: # Checks to make sure the number is positive and not 0 or 1
#         for i in range(2, int(x/2)+1): # Checks between 2 and n/2 
#             if (x % i) == 0: # checking modulo to make sure remainder isn't 0
#                 print("The number", x, "is not prime")
#                 break
#             else:
#                 print("The number", x, "is prime")
#                 break
#     else:
#         print("The number", x, "is not prime") # prints if x <= 1

# primeChecker(-1)
