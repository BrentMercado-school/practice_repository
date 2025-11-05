enrollment = {
    "IT101": {'Alice', 'Bob', 'Charlie'},
    "CS102": {'Bob', 'Diana'},
    "IS201": {'Charlie', 'Eve'}
}

print("Current Enrollments:")
for course, students in enrollment.items():
    print(f"{course}: {students}")

print("\nAdding student 'Frank' to CS102...")
enrollment["CS102"].add("Frank")

print("Removing student 'Alice' from IT101...")
enrollment["IT101"].discard("Alice")

print("\nUpdated Enrollments:")
for course, students in enrollment.items():
    print(f"{course}: {students}")

students_pair_count = {}
for students in enrollment.values():
    for student in students:
        students_pair_count[student] = students_pair_count.get(student, 0) + 1

students_with_multiple_pair = {student for student, count in students_pair_count.items()
                               if count > 1 }
print(f"\nStudents with multiple pairs: {students_with_multiple_pair}")

unique_student = {student for student in students_pair_count}
print(f"All Unique students: {unique_student}")

























