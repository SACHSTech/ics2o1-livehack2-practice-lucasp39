"""
********************************************************
Filename:       problem1.py
Description:    Determine if a triangle is a right angle triangle
Author:         Pei.L
Created On:     12/02/2021
********************************************************
"""
print("******Right Angle Triangle Calculator******")

#get side lengths
side1 = int(input("Side 1 length: "))
side2 = int(input("Side 2 length: "))
side3 = int(input("Side 3 length: "))

#calculate squares
square1 = side1**2
square2 = side2**2
square3 = side3**2

#determine if it is a right triangle
if (square1+square2 == square3) or (square1+square3 == square2) or (square2+square3 == square1):
  print("A triangle with lengths " + str(side1) + ", " +
    str(side2) + ", and " + str(side3) + " forms a right-angled triangle.")
else:
    print("A triangle with lengths " + str(side1) + ", " +
    str(side2) + ", and " + str(side3) + " does not form a right-angled triangle.")