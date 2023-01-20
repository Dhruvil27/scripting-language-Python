file=input("Enter file Name:")
f=open(file,'r')
data=f.read()
word=data.split()
Line=data.split(".")

words=0
sent=0
for i in word:
    words+=len(i)
for k in Line:
    sent=+len(k)
avg=words/len(word)
avgline=sent/len(Line)
print(avg)
print(avgline)