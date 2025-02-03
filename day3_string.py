name="salina"
size=len(name) #len() gives the size of string
print("size of string : ",size)
nameshort=name[0:4]
nameshort2=name[-3:-1]#negative slicing ,negative starts with -1
nameshort3=name[3:5]#corresponding of negative slicing
print(nameshort2,nameshort3)
skip=name[0:5:2]#2 idicate steps
print(skip)