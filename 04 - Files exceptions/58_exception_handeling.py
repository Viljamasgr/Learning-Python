# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("Can not divide by zero.")
except ValueError:
    print("Enter only numbers.")
except Exception:
    print("Something went wrong.")
finally:
    print("Do some cleanup here.")