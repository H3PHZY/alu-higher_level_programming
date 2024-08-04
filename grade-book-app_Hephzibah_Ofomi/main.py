from gradebook import GradeBook

def main():
    gradebook = GradeBook()
    print("Welcome to the GradeBook App")
    
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
        choice = input("Enter your choice: ").strip()

        print(f"User entered choice: {choice}")  # Debug statement

        try:
            if choice == '1':
                email = input("Enter student email: ").strip()
                names = input("Enter student names: ").strip()
                print(f"Adding student: Email={email}, Names={names}")  # Debug statement
                gradebook.add_student(email, names)
            elif choice == '2':
                name = input("Enter course name: ").strip()
                trimester = input("Enter trimester: ").strip()
                credits = int(input("Enter credits: ").strip())
                print(f"Adding course: Name={name}, Trimester={trimester}, Credits={credits}")  # Debug statement
                gradebook.add_course(name, trimester, credits)
            elif choice == '3':
                student_email = input("Enter student email: ").strip()
                course_name = input("Enter course name: ").strip()
                print(f"Registering student for course: StudentEmail={student_email}, CourseName={course_name}")  # Debug statement
                gradebook.register_student_for_course(student_email, course_name)
            elif choice == '4':
                student_email = input("Enter student email: ").strip()
                course_name = input("Enter course name: ").strip()
                attendance = int(input("Enter attendance count: ").strip())
                print(f"Tracking attendance: StudentEmail={student_email}, CourseName={course_name}, Attendance={attendance}")  # Debug statement
                gradebook.track_attendance(student_email, course_name, attendance)
            elif choice == '5':
                print("Calculating GPA...")
                gradebook.calculate_GPA()
            elif choice == '6':
                print("Calculating ranking...")
                ranking = gradebook.calculate_ranking()
                for rank in ranking:
                    print(f"Email: {rank[0]}, GPA: {rank[1]}")
            elif choice == '7':
                min_gpa = float(input("Enter minimum GPA: ").strip())
                max_gpa = float(input("Enter maximum GPA: ").strip())
                print(f"Searching by grade: MinGPA={min_gpa}, MaxGPA={max_gpa}")  # Debug statement
                results = gradebook.search_by_grade(min_gpa, max_gpa)
                for student in results:
                    print(f"Email: {student.email}, GPA: {student.GPA}")
            elif choice == '8':
                student_email = input("Enter student email: ").strip()
                print(f"Generating transcript for: {student_email}")  # Debug statement
                transcript = gradebook.generate_transcript(student_email)
                for course in transcript:
                    print(f"Course: {course[0]}, Credits: {course[1]}, Grade: {course[2]}")
            elif choice == '9':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

