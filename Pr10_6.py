a1="abcdefghijklmnopqrstuwxyz" 
b=0
name=input("Enter string:")

for i in name:
    b+=a1.find((i.lower()))+1
print(b)


