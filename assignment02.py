# 2. Check the number either it's positive, negative or zero
# Write a Python program to check if a number is positive, negative or zero
# Program Console Sample Output 1:
# Enter Number: -1
# Negative Number Entered
# Program Console Sample Output 2:
# Enter Number: 2
# Positive Number Entered
# Program Console Sample Output 3:
# Enter Number: 0
# Zero Entered

num = int(input("Enter any number: "))
if num == 0:
    print("Number is zero.")
elif num > 0:
    print("Number is positive.")
else:
    print("Number is negative.")