# 3. Divisibility Check of two numbers
# Write a Python program to check whether a number is completely divisible by another number. Accept two integer values form the user
# Program Console Sample Output 1:
# Enter numerator: 4
# Enter Denominator: 2
# Number 4 is Completely divisible by 2
# Program Console Sample Output 2:
# Enter numerator: 7
# Enter Denominator: 4
# Number 7 is not Completely divisible by 4

num1=int(input("Enter the numerator: "))
num2=int(input("Enter the denominator: "))
if num1%num2==0:
    print(f"number {num1} is completely divisible by {num2}.")
else:
     print(f"number {num1} is not completely divisible by {num2}.")