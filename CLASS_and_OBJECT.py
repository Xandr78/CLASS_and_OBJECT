class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    # Метод выставления оценок лекторам
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    # Метод для вывода данных по студентам
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_score(self)}\nКурсы в процессе изучения: {", ".join(map(str,student_1.courses_in_progress))}\nЗавершенные курсы: {", ".join(map(str,student_1.finished_courses))}'
        return res
    # Метод для сравнения студентов по оценкам за дз
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student!')
            return
        return average_score(self) < average_score(other)        
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []
    
    # Метод для вывода данных по лекторам
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_score(self)}'
        return res
    # Метод для сравнения между собой лекторов по средней оценке за лекции
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer!')
            return
        return average_score(self) < average_score(other) 

class Reviewer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    
    # Метод выставления оценок студентам за домашние задания
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Метод для вывода данных по экспертам
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

# Функция подсчета средней оценки за лекции всех лекторов в рамках курса
def average_score_all_lecturer(lecturers, courses):
    sum_score = 0
    counter = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if courses in key:
                sum_score += sum(value) / len(value)
                counter += 1
    return round(sum_score / counter, 2)

# Функция подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_score_all_hw_student(students, courses):
    sum_score = 0
    counter = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                sum_score += sum(value) / len(value)
                counter += 1
    return round(sum_score / counter, 2)

# Функция расчёта cредней оценки одного лектора или одного студента
def average_score(past):
    sum = 0
    counter = 0
    for key, value in past.grades.items():
        for val in value:    
            sum += val
            counter += 1
    return round(sum / counter, 2)

student_1 = Student('Nikolai', 'Zarubov', 'man')
student_2 = Student('Elena', 'Prekrasnay', 'woman')
student_3 = Student('Alexander', 'Makedonskei', 'man')

lecturer_1 = Lecturer('Vlad', 'Dracula')
lecturer_2 = Lecturer('Jon', 'Smith')
    
reviewer_1 = Reviewer('Artem', 'Korobov')
reviewer_2 = Reviewer('Jin', 'Gray')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

lecturer_1.grades['Git'] = [7, 2, 6]
lecturer_1.grades['Python'] = [10, 10, 8, 10, 10, 10]
lecturer_1.grades['ООП'] = [10, 10]

lecturer_2.grades['Git'] = [2, 2, 10]
lecturer_2.grades['Python'] = [1, 3, 5, 1]
lecturer_2.grades['ООП'] = [5, 4]

student_1.grades['Git'] = [5, 8]
student_1.grades['ООП'] = [10]
student_1.grades['Python'] = [3, 2, 9]

student_2.grades['Git'] = [1, 3]
student_2.grades['ООП'] = [4]
student_2.grades['Python'] = [10, 8, 6]

student_1.finished_courses += ['Введение в программирование']
student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['ООП', 'Python']
lecturer_1.courses_attached += ['Python', 'Git', 'ООП']
lecturer_2.courses_attached += ['Python', 'Django']

# Список студентов и список лекторов
student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]

print('Задание № 3. Полиморфизм и магические методы')
print()
print('some_reviewer')
print(reviewer_1.__str__())
print()
print('some_lecturer')
print(lecturer_1.__str__())
print()
print('some_student')
print(student_1.__str__())
print()

print('Сравнения')
print('средняя оценка за лекции у Vlad Dracula не меньше, чем у Jon Smith')
print(lecturer_1.__lt__(lecturer_2))
print('средняя оценка за дз у Nikolai Zarubov не меньше, чем у Elena Prekrasnay')
print(student_1.__lt__(student_2))
print()
print('Задание № 4. Полевые испытания')
print('Подсчет средней оценки за лекции всех лекторов в рамках курса:')
print(average_score_all_lecturer(lecturer_list, 'Python'))
print('Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса:')
print(average_score_all_hw_student(student_list, 'Python'))
print()
print('Задание № 2. Атрибуты и взаимодействие классов')
# Метод выставления оценок студентам за дз (ПРОВЕРКА)
print('Метод выставления оценок студентам за дз (ПРОВЕРКА):')
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Python', 2)
print(student_1.grades)

# Метод выставления оценок лекторам за лекцию (ПРОВЕРКА)
print('Метод выставления оценок лекторам за лекцию (ПРОВЕРКА):')
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 10)
print(lecturer_1.grades)
