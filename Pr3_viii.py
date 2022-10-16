import math 
pie=3.14
angel=eval(input("Enter angel:"))
height=eval(input("Enter height:"))

angle=(pie/180)*angel
length=(height/math.sin(angle))
print("length is:",length)
