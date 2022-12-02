s1={10,20,30}
s2={20,30}
print(s1)
print(s2)



print("--------Added Item in a SET------")

s1.add(40)
print(s1)



print("--------Removed Item From a SET------")

s1.discard(20)
print(s1)


print("---Union Operation---")
s3=s1.union(s2)
print(s3)


print("---Intersaction  Operation---")
s1.intersection(s2)
print(s1)

print("----Difference  Operation---")

s1-s2
s2-s1
print(s1)
print(s2)

print("----symmeric Difference  Operation---")

s1^s2
s2^s1
print(s1)
print(s2)


