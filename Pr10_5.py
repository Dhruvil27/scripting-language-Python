def colorcode(hex):
    rgb=[]
    
    for i in (0,2,4):
        dec=int(hex[i:i+2],16)
        rgb.append(dec)
    return tuple(rgb)

print(colorcode("FF6347"))