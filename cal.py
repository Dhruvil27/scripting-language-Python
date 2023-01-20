def add(a,b):
    return (a+b)

def subtraction(a,b):
    return (a-b)

def multiplication(a,b):
    return (a*b)
def Division(a,b):
    return (a/b)

def modulo(a,b):
    return (a%b)

def squre(a):
    return (a**2)

def factorial(a):
    
    if a==0:
     return 1
    else:
        return a*factorial(a-1)