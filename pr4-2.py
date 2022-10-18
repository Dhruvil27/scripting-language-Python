hin=float(input("Enter your height :"))
weight=float(input("Enter your Weight :"))
height=hin*0.0254
print(height)
BMI=weight*(height**2)
if BMI<19:
    print("You are under weight")
elif BMI>25:
    print("Yopu ar overwight")
else:
    print("You are healthy")