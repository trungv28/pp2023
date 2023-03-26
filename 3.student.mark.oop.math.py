import math
import numpy as np
from collections import defaultdict

class Entity:
    def __init__(self, name, id):
        self._name = name
        self._id = id
    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @property
    def info(self):
        pass
    
class Student(Entity):
    def __init__(self, id, name, dob):
        super().__init__(name, id)
        self.__dob = dob
    
    @property
    def dob(self):
        return self.__dob
    
    @Entity.info.getter
    def info(self):
        return f'{self.id:10}{self.name:20}{self.dob:15}'

class Course(Entity):
    def __init__(self, id, name, credit):
        super().__init__(name, id)
        self.__credit = credit

    @property
    def credit(self):
        return self.__credit

    @Entity.info.getter
    def info(self):
        return f'{self.id:10}{self.name:15}'
    
class Mark():
    def __init__(self, course, student, mark):
        self.course = course
        self.student = student
        self.__mark = mark

    @property
    def course_id(self):
        return self.course.id
    
    @property
    def student_id(self):
        return self.student.id
    
    @property
    def mark(self):
        return self.__mark
    
    @property
    def course_credit(self):
        return self.course.credit
    
    @property
    def info(self):
        return f'{self.course_id:10}{self.student_id:10}{self.mark:10}'

class EntityManager:
    def __init__(self):
        self._data = None
    
    def add_info(self):
        pass

    def display(self):
        pass
    
class StudentManager(EntityManager):
    def __init__(self):
        self._data = {}
        self.__num_student = 0
        
    @property   
    def num_student(self):
        return self.__num_student
    
    @num_student.setter
    def num_student(self, num_student):
        if num_student < 0:
            print('Not a valid number')
            return
        else:
            self.__num_student = num_student
    
    @property
    def data(self):
        return self._data
        
    def add_info(self):
        self.num_student = int(input('Enter the number of the student: '))
        for _ in range(self.num_student):
            id = input('Enter the ID of the student: ')
            student = Student(id,
                              input('Enter the name of the student: '),
                              input('Enter the dob of the student: '))
            self._data[id] = student

    def display(self):
        for student in self._data.values():
            print(student.info)

class CourseManager(EntityManager):
    def __init__(self):
        self._data = {}
        self.__num_course = 0

    @property   
    def num_course(self):
        return self.__num_course
    
    @num_course.setter
    def num_course(self, num_course):
        if num_course < 0:
            print('Not a valid number')
            return
        else:
            self.__num_course = num_course
        
    def add_info(self):
        self.num_course = int(input('Enter the number of the course: '))
        for _ in range(self.num_course):
            id = input('Enter the ID of the course: ')
            course = Course(id,
                            input('Enter the name of the course: '),
                            input('Enter the number of credits in the course: '))
            self._data[id] = course

    def display(self):
        for course in self._data.values():
            print(course.info)

    def check(self, id):
        valid = None
        if id in self._data.keys():
            valid = self._data[id]
        else:
            print('This course does not exist')
        return valid
    
class MarkManager(EntityManager):
    def __init__(self):
        self._data = []

    def add_info(self, student_manager, course_manager):
        course_id = input('Enter the course id you want to input the mark: ')
        course = course_manager.check(course_id)
        if course == None: return
        for student in student_manager.data.values():
            mark = math.floor(float(input(f'Enter the mark for {student.name}: '))*10) / 10
            self._data.append(Mark(course, student, mark))

    def display(self):
        for mark in self._data:
            print(mark.info)

    def rank_GPA(self):
        student_mark = defaultdict(list)
        for mark in self._data:
            student_mark[mark.student_id].append(mark)
    

        rank_list = np.array(list(student_mark.values()))
        gpa_list = np.apply_along_axis(lambda key: np.average([gpa.mark for gpa in key],\
                        weights=[float(gpa.course_credit) for gpa in key]), 1, rank_list)
        inds = np.argsort(gpa_list)
        gpa_list = gpa_list[inds[::-1]]
        rank_list = rank_list[inds[::-1]]
        for gpa, rank in zip(gpa_list,rank_list):
            print(f'{rank[0].student_id:10}{gpa:10}')

if __name__ =='__main__':
    student_manager = StudentManager()
    student_manager.add_info()
    student_manager.display()

    course_manager = CourseManager()
    course_manager.add_info()
    course_manager.display()

    mark_manager = MarkManager()
    mark_manager.add_info(student_manager, course_manager)
    mark_manager.add_info(student_manager, course_manager)

    mark_manager.display()
    mark_manager.rank_GPA()
