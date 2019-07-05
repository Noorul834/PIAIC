# 13. Sum of n Positive Integers
# Write a python program to sum of the first n positive integers
# Program Console Sample 1:
# Enter value of n: 5
# Sum of n Positive integers till 5 is 15

num=0
value=int(input("Enter the value of n: "))
for i in range(value+1):
    num+=i
    print(f"sum of n positive integers till {value} is {num}")