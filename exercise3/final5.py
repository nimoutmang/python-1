number=int(input("Enter>>"))
condition=True
number1=1
while number !=72 and condition:
    number1=number1+1
    if number1 == 4:
        condition = False
    if number<72:
        number=int(input("Enter>>"))
if condition:
        print("Win")
       
else:
        print("lost")