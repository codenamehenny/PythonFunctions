#Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
#Task 1: Create functions for each arithmetic operation.

# 4 basic math operations add, subtract, multiply and divide. 
def add_numbers(first_number, second_number):
    return first_number + second_number

def subtract_numbers(first_number, second_number):
    return first_number - second_number

def multiply_numbers(first_number, second_number):
    return first_number * second_number

def divide_numbers(first_number, second_number):
    if first_number or second_number == 0:
        return "Error, can't divide by 0"  #satisfies the the divide by 0 error
    return first_number / second_number 

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
#user inputs type of operation and numbers
operation_type = input("What operation would you like to perform? Choose add, subtract, multiply, or divide: ")
first_number, second_number = int(input("What's the first number? ")), int(input("What's the second number? "))
# conditions with results according to operation and numbers given
if operation_type  == "add":
    print(f"{first_number} + {second_number} = {add_numbers(first_number, second_number)}")
elif operation_type == "subtract":
    print(f"{first_number} - {second_number} = {subtract_numbers(first_number, second_number)}")
elif operation_type == "multiply":
    print(f"{first_number} x {second_number} = {multiply_numbers(first_number, second_number)}")
elif operation_type == "divide":
    print(f"{first_number} ÷ {second_number} = {divide_numbers(first_number, second_number)}")
else:
    print("Please enter a valid input")

