class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   

    def average_grade(self):
        sum_grades = 0
        count_grades = 0
        for keys, values in self.grades.items():
            for value in values:
                count_grades += 1
                sum_grades += value
        average = sum_grades / count_grades
        return average

    def rate_lec(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return "Ошибка"
    
    def __str__(self):
        courses_prog = ", ".join(self.courses_in_progress)
        courses_finish = ", ".join(self.finished_courses)
        message = f" Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашние задания: {self.average_grade()} \n Курсы в процессе изучения: {courses_prog} \n Завершённые курсы: {courses_finish}" 
        return message
    
    def __lt__(self, student):
        return self.average_grade() < student.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        message = f" Имя: {self.name} \n Фамилия: {self.surname}" 
        return message    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} 
    
    def average_grade(self):
        sum_grades = 0
        count_grades = 0
        for keys, values in self.grades.items():
            for value in values:
                count_grades += 1
                sum_grades += value
        average = sum_grades / count_grades
        return average
    
    def __str__(self):
        message = f" Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.average_grade()}" 
        return message

    def __lt__(self, lecture):
        return self.average_grade() < lecture.average_grade()

def average_grade_student(student_list, course):
    sum_av_grades = 0
    count_av_grades = 0
    for student in student_list:
        for grade in student.grades[course]:
            count_av_grades += 1
            sum_av_grades += grade
    average = sum_av_grades / count_av_grades
    return average

def average_grade_lecturer(lecturer_list, course):
    sum_av_grades = 0
    count_av_grades = 0
    for lecturer in lecturer_list:
        for grade in lecturer.grades[course]:
            count_av_grades += 1
            sum_av_grades += grade
    average = sum_av_grades / count_av_grades
    return average





best_student = Student('Sara', 'Jessica', 'female')
best_student.courses_in_progress += ['Python', 'Java']
best_student.add_courses("Введение в программирование")
best_student_2 = Student("Ivan", "Ivanov", "male")
best_student_2.courses_in_progress += ["Python", "Java"]
best_student_2.add_courses("Введение в программирование")

 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', "Java"]
cool_mentor_2 = Reviewer('Some', 'Reviewer')
cool_mentor_2.courses_attached += ['Python', "Java"]

 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 7)
cool_mentor_2.rate_hw(best_student_2, "Python", 5)
cool_mentor_2.rate_hw(best_student_2, "Python", 8)




cool_lec = Lecturer("Vanya", "Popov")
some_lec = Lecturer("Sasha", "Alexandrov")
some_lec.courses_attached += ["Python"]
cool_lec.courses_attached += ['Python']
best_student.rate_lec(cool_lec, "Python", 10)
best_student.rate_lec(cool_lec, "Python", 9) 
best_student.rate_lec(some_lec, "Python", 5)

students = [best_student, best_student_2]
lecturers = [cool_lec, some_lec]


print(best_student)
print(best_student.average_grade())
print(best_student_2.average_grade())
print(best_student > best_student_2)
print(cool_mentor)
print(some_lec.average_grade())
print(cool_lec.average_grade())
print(cool_lec)
print(cool_lec > some_lec)
print(average_grade_student(students, "Python"))
print(average_grade_lecturer(lecturers, "Python"))