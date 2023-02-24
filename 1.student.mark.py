# input number of student
def input_num_student():
    return int(input('Enter the number of students: '))

# input number of course
def input_num_course():
    return int(input('Enter the number of courses: '))

# return dictionary contains information of each student with id is the key value
def input_info_student(num_student:int):
    if(num_student == -1):
        print('You haven\'t input the number of student yet')
        return
    student_list = dict()
    for _ in range(num_student):
        info = dict()
        id = input('Enter the ID of the student: ')
        info['name'] = input('Enter the name of the student: ')
        info['dob'] = input('Enter the dob of the student: ')

        print('\n')
        student_list[id] = info
    return student_list

# return dictionary contains information of each course with id is the key value
def input_info_course(num_course:int):
    if(num_course == -1):
        print('You haven\'t input the number of courses yet.')
        return
    course_list = dict()
    for _ in range(num_course):
        info = dict()
        id = input('Enter the ID of the course: ')
        info['name'] = input('Enter the name of the course: ')
        info['student'] = list()

        print('\n')
        course_list[id] = info
    return course_list

def input_mark(course_list, student_list):
    if(len(student_list)==0 or len(course_list)==0):
        print('You haven\'t have the list of student/course yet')
        return
    while True:
        course_id = input('Enter the id of the course you want to input the mark: ')
        if (course_id in course_list.keys()):
            if (len(course_list[course_id]['student'])!=0):
                print('This course has already been input.')
            else:
                break
        else:
            print('The ID is not found!!! Please re-enter')
    
    for id in student_list.keys():
        mark = int(input(f'Enter the mark of the student {id} : '))
        course_list[course_id]['student'].append([id, mark])
    
    return course_list

def print_mark(course_list):
    if(len(course_list)==0):
        print('You haven\'t have the list of course yet')
        return
    while True:
        course_id = input('Enter the id of the course you want to print the mark: ')
        if(course_id in course_list.keys()):
            if (len(course_list[course_id]['student'])==0):
                print('This course\'s marks hasn\'t been input yet.')
            else:
                break
        else:
            print('The ID is not found!!! Please re-enter')

    print('\n')
    print('The mark of this course is as follow: ')
    print('ID\t\tMark')
    for i in range(len(course_list[course_id]['student'])):
        id = course_list[course_id]['student'][i][0]
        mark = course_list[course_id]['student'][i][1]
        print(id, '\t', mark)

def main():
    num_student, num_course = -1, -1
    student_list, course_list = dict(), dict()
    print(""" You can input as follow
    Type 1 to input number of students
    Type 2 to input number of courses
    Type 3 to input student info
    Type 4 to input course info
    Type 5 to input marks
    Type 6 to print the result
    Type other to exit\n
    """)

    while True:
        choice = int(input('Enter the action you want to do: '))
        if(choice == 1):
            num_student = input_num_student()
            print('\n')

        elif(choice == 2):
            num_course = input_num_course()
            print('\n')

        elif(choice == 3):
            student_list = input_info_student(num_student)

        elif(choice == 4):
            course_list = input_info_course(num_course)

        elif(choice == 5):
            course_list = input_mark(course_list, student_list)
            print('\n')

        elif(choice == 6):
            print_mark(course_list)

        else:
            break
    
if __name__ == '__main__':
    main()