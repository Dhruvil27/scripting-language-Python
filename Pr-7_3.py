info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)



print("----------Added key vale Pair in a Dictionary----------------")

info['DOB'] = 2001
print(info)

print("----------Removed key vale Pair in a Dictionary----------------")

info.pop('eligible')
print(info)


if "DOB" in info:
    print("Exists")
else:
    print("Does not exist")


    

print("--------Iterate through a Dictionar--------")


keys = info.keys()
print(keys)


print("--------Concanenate multiple dictionaries---------")

info = {'name':'Dhruvil', 'age':17, 'eligible':"No"}
info2 = {'DOB': "27-1-2006",'city': "Navsari","Blood Group" : "O+"}
info.update(info2)
print('Updated dictionary:')
print(info)