# 9. Calculate Interest
# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
# Program Console Sample 1:
# Please enter principal amount: 10000
# Please Enter Rate of interest in %: 0.1
# Enter number of years for investment: 5
# After 5 years your principal amount 10000 over an interest rate of 0.1 % will be 16105.1


Amount = int(input("Enter any number: "))
Interest_percentage = float(input("Enter rate of interest in percentage: "))
years = int(input("Enter number of year/years for investment: "))
future_value = Amount*((1+(0.01*Interest_percentage*100))**years)
print(round(future_value,2))
