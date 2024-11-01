import json


class Person:
    def __init__(self, name="", age=0, address=""):
        self.name = name
        self.age = age
        self.address = address
        
    def display_person_info(self):
        print(f'''
                Person Information:
                Name: {self.name}
                Age: {self.age}
                Address: {self.address}
                ''')


class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []
        
    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        print(f'''
        Student Information: 
        Name: {self.name}
        ID: {self.student_id}
        Age: {self.age}
        Address: {self.address}
        Enrolled courses: {self.courses}
        Grades: {self.grades}''')


class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_course_info(self):
        enrolled_students = ""
        for student in self.students:
            enrolled_students += student.name + ", "

        print(f'''
              Course Information:  
              Course Name: {self.course_name}
              Code: {self.course_code}
              Instructor: {self.instructor}
              Enrolled Students: {enrolled_students}''')


def students_dictionary(student):
    return {
        "name": student.name,
        "age": student.age,
        "address": student.address,
        "student_id": student.student_id,
        "grades": student.grades,
        "courses": student.courses
    }


def courses_dictionary(course):
    return {
        "course_name": course.course_name,
        "course_code": course.course_code,
        "instructor": course.instructor,
        "students": [student.name for student in course.students]
    }


all_students = {}
all_courses = {}

print(f'''
      ==== Student Management System ====
      1. Add New Student
      2. Add New Course
      3. Enroll Student in Course
      4. Add Grade for Student
      5. Display Student Details 
      6. Display Course Details 
      0. Exit 
''')

while True:
    option = int(input("Enter your option number: "))

    if option == 0:
        print(f'Exiting Student Management System. Goodbye!')
        break

    elif option == 1:
        name = input("Enter Student Name: ")
        age = int(input("Enter age: "))
        address = input("Enter address: ")
        student_id = input("Enter student id: ")

        all_students[student_id] = Student(name, age, address, student_id)
        print(f'Student {name} (ID: {student_id}) added successfully')

    elif option == 2:
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor = input("Enter Instructor Name: ")

        all_courses[course_code] = Course(course_name, course_code, instructor)
        print(f'Course {course_name} (Code: {course_code}) created with instructor {instructor}')

    elif option == 3:
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")

        if student_id in all_students and course_code in all_courses:
            all_students[student_id].enroll_course(course_code)
            all_courses[course_code].add_student(all_students[student_id])
            print(f'Student {all_students[student_id].name} (ID: {student_id}) enrolled in {all_courses[course_code].course_name} (Code: {course_code})')
        else:
            print("Invalid Student ID or Course Code.")

    elif option == 4:
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")

        if student_id in all_students and course_code in all_courses:
            grade_input = input("Enter Grade: ")
            all_students[student_id].add_grade(all_courses[course_code].course_name, grade_input)
            print(f'Grade {grade_input} added for {all_students[student_id].name} in {all_courses[course_code].course_name}')
        else:
            print("Invalid Student ID or Course Code.")

    elif option == 5:
        student_id = input("Enter Student ID: ")

        if student_id in all_students:
            all_students[student_id].display_student_info()
        else:
            print("Invalid Student ID")

    elif option == 6:
        course_code = input("Enter Course Code: ")

        if course_code in all_courses:
            all_courses[course_code].display_course_info()
        else:
            print("Invalid Course Code.")

    elif option == 7:
        students_data = {student_id: students_dictionary(student) for student_id, student in all_students.items()}
        courses_data = {course_code: courses_dictionary(course) for course_code, course in all_courses.items()}

        with open("Students and Courses info.json", "w") as json_file:
            json.dump({"students": students_data, "courses": courses_data}, json_file, indent=4)
        print("Data saved to Students and Courses info.json")

    elif option == 8:
        with open("Students and Courses info.json", "r") as json_file:
            data = json.load(json_file)
        print(data)

    else:
        print(f'Invalid option')
