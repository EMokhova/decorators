from statistics import mean
from log_decorator import log_decorator_fabric

log_gecor_1 = log_decorator_fabric('D:\pythonProject\decorators\log\my_log.txt')
log_gecor_2 = log_decorator_fabric('D:\pythonProject\decorators\log\logging.txt')


class Student:
    def __init__(self, name, surname, gender):
        self.avg = 0
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # @log_gecor_1
    def avg_student(self):
        list = []
        for grade in self.grades.values():
            list_avg = mean(grade)
            list.append(list_avg)
        self.avg = mean(list)
        return self.avg

    def __str__(self):
        sname = f'Имя: {self.name}'
        ssurname = f'Фамилия: {self.surname}'
        avg_s = Student.avg_student(self)
        avg_st = f'Cредняя оценка за домашние задания: {round(avg_s, 2)}'
        coursers_progress = f'Курсы в процессе обучения: {self.courses_in_progress}'
        finish_course = f'Завершенные курсы: {self.finished_courses}'
        res = sname + '\n' + ssurname + '\n' + avg_st + '\n' + coursers_progress + '\n' + finish_course
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Данный пользователь не является студентом!')
            return
        return self.avg < other.avg


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.avg = 0
        self.grades = {}

    def avg_lector(self):
        list = []
        for grade in self.grades.values():
            list_avg = mean(grade)
            list.append(list_avg)
        self.avg = mean(list)
        return self.avg

    def __str__(self):
        sname = f'Имя: {self.name}'
        ssurname = f'Фамилия: {self.surname}'
        avg_s = Lecturer.avg_lector(self)
        avg_lector = f'Cредняя оценка за лекции: {round(avg_s, 2)}'
        res = sname + '\n' + ssurname + '\n' + avg_lector
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Данный пользователь не является лектором!')
            return
        return self.avg < other.avg


class Reviewer(Mentor):
    def __init__(self, name, power):
        super().__init__(name, power)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        sname = f'Имя: {self.name}'
        ssurname = f'Фамилия: {self.surname}'
        res = sname + '\n' + ssurname
        return res


@log_gecor_1
def avg_all_students(student_list, course):
    list = []
    for student in student_list:
        if course in student.finished_courses or student.courses_in_progress:
            gr = student.grades.get(course)
            print(gr)
            avg_l = mean(gr)
            list.append(avg_l)
    avg_all = mean(list)
    print(f'Средняя оценка студентов по курсу {course} - {avg_all}')
    return avg_all


@log_gecor_2
def avg_all_lecturer(lecturer_list, course):
    list = []
    for lecturer in lecturer_list:
        if course in lecturer.courses_attached:
            gr = lecturer.grades.get(course)
            print(gr)
            avg_l = mean(gr)
            list.append(avg_l)
    avg_all = mean(list)
    print(f'Средняя оценка лекторов по курсу {course} - {avg_all}')
    return avg_all


if __name__ == '__main__':
    student1 = Student('Ruoy', 'Eman', '21')
    student2 = Student('Jon', 'Martin', '22')
    student1.courses_in_progress += ['Python']
    student1.courses_in_progress += ['C++']
    student1.add_courses('Pascal')
    student2.courses_in_progress += ['Python']
    student2.courses_in_progress += ['Delphi']
    student2.add_courses('Pascal')

    reviewer1 = Reviewer('Some', 'Buddy')
    reviewer2 = Reviewer('Ilon', 'Parker')

    reviewer1.courses_attached += ['Python']
    reviewer2.courses_attached += ['C++']
    reviewer1.courses_attached += ['Pascal']
    reviewer2.courses_attached += ['Delphi']

    reviewer1.rate_hw(student1, 'Python', 5)
    reviewer1.rate_hw(student1, 'Python', 4)
    reviewer1.rate_hw(student1, 'Python', 7)
    reviewer1.rate_hw(student2, 'Python', 8)
    reviewer1.rate_hw(student2, 'Python', 6)
    reviewer1.rate_hw(student2, 'Python', 9)
    reviewer2.rate_hw(student1, 'C++', 10)
    reviewer2.rate_hw(student1, 'C++', 8)
    reviewer2.rate_hw(student1, 'C++', 9)
    reviewer2.rate_hw(student2, 'Delphi', 7)
    reviewer2.rate_hw(student2, 'Delphi', 9)
    reviewer2.rate_hw(student2, 'Delphi', 9)

    lecturer1 = Lecturer('Bob', 'Simpson')
    lecturer2 = Lecturer('Jack', 'Maplon')

    lecturer1.courses_attached += ['Python']
    lecturer2.courses_attached += ['C++']
    lecturer1.courses_attached += ['Delphi']
    lecturer2.courses_attached += ['Pascal']

    student1.rate_hw(lecturer1, 'Python', 9)
    student1.rate_hw(lecturer1, 'Python', 10)
    student1.rate_hw(lecturer1, 'Python', 9)
    student1.rate_hw(lecturer2, 'C++', 8)
    student1.rate_hw(lecturer2, 'C++', 9)
    student1.rate_hw(lecturer2, 'C++', 9)
    student2.rate_hw(lecturer1, 'Delphi', 8)
    student2.rate_hw(lecturer1, 'Delphi', 8)
    student2.rate_hw(lecturer1, 'Delphi', 10)
    student2.rate_hw(lecturer2, 'Pascal', 10)
    student2.rate_hw(lecturer2, 'Pascal', 9)
    student2.rate_hw(lecturer2, 'Pascal', 10)
    student1.avg_student()
    student2.avg_student()

    print(student1.grades)
    print(student2.grades)
    print(lecturer1.courses_attached)
    print(lecturer2.courses_attached)
    print(lecturer1.grades)
    print(lecturer2.grades)

    print(reviewer1)
    print(reviewer2)
    print(lecturer1)
    print(lecturer2)
    print(student1)
    print(student2)

    print(student1.avg)

    print(student1 < student2)
    print(lecturer1 > lecturer2)

    avg_all_students([student1, student2], 'Python')
    avg_all_lecturer([lecturer1, lecturer2], 'Python')
