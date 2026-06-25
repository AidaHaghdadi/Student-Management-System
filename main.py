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

    if user_selection == 1 :
        student_name = input("Enter Name :")
        student_age = int(input("Enter Age :"))
        student_grade = float(input("Enter Grade :"))
        student = {
            "Name" : student_name,
            "Age" : student_age,
            "Grade" : student_grade
        }
        students.append(student)
        print("Student's Information Added!")
