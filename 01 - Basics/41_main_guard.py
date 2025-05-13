# if __name__ == __main__: (this script can be imported OR run standalone)
#                          Functions and classes in this module can be reused
#                          without the main block of code executing
# Good practice (code is modular,
#                helps readability,
#                leaves no global variables,
#                avoid unintended execution)

# Ex. library = import library for functionality
#               When running directly, display a help page

def favourite_food(food):
    print(f"Your favourite food i {food}")

def main():
    print("This is script1")
    favourite_food("pizza")
    print("Goodbye.")

if __name__ == '__main__':
    main()
