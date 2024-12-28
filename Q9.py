'''Q9. Write a Python program that takes a side of a square, and the radius as input
and checks whether the square can be inscribed into the circle or not.'''
import math

Side = float(input("Enter Side of Square : "))
Radius = float(input("Enter Radius of Circle : "))

diameter = 2*Radius
diagonal_lengh = Side * pow(2,0.5)

#condition : diameter of circle = diagonal length of square
if (diameter==diagonal_lengh): print("Square of side lenth ",Side, "can be inscribed into the circle of radius ",Radius)
else: print("Square of side lenth ",Side,"CANNOT be inscribed into the circle of radius ",Radius)