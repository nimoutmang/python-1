fruits = [
    ["mango", "green", 10],
    ["banana", "yellow", 14],
    ["Coconut", "white", 15],
    ["apple","red",50],
    ["orange","orange",30]
]

fruitName=input("Enter>>")
result=True
for fruit in range (len(fruits)):
    if fruits[fruit][0] == fruitName:
        print(fruits[fruit][1], fruits[fruit][2] )
        result=False
if result:
    print("NOT FOUND")
  


