from student import Student
from course import Course
import database

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.load_data()  # Load existing data from the database

    def load_data(self):
        """Load students and courses from the database."""
        conn = None
        try:
            conn = database.connect()
            cursor = conn.cursor()
            
            # Load students
            cursor.execute('SELECT email, names, GPA FROM students')
            students = cursor.fetchall()
            self.student_list = [Student(email, names) for email, names, GPA in students]
            for student in self.student_list:
                student.GPA = GPA

            # Load courses
            cursor.execute('SELECT name, trimester, credits FROM courses')
            courses = cursor.fetchall()
            self.course_list = [Course(name, trimester, credits) for name, trimester, credits in courses]

        except Exception as e:
            print(f"Error loading data: {e}")
        finally:
            if conn:
                conn.close()

    def add_student(self, email, names):
        """Add a new student and save to the database."""
        if not any(student.email == email for student in self.student_list):
            student = Student(email, names)
            self.student_list.append(student)
            database.add_student_to_db(email, names)
        else:
            print(f"Student with email {email} already exists.")

    def add_course(self, name, trimester, credits):
        """Add a new course and save to the database."""
        if not any(course.name == name for course in self.course_list):
            course = Course(name, trimester, credits)
            self.course_list.append(course)
            database.add_course_to_db(name, trimester, credits)
        else:
            print(f"Course with name {name} already exists.")

    def register_student_for_course(self, student_email, course_name):
        """Register a student for a course."""
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)

        if student and course:
            student.register_for_course((course.name, course.credits, 0.0))  # 0.0 as placeholder for grade
            database.register_student_for_course(student_email, course_name)
        else:
            print("Student or course not found.")

    def track_attendance(self, student_email, course_name, attendance):
        """Track attendance for a student in a course."""
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)

        if student and course:
            database.track_attendance(student_email, course_name, attendance)
            print(f"Tracking attendance: StudentEmail={student_email}, CourseName={course_name}, Attendance={attendance}")
        else:
            print("Student or course not found.")

    def calculate_GPA(self):
        """Calculate and update GPA for all students."""
        for student in self.student_list:
            student.calculate_GPA()
            database.update_student_GPA(student.email, student.GPA)

    def calculate_ranking(self):
        """Calculate and return the ranking of students based on GPA."""
        self.student_list.sort(key=lambda x: x.GPA, reverse=True)
        return [(student.email, student.GPA) for student in self.student_list]

    def search_by_grade(self, min_gpa, max_gpa):
        """Search and return students within the GPA range."""
        return [s for s in self.student_list if min_gpa <= s.GPA <= max_gpa]

    def generate_transcript(self, student_email):
        """Generate and return the transcript for a student."""
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            return student.courses_registered
        else:
            print(f"Student with email {student_email} not found.")
            return []

