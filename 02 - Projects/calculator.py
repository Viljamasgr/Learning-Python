# Python Calculator
# A simple program that performs basic arithmetic operations (+, -, *, /)

# Get user input for the operator and numbers
operator = input("Enter an operator (+, -, *, /): ")  # User chooses an operation
num1 = float(input("Enter first number: "))  # Convert input to float for decimal calculations
num2 = float(input("Enter second number: "))  # Convert input to float for decimal calculations

# Perform the selected arithmetic operation
if operator == "+":
    result = num1 + num2  # Addition
    print("The result is:", result)
elif operator == "-":
    result = num1 - num2  # Subtraction
    print("The result is:", result)
elif operator == "*":
    result = num1 * num2  # Multiplication
    print("The result is:", result)
elif operator == "/":
    if num2 == 0:  # Prevent division by zero error
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2  # Division
        print("The result is:", result)
else:
    print("Invalid operator! Please enter one of (+, -, *, /)")
