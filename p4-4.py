hr=int(input("enter the hours :"))
r=int(input("enter thr rate ;"))

if 40 > hr  :
    a=hr*r
    print("total hr amount is:",a)
elif 40 < hr :
    a=hr*r
    b=hr-40
    c=(b)*(r/2)
    t=a+c
    print("total hr salary is:",t)