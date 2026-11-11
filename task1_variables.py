"""Task 1: Variables and variable names  (lesson 1.1 and 1.2)

Edit this file, then run:  python task1_variables.py
Replace every TODO. Do not rename the variables or functions.
"""

# 1. Create four variables about yourself.
#    student_name -> a string (not empty)
#    age          -> an int
#    gpa          -> a float
#    is_enrolled  -> a bool
student_name = "Aaron Marby Manreal"
age = 20
gpa = 3.0
is_enrolled = True

# 2. Swap the values of a and b WITHOUT creating a third variable.
#    After your code runs, a must be 7 and b must be 3.
a = 3
b = 7
# TODO: swap them here (hint: multiple assignment)
a, b = b, a

# 3. Which of these are valid Python variable names?
#    Put ONLY the valid ones in the list, in the same order they appear.
candidates = ["my_var", "2nd_place", "_hidden", "first-name", "Total", "for", "user name", "x1"]
valid_names = ["my_var", "_hidden", "Total", "x1"]  # TODO

# 4. One line that assigns the value 0 to x, y and z at the same time.
# TODO: write it here, e.g. x = ...
x = y = z = 0

if __name__ == "__main__":
    print(student_name, age, gpa, is_enrolled)
    print(a, b)
    print(valid_names)
