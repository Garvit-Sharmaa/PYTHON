# Task 1: Perform Basic Mathematical Operations

# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.

a = float(input("enter first number :"))
b = float(input("enter second number :"))

Add = a+b

sub = a-b

mul = a * b 
div = a/b

print ("Addition of two numbers is :",Add)
print ("Subtraction of two numbers is :",sub)   
print ("Multiplication of two numbers is :",mul)
print ("Division of two numbers is :",div)


# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

first_name = input("enter your first name :")
last_name = input("enter your last name :")

full_name = first_name + " " + last_name

print (f" hello {full_name}, welcome to our website !")

