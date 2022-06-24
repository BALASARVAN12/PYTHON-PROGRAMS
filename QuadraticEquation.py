# Python program to solve Roots of a Quadratic Equation

import math
a = 15
b = 42
c = 10

#We Should Calculating value of Discriminant
d = (b ** 2) - (4 * a * c )

# if Discriminant is negative , then roots are imaginary , else they are real
x1 = 0
x2 = 0 
if d <= 0 :
  x1 = (-b + math.sqrt(d)) / (2 * a)
  x2 = (-b - math.sqrt(d)) / (2 * a)
else :
  x1 = (-b + (d ** 0.5)) / (2 * a)
  x2 = (-b - (d ** 0.5)) / (2 * a)
print("x1 is : ",x1)
print("x2 is : ",x2)
