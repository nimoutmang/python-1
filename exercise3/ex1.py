fruits=[
    ["mango", "yellow", 1],
    ["banana", "yellow",14],
    ["coconut","white",15],
]
fruitName=input("Enter>>")
result=True
for fruit in fruits:
    if fruit[0]==fruitName and result:
        print(fruit[1], fruit[2])
        result=False
if result:
    print("NotFound")


    
    
    
    