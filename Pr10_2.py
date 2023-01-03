
s=input("Enter A string:")
vowel="a,e,i,o,u"
a=0
b=0

for i in s:
    if i in vowel:
        a+=1
    else:
        b+=1
print("Vowel Are:",a,"\nConstant are:",b)
    