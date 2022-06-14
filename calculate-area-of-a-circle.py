#calculate the area of a circle

import math 

radius = input("Enter the radius of the circle: ") 
radius = float(radius) 
area = math.pi * radius * radius 

print("Area of the circle: {:.2f}".format(area))
