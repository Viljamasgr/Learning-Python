# if = Do some code only IF some conditions is True
#      Else do something else

age = int(input("How old are you? "))

if age >= 18:
    print(f"You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 100:
    print("You are too old to sign up!")
else:
    print("You must be 18+ to sign up!")