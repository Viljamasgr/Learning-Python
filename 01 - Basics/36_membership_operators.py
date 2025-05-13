# Membership operators = used to test whether a value is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

email = "JohnSmith@gmail.com"

if "@" in email and "." in email:
    print("Valid email.")
else:
    print("Invalid email.")