array=[
    {"name": "mango", "price": 10},
    {"name": "banana", "price": 12},
    {"name": "apple", "price": 13}
]

newArray=[]
for name in array:
    if name["price"] <20:
        newArray.append(name["name"])
print(newArray)
        
