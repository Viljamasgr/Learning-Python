# Conditional expressions (ternary operators) provide a one-line shortcut for if-else statements.
# They allow printing or assigning one of two values based on a condition.
# Syntax: X if condition else Y

num = 5
a = 6
b = 6
age = 13
temperature = 20
user_role = "guest"

# Prints whether the number is positive or negative
print("Positive" if num > 0 else "Negative")

# Determines if the number is even or odd (fixed missing condition)
result = "EVEN" if num % 2 == 0 else "ODD"

# Assigns the maximum and minimum value between 'a' and 'b'
max_num = a if a > b else b
min_num = a if a < b else b

# Categorizes a person based on age
status = "Adult" if age >= 19 else "Child"

# Classifies weather temperature
weather = "HOT" if temperature > 20 else "COLD"

# Assigns access level based on user role
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)