students = []

user_selection = None
while user_selection != 5 :
    print("\nMenu:")
    print("1- Add Student")
    print("2- Show Student")
    print("3- Search Student")
    print("4- Delete Student")
    print("5- Exit")

    try :
        user_selection = int(input("Enter your selection : "))
    except ValueError :
        print("Invalid Input!\n")
        continue
