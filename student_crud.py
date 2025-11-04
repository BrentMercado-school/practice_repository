class Student(object):
    def __init__(self, last_name, first_name, course, s_id):
        self.last_name = last_name
        self.first_name = first_name
        self.course = course

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
        print("\n\n--- You are now creating a Student ---")
        lname = input("Enter student last name: ")
        fname = input("Enter student first name: ")
        c = input("Enter student course: ")
        student_id = input("Enter student id: ")
        newStudent = Student(lname, fname, c, student_id)
        ListOfStudents.append(newStudent)

        print("\nYou have successfully created a Student!")
        input("Press enter to continue...")
        print("\n")