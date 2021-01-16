def numberOfSeven(numbers):
    newNumber=0
    for n in range (len(numbers)):
        if numbers[n]==7:
            newNumber=newNumber+1

    return newNumber

numberOfNumber=eval(input("Enter numbers:"))
print(numberOfSeven(numberOfNumber))