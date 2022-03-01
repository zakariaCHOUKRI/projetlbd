from abc import ABC

class University:
    """This is the university class"""

    def __init__(self, name: str, address: str, website: str, telephone: str, email: str, date_founded: str, list_of_schools: list):
        self.name = name
        self.address = address
        self.website = website
        self.telephone = telephone
        self.email = email
        self.date_founded = date_founded
        self.list_of_schools = list_of_schools

    def display(self):
        print("name:", self.name,
            "\naddress:", self.address,
            "\nwebsite:", self.website,
            "\ntelephone:", self.telephone,
            "\nemail:", self.email,
            "\ndate_founded:", self.date_founded,
            "\nlist_of_schools:", self.list_of_schools)


class School:
    """This is the school class"""

    def __init__(self, name: str, address: str, website: str, telephone: str, email: str, date_founded: str, list_of_programs: list):
        self.name = name
        self.address = address
        self.website = website
        self.telephone = telephone
        self.email = email
        self.date_founded = date_founded
        self.list_of_programs = list_of_programs

    def display(self):
        print("name:", self.name,
              "\naddress:", self.address,
              "\nwebsite:", self.website,
              "\ntelephone:", self.telephone,
              "\nemail:", self.email,
              "\ndate_founded:", self.date_founded,
              "\nlist_of_programs:", self.list_of_programs)


class Program:
    """This is the school class"""

    def __init__(self, name: str, address: str, website: str, telephone: str, email: str, date_founded: str, list_of_courses: list, list_of_students: list):
        self.name = name
        self.address = address
        self.website = website
        self.telephone = telephone
        self.email = email
        self.date_founded = date_founded
        self.list_of_courses = list_of_courses
        self.list_of_students = list_of_students

    def display(self):
        print("name:", self.name,
              "\naddress:", self.address,
              "\nwebsite:", self.website,
              "\ntelephone:", self.telephone,
              "\nemail:", self.email,
              "\ndate_founded:", self.date_founded,
              "\nlist_of_subjects:", self.list_of_courses,
              "\nlist_of_students:", self.list_of_students)

class Person(ABC):
    """This is the person class"""

    def __init__(self, name: str, ID: int, email: str):
        self.name = name
        self.ID = ID
        self.email = email

    def display(self):
        pass

class Student(Person):
    """This is the student class"""

    def __init__(self, name: str, ID: int, email: str, Program: Program, enrolled_courses: list):
        super().__init__(name, ID, email)
        self.Program = Program
        self.enrolled_courses = enrolled_courses
        self.course_grades = {i: {"TP": None, "DS": None, "Project": None, "TD": None, "final": None} for i in enrolled_courses}

    def get_course_grades(self, course):
        return self.course_grades[course]

    def get_enrolled_courses(self):
        return self.enrolled_courses


class Course:
    """This is the course class"""


    def __init__(self, name, Students, Professor, infos: dict = None):
        self.name = name
        self.Students = Students
        self.infos = infos
        self.Professor = Professor
        self.elements = ["DS", "TP", "TD", "Project"]
        self.coeffs = {i:0 for i in self.elements}


    def set_coeff(self):
        for i in self.elements:
            self.coeffs[i] = float(input(f"{i} coeff: "))


    def set_grades(self):

            for student in sorted(self.Students):
                student.course_grades[self.name]["TP"] = float(input(f"{student} TP: "))
                student.course_grades[self.name]["DS"] = float(input(f"{student} DS: "))
                student.course_grades[self.name]["TD"] = float(input(f"{student} TD: "))
                student.course_grades[self.name]["Project"] = float(input(f"{student} Project: "))


    def set_final_grade(self):
        for student in sorted(self.Students):
            for i in ["TP", "DS", "TD", "Project"]:
                if student.course_grades[self.name][i] == None:
                    student.course_grades[self.name][i] = 0
