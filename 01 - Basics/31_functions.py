# function = A block of reusable code
#            place () after the function name to invoke it

def display_invoice (username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of £{amount} is due: {due_date}")

display_invoice("JohnSmith123", 100.01, "01/02/2026")


# return = statement used to end a function
#          and send a result back to the caller

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)