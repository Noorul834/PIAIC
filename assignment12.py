# 12. BMI Calculator
# Write a Python program to calculate body mass index
# Program Console Sample 1:
# Enter Height in Cm: 180
# Enter Weight in Kg: 75
# Your BMI is 23.15

import math
height=int(input("Enter height in cm: "))
weight=int(input("Enter weight in kg: "))
BMI=(weight/(math.pow(height*0.012,2)))
BMI= round(BMI,2)
print(f"Your BMI is:{BMI}")
