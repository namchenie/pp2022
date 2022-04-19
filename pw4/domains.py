#Create class for student
class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.id = student_id
        self.name = student_name
        self.dob = student_dob


    def CourseMark(self, course, mark):
        courseMark = {
            "course" : course,
            "mark" : mark
        }   
        self.MarkList.append(courseMark)

    def printStudent(self):
        print(f"{self.id}   {self.name}     {self.dob}")

#Create class for course        
class Course:
    def __init__(self, course_id, course_name, course_credit):
        self.id = course_id
        self.name = course_name
        self.credit = course_credit
    def printCourse(self):
        print(f"{self.id}   {self.name}     {self.credit}")