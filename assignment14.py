# 14. Digits Sum of a Number
# Write a Python program to calculate the sum of the digits in an integer
# Program Console Sample 1:
# Enter a number: 15
# Sum of 1 + 5 is 6
# Program Console Sample 2:
# Enter a number: 1234
# Sum of 1 + 2 + 3 + 4 is 10

num=input("Enter any num: ")
sum=0
for s in num:
    sum+=int(s)
print(f"The sum of num is:",sum)