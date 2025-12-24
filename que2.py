sectiona = {}

while True:
    print("Enter your choice (1-4) :")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Print all Students")
    print("4. Exit")
    opt = int(input("Choice - "))

    if opt == 1:
        name = input("Name to add :-")
        score = input("Score :-")
        if(name in sectiona):
            print("Name already exists, please try new name")
        else:
            sectiona[name] = score
            print("Student Added Succesfully")
    elif opt == 2:
        name = input("Enter the name :-")
        if(name in sectiona):
            new_score = int(input("Enter new Score :-"))
            sectiona[name] = new_score
            print("Score updated")
        else:
            print("No name found")
    elif opt == 3:
        for name, score in sectiona.items():
            print(name, ":" ,score)
    elif opt == 4:
        print("Exitting")
        break
    else:
        print("Invalid input, try again")

