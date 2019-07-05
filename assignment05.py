# 5. Copy string 'n' times
# Write a Python program to get a string which is 'n' (non-negative integer) copies of a given string.
# Program Console Output:
# Enter String: Hi
# How many copies of String you need: 4
# 4 Copies of Hi are HiHiHiHi

string=input("Enter a string: ")
n=int(input("How many of copies of string you want?: "))
if n>0:
    print(f"{n} copies of string {string} are: {string*n}")
else:
        print("Invalid")