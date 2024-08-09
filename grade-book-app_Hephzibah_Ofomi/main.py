from gradebook import GradeBook

def main():
    gradebook = GradeBook()

    while True:
        print("""
        Menu:
        1. Add student
        2. Add course
        3. Register student for course
        4. Track attendance
        5. Calculate GPA
        6. Calculate ranking
        7. Search by grade
        8. Generate transcript
        9. Exit
        """)
<<<<<<< HEAD
        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter credits: "))
            gradebook.add_course(name, trimester, credits)
        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            gradebook.register_student_for_course(student_email, course_name)
        elif choice == '4':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            try:
                attendance = int(input("Enter attendance count: "))
            except ValueError:
                print("Invalid attendance count. Please enter an integer.")
                continue
=======
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            email = input("Enter student email: ").strip()
            names = input("Enter student names: ").strip()
            gradebook.add_student(email, names)
        elif choice == '2':
            name = input("Enter course name: ").strip()
            trimester = input("Enter trimester: ").strip()
            credits = int(input("Enter credits: ").strip())
            gradebook.add_course(name, trimester, credits)
        elif choice == '3':
            student_email = input("Enter student email: ").strip()
            course_name = input("Enter course name: ").strip()
            grade_points = float(input("Enter grade points: ").strip())
            gradebook.register_student_for_course(student_email, course_name, grade_points)
        elif choice == '4':
            student_email = input("Enter student email: ").strip()
            course_name = input("Enter course name: ").strip()
            attendance = int(input("Enter attendance count: ").strip())
>>>>>>> e74efa9413d02b20416d7acd848127f367cd4be4
            gradebook.track_attendance(student_email, course_name, attendance)
        elif choice == '5':
            gradebook.calculate_GPA()
        elif choice == '6':
            ranking = gradebook.calculate_ranking()
            for rank in ranking:
                print(f"Email: {rank[0]}, GPA: {rank[1]}")
        elif choice == '7':
<<<<<<< HEAD
            min_grade = float(input("Enter minimum GPA: "))
            max_grade = float(input("Enter maximum GPA: "))
            results = gradebook.search_by_grade(min_grade, max_grade)
            for student in results:
                print(f"Email: {student.email}, GPA: {student.GPA}")
        elif choice == '8':
            for student in gradebook.student_list:
                print(f"Email: {student.email}, GPA: {student.GPA}")
=======
            min_gpa = float(input("Enter minimum GPA: ").strip())
            max_gpa = float(input("Enter maximum GPA: ").strip())
            results = gradebook.search_by_grade(min_gpa, max_gpa)
            for student in results:
                print(f"Email: {student.email}, GPA: {student.GPA}")
        elif choice == '8':
            student_email = input("Enter student email: ").strip()
            transcript = gradebook.generate_transcript(student_email)
            for course in transcript:
                print(f"Course: {course[0]}, Credits: {course[1]}, Grade Points: {course[2]}")
>>>>>>> e74efa9413d02b20416d7acd848127f367cd4be4
        elif choice == '9':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

