'''def greeting(name):
    print('Hello'+ name)'''
'''def displaymsg(name):
    print("Hi"+ name)'''

#ASSIGNMENT 
#WRITE A PYTHON PROGRAM USING A MODULE TO SOLVE FOR THE ROOT OF A QUADRATIC EQUATION AX^2 + BX + C =0 WHERE X=-B+ OR - SQRT B^2 -4AC/2A
# quadratic_solver.py

import cmath

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the two roots
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)

    return root1, root2
