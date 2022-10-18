marks1=float(input("Enter your marks  : "))
marks2=float(input("Enter your marks  : "))
marks3=float(input("Enter your marks  : "))
marks4=float(input("Enter your marks  : "))
marks5=float(input("Enter your marks  : "))
total=int((marks1+marks2+marks3+marks4+marks5)/5)
if total>=90 and total<=100:
    print("A")
elif total>=80 and total<=89:
    print("B")
elif total>=70 and total<=79:
    print("C")
elif total>=60 and total<=69:
    print("D")
elif total>=50 and total<=59:
    print("E")
elif total>50:
    print("Fail")