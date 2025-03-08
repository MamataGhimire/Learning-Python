d={}#Empty dictionary
marks={

    "sallu":100,
    "monika":80,
    "suraj":24,
    0:"kriti"

}
print(marks,type(marks))
print(marks["sallu"])
print(marks.get("sallu"))
   #print(marks["sallu2"]) returns an error ,print(marks.get("sallu2")) prints None

# methods of dictionary
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"sallu":99})
print(marks)

marks.update({"venshu":100})
print(marks)
print(len(marks))


