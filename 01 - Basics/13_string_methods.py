# String methods allow various operations on text input.
# These functions help modify, search, and validate user-provided strings.

name = input("Enter your full name: ")
phone_number = input("Enter your phone #: ")

# Get the length of the name
result = len(name)

# Find the first occurrence of 'o' in the name
result = name.find("o")

# Find the last occurrence of 'q' in the name
result = name.rfind("q")

# Capitalize the first letter of the name
name = name.capitalize()

# Convert the name to uppercase
name = name.upper()

# Convert the name to lowercase
name = name.lower()

# Check if the name consists only of digits (Fixed: 'ame' -> 'name')
result = name.isdigit()

# Check if the name consists only of alphabetic characters (Fixed: 'alpha()' -> 'isalpha()')
result = name.isalpha()

# Count occurrences of '-' in the phone number
result = phone_number.count("-")

# Remove hyphens from the phone number for clean formatting
phone_number = phone_number.replace("-", "")

print(phone_number)