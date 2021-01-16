Newname=[
    {"name":"dara", "age":23},
    {"name": "gygy", "age":45},
    {"name": "somphors","age":19}
]
Array=[]
for Name in Newname:
    if Name["age"]>23:
        Array.append(Name["name"])
print(Array)




array=[
    {"name": "mango", "price": 90},
    {"name": "banana", "price": 12},
    {"name": "apple", "price": 13}


]

newArray=[]
oldArray=[]
for name in array:
    if name["price"]<20:
        newArray.append(name["name"])
        print(newArray)

    else:
        print(oldArray)




