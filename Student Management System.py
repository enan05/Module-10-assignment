class Person:
    name = ""
    age = 0
    address = ""

    def display_person_info(self):
        print(f'name: {self.name}'
              f'age: {self.age}'
              f'address: {self.address}')


class Student(Person):
    student_id = ""
    grades = {"": ""}
    courses = []

    def add_grade(self, subject, grade):
        self.grades = {subject: grade}

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        print(f'name: {self.name}'
              f'ID: {self.student_id}'
              f'age: {self.age}'
              f'address: {self.address}'
              f'enrolled courses: {self.courses}'
              f'grades: {self.grades}')


class Course:
    course_name = ""
    course_code = ""
    instructor = ""
    students = []

    def add_student(self, student):
        self.students.append(student)

    def display_course_info(self):
        print(f'Course Name: {self.course_name}'
              f'Code: {self.course_code}'
              f'Instructor: {self.instructor}'
              f'Enrolled Students: {self.instructor}')
