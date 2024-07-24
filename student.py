class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        if not self.courses_registered:
            return 0.0
        total_points = sum(course.credits * course.grade for course in self.courses_registered)
        total_credits = sum(course.credits for course in self.courses_registered)
        self.GPA = total_points / total_credits if total_credits else 0.0
        return self.GPA

class Course:
    def __init__(self, name, trimester, credits, grade=0.0):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade = grade
