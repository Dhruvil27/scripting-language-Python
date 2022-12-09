

#Task-1
stu={"Id":21033,"Name":"Dhruvil","Branch":"Computer","city":"Navsari","SPI":8,"Age":17}
#Task-2
print(stu)


#Task-3
print("--------Added Key Vlaue pair--------")
stu["Semester"]=3
print(stu)
#Task-3_2
print("--------Remove  Key Vlaue pair--------")
del stu["city"]
print(stu)

#Task-4
value=str(input("Enter The key you will be Find:"))
bul=value in stu
print(bul)

#Task-5

print("--------Iterate through a Dictionar--------")

for i in stu :
    print(stu[i])

#Task-6
print("--------Concanenate multiple dictionaries---------")
stu1={"Hello":1,"Day":3}
stu.update(stu1)
print(stu)
        




