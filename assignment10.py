# 10. Euclidean distance
# write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# Program Console Sample 1:
# Enter Co-ordinate for x1: 2
# Enter Co-ordinate for x2: 4
# Enter Co-ordinate for y1: 4
# Enter Co-ordinate for y2: 4
# Distance between points (2, 4) and (4, 4) is 2
# ###### Reference:
# https://en.wikipedia.org/wiki/Euclidean_distance

x1=int(input("Enter Co-ordinate for x1: "))
x2=int(input("Enter Co-ordinate for x2: "))
y1=int(input("Enter Co-ordinate for y1: "))
y2=int(input("Enter Co-ordinate for y2: "))
import math
print(f"(x1,y1))=({x1},{y1})")
print(f"(x2,y2))=({x2},{y2})")
distance_formula = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
distance_formula = round(distance_formula,2)
print(f"The Distance Between Points ({x1},{y1}) and ({x2},{y2}) are: {distance_formula}")

