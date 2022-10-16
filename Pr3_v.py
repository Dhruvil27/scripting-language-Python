
a=int(input("Enter  the value of a:"))
b=int(input("Enter  the value of b:"))
c=int(input("Enter  the value of c:"))

 
max= (a if  (a>b and a>c) else b if (b>a and b>c)else c)
 
print("Greater number will be Printed:",max)