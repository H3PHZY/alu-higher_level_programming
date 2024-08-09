from student.py import Student
from course.py import Course
import database

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
        database.add_student_to_db(email, names)

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        database.add_course_to_db(name, trimester, credits)

    def register_student_for_course(self, student_email, course_name):
        student = next(s for s in self.student_list if s.email == student_email)
        course = next(c for c in self.course_list if c.name == course_name)
        student.register_for_course((course.name, course.credits, 0.0)) # Assuming 0.0 as placeholder for grade
        database.register_student_for_course(student_email, course_name)

    def track_attendance(self, student_email, course_name, attendance):
        database.track_attendance(student_email, course_name, attendance)

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()
            database.update_student_GPA(student.email, student.GPA)

    def calculate_ranking(self):
    # Example implementation
    # This method should return a list of tuples (email, GPA)
    return [(student.email, student.GPA) for student in self.student_list]

    # In your main function
    ranking = gradebook.calculate_ranking()
    print(ranking)  # Debugging line to ensure ranking is correct
    for rank in ranking:
    	print(f"Email: {rank[0]}, GPA: {rank[1]}")
 
    def search_by_grade(self, min_gpa, max_gpa):
        return [s for s in self.student_list if min_gpa <= s.GPA <= max_gpa]

    def generate_transcript(self, student_email):
        student = next(s for s in self.student_list if s.email == student_email)
        return student.courses_registered

