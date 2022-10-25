# Activity 1: The Fibonacci Series
def fibonacciSeries():
    
    num1, num2 = 0, 1 # Setting the numbers

    while num1 <= 50: # while loop will run until num1 <= 50. 
        print(num1)
        num1, num2 = num2, num1 + num2 # takes num1 and makes it num2, takes num2 and makes it num1 + num2
fibonacciSeries()

# Activity 2: Multiplication Tables
def timesTable(num1):
    for x in range(1,11): # sets range to loop through
        print(num1," x ",x," = ",num1 * x) # uses commas to separate strings and variables
timesTable(6)