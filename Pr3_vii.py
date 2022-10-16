import cmath  
a = float(input("Enter value of a:"))  
b = float(input("Enter value of b:"))  
c = float(input("Enter value of  c:"))  
  

Dis=b**2-4*a*c

Ans1 = (-b + cmath.sqrt(Dis))/(2 * a)
Ans2 = (-b-cmath.sqrt(Dis))/(2 * a)  


print("The Discriminant is:",Dis) 


print("The Real Roots are:",Ans1)
print("The Real Roots are:",Ans2)


