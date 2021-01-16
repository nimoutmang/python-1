print("Welcome to the student database")
print("0: exit")
print("1: add student to database with score 0")
print("2: add points to one student")
print("3: print student average")
print("4: print all students and score")
action = int(input("select an action : "))
students = []

while action != 0:
    if action == 1:
    # TODO : - ask for the name of student,
    # - create a student with this name and with score=0
    # - append the new student to the students array
        Dictionary = {}
        Names = input()
        Dictionary["name"] = Names
        Dictionary["score"] = 0
        students.append(Dictionary)
        print(students)
    elif action == 2:
    # TODO : - ask for the index of student,
    # - ask how many score to add
    # - add score to the student in array
        nameOfstudent = input()
        number = int(input())
        students.append(nameOfstudent)
        students.append(number)
        print(students)
    elif action == 3:
        # TODO : - calculate and print average score
        scoreOfname = eval(input())
        sumOfscore = 0
        for n in range(len(scoreOfname)):
            sumOfscore += scoreOfname[n]["score"]
        averageOfscore = sumOfscore/len(scoreOfname)
        print(averageOfscore)
    elif action == 4:
        print(students)

    action = int(input("select an action : "))