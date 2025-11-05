class Student(object):
    def __init__(self, last_name, first_name, course, s_id):
        self.last_name = last_name
        self.first_name = first_name
        self.course = course
        self.s_id = s_id

ListOfStudents = []
while True:
    print("--- STUDENT CRUD PROJECT ---")
    print("1 - Add Student\n2 - View Students\n3 - Delete Students\n4 - Edit Students")
    print("----------------------------")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1 or choice == 2 or choice == 3 or choice == 4:
                break
            print("Invalid Choice\n")
            continue
        except ValueError:
            print("Invalid Choice\n")
            continue

    if choice == 1:
        print("\n--- You are now creating a Student ---")
        lname = input("Enter student last name: ")
        fname = input("Enter student first name: ")
        c = input("Enter student course: ")
        student_id = input("Enter student id: ")
        newStudent = Student(lname, fname, c, student_id)
        ListOfStudents.append(newStudent)

        print("\nYou have successfully created a Student!")
        input("Press enter to continue...")
        print("\n")

    elif choice == 2:
        if len(ListOfStudents) == 0:
            print("\nYou have not created any Students")
            input("Press enter to continue...")
            print("\n")
        else:
            print("\n--- You are viewing the list of Students ---")
            i = 1
            for student in ListOfStudents:
                print(f"{i}. {student.last_name}, {student.first_name} - {student.course} - {student.s_id}")
                i = i + 1

            input("\nPress enter to continue...")
            print("\n")

    elif choice == 3:
        if len(ListOfStudents) == 0:
            print("\nYou have not created any Students")
            input("Press enter to continue...")
            print("\n")
        else:
            print("\n--- You are deleting a Student ---")
            id_to_delete = input("Enter student id: ")
            for i in range(len(ListOfStudents)):
                if ListOfStudents[i].s_id == id_to_delete:
                    print("Student Found!")
                    print(f"{ListOfStudents[i].last_name}, {ListOfStudents[i].first_name} - {ListOfStudents[i].course} - {ListOfStudents[i].s_id}")

                    sure = input("\nAre you sure you want to delete this Student? (y/n): ").lower()
                    if sure == "y":
                        del ListOfStudents[i]
                        print("\nStudent Deleted!")
                        input("Press enter to continue...")
                        print("\n")
                    else:
                        print("\nStudent Not Deleted!")
                        input("Press enter to continue...")
                        print("\n")
                    break
            print(f"\nThe id {id_to_delete} does not exist.")
            input("Press enter to continue...")
            print("\n")


