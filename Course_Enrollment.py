class Student:
    def __init__(self,name):
        self.name=name
        self.enrolled_courses=[]
    def get_name(self):
        return self.name
    def enroll_course(self,course):
        self.enrolled_courses.append(course)
    def drop_course(self,course):
        self.enrolled_courses.remove(course)
    def view_courses(self):
        return [i.get_name() for i in self.enrolled_courses]

class Course:
    def __init__(self,name,maximum_students):
        self.name=name
        self.maximum_students_allowed=maximum_students
        self.list_of_students_enrolled=[]
    def get_capacity(self):
        return self.maximum_students_allowed-len(self.list_of_students_enrolled)
    def get_name(self):
        return self.name
    def enroll(self,student):
        self.list_of_students_enrolled.append(student)
    def drop(self,student):
        self.list_of_students_enrolled.remove(student)
    def view_students(self):
        return [i.get_name() for i in self.list_of_students_enrolled]
    def search_student(self,student):
        if student in self.list_of_students_enrolled:
            return True
        return False

class EnrollmentSystem:
    def __init__(self):
        pass
    def enroll(self,course,student):
        if course.search_student(student)==False and course.get_capacity()!=0:
            course.enroll(student)
            student.enroll_course(course)
            print("Successfully Enrolled")
        elif course.search_student(student):
            print("Already Enrolled")
        elif course.get_capacity()==0:
            print("Course is full!")
    def drop(self,course,student):
        if course.search_student(student):
            course.drop(student)
            student.drop_course(course)
            print("Successfully dropped")
        elif course.search_student(student)==False:
            print("You are not enrolled in this course!")
