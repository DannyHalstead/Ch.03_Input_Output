'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''

print("You are going to find out the area of your trapezoid, whether you want to or not.")
BaseOne=float(input("What is the length of your first base?"))
print("Great.")
BaseTwo=float(input("What is the length of your second base?"))
print("Even better.")
Height=float(input("What is the height of your trapezoid?"))
print("Wow!")
Area=(BaseOne+BaseTwo)/2*Height
print("It is my life goal to tell you that the area of your trapezoid is", Area)