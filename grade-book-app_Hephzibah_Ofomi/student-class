class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        total_credits = sum(course[1] for course in self.courses_registered)
        total_points = sum(course[1] * course[2] for course in self.courses_registered)
        self.GPA = total_points / total_credits if total_credits > 0 else 0.0

    def register_for_course(self, course):
        self.courses_registered.append(course)

