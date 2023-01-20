import string

def main():
    file=input("Enter File Name:")
    inputfile=open(file,'r')
    files=input("Enter file name")
    outputfile=open(files,'w')
    for i in inputfile:
        word=i.split()
        for k in word:
            count=0
            for j in k:
                if not  j in string.punctuation:
                    count+=1
            if count==4:
                if "."in k:    
                    k="****."
                elif "!" in k:
                    k="****!"
                else:
                    k="****"
            print(k+"_",file=outputfile,end="")
    inputfile.close()
    outputfile.close()

if __name__ =="_main_":
 main()


