# класс Студент
student_list = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        student_list.append(self)

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_to_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and \
                course in lecturer.courses_attached and 1 <= rate <= 10:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            print('Ошибка')

    def average_grades(self):
        grades_sum = 0
        count = 0
        for grade in self.grades.values():
            for num in grade:
                grades_sum += num
                count += 1
        return round(grades_sum / count, 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average_grades() < other.average_grades()

    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за домашние задания:' \
               f' {self.average_grades()}, \nКурсы в процессе изучения: {self.courses_in_progress},' \
               f'\nЗавершенные курсы: Введение в программирование'


# класс Ментор
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def add_courses(self, course_name):
        self.courses_attached.append(course_name)


lecturer_list = []


# класс Лектор
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rates = {}
        self.courses_attached = []
        lecturer_list.append(self)

    def average_rate(self):
        count = 0
        rates_sum = 0
        for rate in self.rates.values():
            for nums in rate:
                rates_sum += nums
                count += 1
        return round(rates_sum / count, 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average_rate() < other.average_rate()

    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за лекции: {self.average_rate()}'


# класс Ревьюер
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)
        self.courses_attached = []

    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         print('Ошибка')

    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}'


def average_student_grade_by_course(student_list, course):
    sum_grade = 0
    count = 0
    for student in student_list:
        if course not in student.grades.keys():
            pass
        else:
            for grade in student.grades[course]:
                sum_grade += grade
                count += 1
    return print(round(sum_grade / count, 2))


def average_lecturer_rate_by_course(lecturer_list, course):
    sum_rate = 0
    count = 0
    for lecturer in lecturer_list:
        if course not in lecturer.rates.keys():
            pass
        else:
            for rate in lecturer.rates[course]:
                sum_rate += rate
                count += 1
    return print(round(sum_rate / count, 2))


# вызов по 2 экземпляра класса
first_mentor = Mentor('Rick', 'Davis')
second_mentor = Mentor('Eva', 'Esteban')

first_lecturer = Lecturer('Peter', 'Smith')
# print(first_lecturer.name)
# print(first_lecturer.surname)
second_lecturer = Lecturer('Eman', 'Odin')

first_student = Student('Pole', 'Ricks', 'male')
# print(first_student.name)
# print(first_student.surname)
second_student = Student('Emma', 'Jones', 'female')

first_reviewer = Reviewer('Anna', 'Kyle')
# print(first_reviewer.name)
# print(first_reviewer.surname)
# print(first_reviewer.courses_attached)
second_reviewer = Reviewer('Ros', 'Geller')

# вызов методов
first_lecturer.add_courses('Python')
first_lecturer.add_courses('Git')

# print(first_lecturer.courses_attached)
second_lecturer.add_courses('Git')
second_lecturer.add_courses('Python')
second_lecturer.add_courses('C++')

# print(second_lecturer.courses_attached)
first_student.add_courses('Python')
first_student.add_courses('Git')
second_student.add_courses('C++')
second_student.add_courses('Git')
first_student.rate_to_lecturer(first_lecturer, 'Python', 10)
second_student.rate_to_lecturer(first_lecturer, 'Git', 8)
first_student.rate_to_lecturer(second_lecturer, 'Python', 9)
second_student.rate_to_lecturer(second_lecturer, 'Git', 10)

print(first_student.courses_in_progress)
print(first_lecturer.rates)
print(first_lecturer.average_rate())
first_reviewer.rate_hw(first_student, 'Python', 9)
second_reviewer.rate_hw(first_student, 'Git', 10)
first_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Git', 7)
print(first_student.grades)
first_student.average_grades()
second_student.average_grades()
print(first_student.average_grades())

print(first_student)
print(first_lecturer)
print(first_reviewer)

print(first_student < second_student)
print(first_lecturer < second_lecturer)

average_student_grade_by_course(student_list, 'Python')
average_student_grade_by_course(student_list, 'Git')
average_lecturer_rate_by_course(lecturer_list, 'Python')
average_lecturer_rate_by_course(lecturer_list, 'Git')