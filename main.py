#print("Welcome to csc class")
'''name = input("Enter your name: ")
age = input("Enter your age: ")
depertment = input('Enter your depertment: ')
matric = input("Enter your matric number: ")
sex = input("Enter your sex: ")
school = input("Enter your school: ")
print("Welcome", name, "Your age is", age, "Your depertment is" ,depertment, "Your matric number is" ,matric, "Your sex is" ,sex, "Your school is" ,school,  )'''

'''first = input("Enter the first number: ")
second = input("Enter second number: ")
last = input("Enter your last number: ")
sum = int(first) + int(second) + int(last)
print("The sum of the three numbers are" ,sum,)

first = input("Enter the first number: ")
second = input("Enter second number: ")
last = input("Enter your last number: ")
sub = int(first) - int(second) - int(last)
print("The subtraction of the three numbers are" ,sub,)

first = input("Enter the first number: ")
second = input("Enter second number: ")
last = input("Enter your last number: ")
mut = int(first) * int(second) * int(last)
print("The mutiplication of the three numbers are" ,mut,)

first = input("Enter the first number: ")
second = input("Enter second number: ")
last = input("Enter your last number: ")
div = int(first) * int(second) * int(last)
print("The division of the three numbers are" ,div,)'''

'''import modules
modules.greeting(" David")'''
'''import modules
name = input(" What is your name: ").upper()
modules.displaymsg(name)'''
# main.py

from modules import solve_quadratic

# Input coefficients from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Call the solve_quadratic function from the module
roots = solve_quadratic(a, b, c)

# Display the roots
print(f"The roots of the quadratic equation are: {roots}")
