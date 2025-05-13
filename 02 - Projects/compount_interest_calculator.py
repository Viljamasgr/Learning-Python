# Python compound interest calculator
# This program calculates the future balance using compound interest formula.

principal = 0  # Initial amount of money
rate = 0  # Annual interest rate percentage
time = 0  # Investment duration in years

# Get valid principal amount from the user
while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal can't be less than zero.")
    else:
        break

# Get valid interest rate from the user
while True:
    rate = float(input("Enter the interest rate (%): "))
    if rate < 0:
        print("Interest rate can't be less than zero.")
    else:
        break

# Get valid investment duration from the user
while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than zero.")
    else:
        break

# Calculate compound interest
total = principal * pow((1 + rate / 100), time)

# Display the final balance with two decimal places
print(f"Balance after {time} year(s): £{total:.2f}")