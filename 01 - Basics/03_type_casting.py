# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "John Smith"
age = 23
gpa = 3.14
is_student = True

# Convert variables to different types
name_as_int = int(age)  # Convert age to an integer (technically, it's already an int)
age_as_str = str(age)  # Convert age to a string
gpa_as_int = int(gpa)  # Convert GPA to an integer (truncates the decimal part)
is_student_as_int = int(is_student)  # Convert boolean to an integer (True = 1, False = 0)
gpa_as_str = str(gpa)  # Convert GPA to a string
age_as_float = float(age)  # Convert age to a float
name_as_bool = bool(name)  # Convert string to boolean (non-empty string = True)

# Print the results
print("name as bool:", name_as_bool, type(name_as_bool))
print("age as str:", age_as_str, type(age_as_str))
print("gpa as int:", gpa_as_int, type(gpa_as_int))
print("is_student as int:", is_student_as_int, type(is_student_as_int))
print("gpa as str:", gpa_as_str, type(gpa_as_str))
print("age as float:", age_as_float, type(age_as_float))