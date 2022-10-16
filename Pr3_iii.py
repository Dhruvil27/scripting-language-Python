p=int(input("Enter the principal amount:"))
r=int(input("Enter the rate for compound interest:"))
t=int(input("Enter the  number of time periods elapsed:"))
n=int(input("Enter the number of times interest applied per time period:"))

simple_interest=float(p*r*t)/100
compound_interest=float(p*(1+r)/(100*n)**n*t)

print("Simple intrest is:",simple_interest)
print("Compound intrest is :",compound_interest) 

