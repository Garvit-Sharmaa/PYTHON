# Task 1: Calculate Factorial Using a Function   
# Problem Statement: Write a Python program that: 
# 1.   Defines a function named factorial that takes a number as an argument 
# and calculates its factorial using a loop or recursion. 
# 2.   Returns the calculated factorial. 
# 3.   Calls the function with a sample number and prints the output

n = int(input("enter a number to find factorial: "))
def factorial(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n * factorial(n-1)


print(f"factorial of number {n} is {factorial(n)}")

# OUTPUT:
# enter a number to find factorial: 7
# factorial of number 7 is 5040


# Task 2: Using the Math Module for Calculations 
  
# Problem Statement: Write a Python program that: 
# 1.   Asks the user for a number as input. 
# 2.   Uses the math module to calculate the: 
# o   Square root of the number 
# o   Natural logarithm (log base e) of the number 
# o   Sine of the number (in radians) 
# 3.   Displays the calculated results. 

import math 

num = float(input("enter your number:"))
sqrt = math.sqrt(num)
log = math.log (num)
sin = math.sin(num)
print(f"the sqrt of {num} is {sqrt}")
print(f"the log of the number {num} is {log}")
print(f"the sin of the number{num} is {sin}")
print(f"thankyou!")

# OUTPUT:
# the sqrt of 6.0 is 2.449489742783178
# the log of the number 6.0 is 1.791759469228055
# the sin of the number6.0 is -0.27941549819892586
# thankyou!