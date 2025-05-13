# Logical operators evaluate multiple conditions: or, and, not
# - 'or' requires at least one condition to be True
# - 'and' requires both conditions to be True
# - 'not' inverts the condition (True becomes False, False becomes True)

temp = 20
is_sunny = True  # Boolean flag indicating if it's sunny

if temp >= 28 and is_sunny:
    print("It is HOT outside.")
    print("It is SUNNY.")
elif temp <= 0 and is_sunny:
    print("It is COLD outside.")
    print("It is SUNNY.")
elif 0 < temp < 28 and is_sunny:  # Temperature falls within a warm range
    print("It is WARM outside.")
    print("It is SUNNY.")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside.")
    print("It is CLOUDY.")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside.")
    print("It is CLOUDY.")
elif 0 < temp < 28 and not is_sunny:
    print("It is WARM outside.")
    print("It is CLOUDY.")