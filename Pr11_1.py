#Operation 1

# f=open("file.txt","w")
# f.write("Hello World")
# if f:
#     print("File is created")
# print(f.read())
# f.close()

# #Operation 2
# f=open("file.txt","r")
# print(f.read())
# f.close()

# #Operation 3

f=open("file.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

# f.close()


# #operation 5

# f=open("file.txt","w")
# a=("Hello Navsari")
# f.writelines(a)
# f.close()

# #Operation 6

# line=0
# word=0
# f=open("file.txt","r")

# for i in f:
#     line+=1
#     word+=len(i.split())
# print("lines are:",line,"\n","Words are:",word)
# f.close()