# from operator import le

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor): # Задание 1 
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def ocenka_studentov(self, student, course, grade): # Задание 2 
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self): # Задание 3
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

#Оценивание лекторов студентами:

    def ocenivanie_lektorov_studentami(self, lecturer, course, grade): # Задание 2
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
 
#Средняя оценка студента за домашние задание  
    
    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 1)
        return average_rating

#Средняя оценка студента в рамках конкретного курса
    
    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 1)
        return average_rating               

    def __str__(self): #Задание 3
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Not a student"
        return self.av_rating() < other.av_rating()


class Lecturer(Mentor): #Задание 1

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 1)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 1)
        return average_rating   

    def __str__(self): # Задание 3
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_rating()}"
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Not a Lecturer!"
        return self.av_rating() < other.av_rating(self)
    

#Задание 4
# Студенты
student1 = Student('Петя', 'Петров', 'муж')
student1.courses_in_progress += ['Python']
student1.finished_courses += ["Введение в програмирование"]


student2 = Student('Юлия', 'Чернова', 'жен')
student2.courses_in_progress += ['Python']
student2.finished_courses += ["Введение в програмирование"]

# Лекторы
lecturer1 = Lecturer('Виктор', 'Стрельцов')
lecturer1.courses_attached += ['Python']
 
lecturer2 = Lecturer('Мария', 'Колесниченко')
lecturer2.courses_attached += ['Python']

# Проверяющие
reviewer1 = Reviewer('Матвей', 'Иванов')
reviewer1.courses_attached += ['Python']
 
reviewer2 = Reviewer('Кондрат', 'Афанасьев')
reviewer2.courses_attached += ['Python']

# Оценки студентам
reviewer1.ocenka_studentov(student1, 'Python', 8)
reviewer1.ocenka_studentov(student1, 'Python', 7)
reviewer1.ocenka_studentov(student1, 'Python', 5)

reviewer2.ocenka_studentov(student2, 'Python', 9)
reviewer2.ocenka_studentov(student2, 'Python', 8)
reviewer2.ocenka_studentov(student2, 'Python', 4)

# Оценки лекторам
student1.ocenivanie_lektorov_studentami(lecturer1, 'Python', 10)
student1.ocenivanie_lektorov_studentami(lecturer1, 'Python', 6)
student1.ocenivanie_lektorov_studentami(lecturer1, 'Python', 8)

student2.ocenivanie_lektorov_studentami(lecturer2, 'Python', 9)
student2.ocenivanie_lektorov_studentami(lecturer2, 'Python', 7)
student2.ocenivanie_lektorov_studentami(lecturer2, 'Python', 8)

student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]
reviewer_list = [reviewer1, reviewer2]


#Средняя оценка студентов в рамках курса

def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 1)
    return average_rating


print(average_rating_for_course('Python', student_list))
print(average_rating_for_course('Python', lecturer_list))
print(f"Студент1\n{student1}")
print(f"Студент2\n{student2}")
print(f"Лектор1\n{lecturer1}")
print(f"Лектор2\n{lecturer2}")
# print(Lecturer.__lt__(lecturer1,student1))