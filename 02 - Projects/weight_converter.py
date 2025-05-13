# Python weight converter

weight = float(input("Weight: "))
unit = str(input("Kilograms or Pounds? (K or L): "))

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print("Invalid unit! Please enter K or L")

