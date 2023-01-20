f=open("file.txt")

num=0
f.readline()
for i in f:
    for a in i:
        if a.isdigit()==True:
            num+=1
            print("Number is:",a)
print("Total Number is:",num)