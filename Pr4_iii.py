height=float(input("Enter height:"))
weight=float(input("Enter weight:"))

BMI=(weight/height**2)
print(BMI)
if BMI<19:
    print("Your Weight is underweight")
elif BMI>25:
    print("Your Weight is overweight")

else: 

    print("You are Healthy")