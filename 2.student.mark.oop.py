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
    def __init__(self, id, name):
        super().__init__(name, id)

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
                            input('Enter the name of the course: '))
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
            mark = int(input(f'Enter the mark for {student.name}: '))
            self._data.append(Mark(course, student, mark))

    def display(self):
        for mark in self._data:
            print(mark.info)

if __name__ =='__main__':
    student_manager = StudentManager()
    student_manager.add_info()
    student_manager.display()

    course_manager = CourseManager()
    course_manager.add_info()
    course_manager.display()

    mark_manager = MarkManager()
    mark_manager.add_info(student_manager, course_manager)
    mark_manager.display()