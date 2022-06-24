# Python program to calculate Area of a triangle with all sides known

side1 = 8
side2 = 6
side3 = 9

#First we should calculate semiperimeter
semiperimeter = (side1 + side2 + side3) / 2
# calculatig area
area = semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3)
area = area ** 0.5
print(area)
