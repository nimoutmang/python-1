fruitsDictionary = {
    "mango": ["yellow", 1],
    "banana": ["yellow", 14],
    "coconut": ["white", 15],
}
fruitName = input("Enter>>")
if fruitName in fruitsDictionary:
    fruitColor = fruitsDictionary[fruitName][0]
    fruitPrice = fruitsDictionary[fruitName][1]
    print(fruitColor, fruitPrice)
else:
    print("not found")







