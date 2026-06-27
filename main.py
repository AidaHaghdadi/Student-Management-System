students = []

user_selection = None
while user_selection != 5 :
    print("\nMenu:")
    print("1- Add Student")
    print("2- Show Student")
    print("3- Search Student")
    print("4- Delete Student")
    print("5- Exit")

    # Input validation
    try :
        user_selection = int(input("Enter your selection : "))
    except ValueError :
        print("Invalid Input!\n")
        continue
    
    # Add student
    if user_selection == 1 :
        student_name = input("Enter Name :")
        student_age = int(input("Enter Age :"))
        student_grade = float(input("Enter Grade :"))
        student = {
            "name" : student_name,
            "age" : student_age,
            "grade" : student_grade
        }
        students.append(student)
        print("Student's Information Added!")

    # Show student
    elif user_selection == 2 :
        if len(students) == 0 :
            print("No student found!")
        else :
            print("\nstudents list :")
            for index, student in enumerate(students) :
                print(f"{index + 1}. {student['name']} | age: {student['age']} | grade: {student['grade']}")
                
    # Search student
    elif user_selection == 3 :
        search_student = input("Enter student name :")
        count = 0
        for student in students:
            if search_student == student["name"] :
                print(f"{count + 1}. {student['name']} | age: {student['age']} | grade: {student['grade']}")
                count += 1
        if count == 0 :
            print("Student not found!")
        else :
            print(f"<{count} student(s) found>")