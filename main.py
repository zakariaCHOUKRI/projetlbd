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
        self.Staff = []

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
        self.final_grades = {i: None for i in enrolled_courses}

    def get_course_grades(self, course):
        return self.course_grades[course]

    def get_enrolled_courses(self):
        return self.enrolled_courses

    def get_final_grades(self, course):
        return self.final_grades[course]

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
        for elem in self.elements:
            if self.coeffs[elem] != 0:
                for student in sorted(self.Students):
                    student.course_grades[self.name][elem] = float(input(f"{student} {elem}: "))


    def set_final_grade(self):
        for student in sorted(self.Students):
            final_grade = 0
            for i in self.elements:
                if student.course_grades[self.name][i] != None:
                    final_grade += student.course_grades[self.name][i] * self.coeffs[i]
            student.final_grades[self.name] = final_grade

    def display_final_grades(self):
        return {i: i.final_grades[self.name] for i in self.Students}


class Professor(Person):
    """This is the Professor person"""
    
    def __init__(self, name: str, ID: int, email: str, Programs: list):
        super().__init__(name, ID, email)
        self.Programs = Programs

    def add_program(self, program):
        self.Programs.append(program)

    def get_programs(self):
        return self.Programs

class Promo:
    """This is the Promo class"""

    def __init__(self, students: list, year: str):
        self.year = year
        self.students = students
    
    def display(self):
        pass

fri = Student("free", 71, "fri@um6p.ma", ingenior_info, [LBD, analise])
basma = Student("bsma", 97, "bsma@um6p.ma", ingenior_info, [LBD, analise])
assklou = Professor("Assklou", 123, "assklou@um6p.ma", [ingenior_info])
mol_analyse = Professor("mol_analyse", 23, "analyse@um6p.ma", [ingenior_info])
lbd = Course("lbd", [fri, basma], assklou)
analise = Course("analyse", [fri, basma], mol_analyse)
ingenior_info = Program("ing cs", "bngrir", "um6p-cs.ma", "0811", "cs@um6p.ma", "2021", [lbd, analise], [fri, basma])
cs = School("cs", "bngrir", "um6p-cs.ma", "0811", "cs@um6p.ma", "2018", [ingenior_info])
um6p = University("um6p", "bngrir", "um6p.ma", "0811", "um6p@um6p.ma", "2013",)