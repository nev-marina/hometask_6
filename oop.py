class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_mark = float()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        res = []
        sum_grades = 0
        for grade in self.grades.values():
            res += grade
            sum_grades = sum(res) / len(res)
        self.average_mark = sum_grades
        student_info = f'Имя: {self.name} \nФамилия: {self.surname} ' \
                       f'\nСредняя оценка за домашние задания: {self.average_mark}' \
                       f' \nКурсы в процессе изучения: {courses_in_progress_str} ' \
                       f'\nЗавершенные курсы: {finished_courses_str}'
        return student_info

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнить нельзя')
            return
        return self.average_mark < other.average_mark


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_mark = float()

    def __str__(self):
        res = []
        sum_grades = 0
        for grade in self.grades.values():
            res += grade
            sum_grades = sum(res) / len(res)
        self.average_mark = sum_grades
        lecturer_info = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_mark}'
        return lecturer_info

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнить нельзя')
            return
        return self.average_mark < other.average_mark


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_info = f'Имя: {self.name} \nФамилия: {self.surname}'
        return reviewer_info


best_student = Student('Marla', 'Singer', 'female')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Java']
best_student.finished_courses += ['C+']

worst_student = Student('Tyler', 'Durden', 'male')
worst_student.courses_in_progress += ['Python']
worst_student.finished_courses += ['C#']
worst_student.finished_courses += ['Pyton+']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Jack', 'Black')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

lecturer_1 = Lecturer('Jack', 'Daniels')
lecturer_1.courses_attached += ['Python']


lecturer_2 = Lecturer('John', 'Dow')
lecturer_2.courses_attached += ['Python']


# Оценки студентам
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 8)

reviewer_1.rate_hw(worst_student, 'Python', 6)
reviewer_1.rate_hw(worst_student, 'Python', 8)

reviewer_2.rate_hw(best_student, 'Python', 10)
reviewer_2.rate_hw(best_student, 'Python', 10)

reviewer_2.rate_hw(worst_student, 'Python', 7)
reviewer_2.rate_hw(worst_student, 'Python', 6)

# Оценки лекторам
best_student.rate_lecturer(lecturer_1, 'Java', 10)
best_student.rate_lecturer(lecturer_1, 'Python', 7)

best_student.rate_lecturer(lecturer_2, 'Python', 3)
best_student.rate_lecturer(lecturer_2, 'Python', 10)


worst_student.rate_lecturer(lecturer_1, 'Python', 10)
worst_student.rate_lecturer(lecturer_1, 'Pyton', 8)

worst_student.rate_lecturer(lecturer_2, 'Python', 4)
worst_student.rate_lecturer(lecturer_2, 'Python', 10)


print(best_student)
print(worst_student)
print()
print(lecturer_1)
print(lecturer_2)
print()
print(reviewer_1)
print(reviewer_2)
print()
print('Сравнение лекторов')
print(lecturer_1 > lecturer_2)
print()
print('Сравнение студентов')
print(best_student < worst_student)
print()

# Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
students_list = [best_student, worst_student]
def average_student_grade(students_list, course):
    sum_grades = 0
    count = 0
    for student in students_list:
        if student.courses_in_progress == [course]:
            sum_grades += student.average_mark
            count += 1
    av_grade = sum_grades / count
    return av_grade
print('Средняя оценка студентов')
print(average_student_grade(students_list, 'Python'))

#Подсчет средней оценки за лекции всех лекторов в рамках курса
lecturer_list = [lecturer_1, lecturer_2]
def av_lecturer_grade(lecturer_list, course):
    sum_grades = 0
    count = 0
    for lecturer in lecturer_list:
        if lecturer.courses_attached == [course]:
            sum_grades += lecturer.average_mark
            count += 1
    av_grade = sum_grades / count
    return av_grade

print('Средняя оценка у лекторов')
print(av_lecturer_grade(lecturer_list, 'Python'))