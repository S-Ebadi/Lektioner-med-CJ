
class Student():
    def __init__(self, name, age, school, courses):
        self.name = name
        self.age = age
        self.school = school
        self.courses = courses

class Teacher():
    pass

class Admin():
    pass

# Vad är en student i vårt program?

def create_student_as_list(name, age, school):
    new_student = [name, age, school]
    return new_student

student = ["Said", 41, "Chas"]
student1 = ["Mika", 37, "Academy"]
student2 = ["Anna", 29, "Chas Academy"]

student_dict = {
    "name": "Said",
    "age": 41,
    "school": "Chas"
}

student1_dict = {
    "name": "Mika",
    "age": 37,
    "school": "Academy"
}

student4 = create_student_as_list("Vincent", 31, "Chas Academy")

saids_courses = ["Python", "JavaScript", "HTML"]

student5 = Student("Alexander", 25, "Chas Academy", saids_courses)

if "Python" in saids_courses:
    print("Said läser in Python")

