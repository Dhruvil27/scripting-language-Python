rgb=[]


for i in range(0,2,4):
    dec=int(hex[i:i1+2],16)
    rgb.append(dec)
return tuple(rgb)

print(colorcode("FF6347"))