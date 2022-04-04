StudentList = []
CourseList = []

#Create class for student
class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.id = student_id
        self.name = student_name
        self.dob = student_dob
    def printStudent(self):
        print(f"{self.id}   {self.name}     {self.dob}")

#Create class for course        
class Course:
    def __init__(self, course_id, course_name):
        self.id = course_id
        self.name = course_name
    def printCourse(self):
        print(f"{self.id}   {self.name}")
        

#input student info
def inputStudent():
    
    print("Input student information")
    studentCount = int(input("Enter students number: "))
    for i in range(0, studentCount):
        student_id = str(input("Enter student's ID: "))
        student_name = str(input("Enter student's name: "))
        student_dob = str(input("Enter student's DoB: "))
        StudentList.append(Student(student_id, student_name, student_dob))

#input course info
def inputCourse():
    
    print("Input course information")
    courseCount = int(input("Enter courses number: "))
    for i in range(0, courseCount):
        course_id = str(input("Enter course's ID: "))
        course_name = str(input("Enter course's name: "))
        CourseList.append(Course(course_id, course_name))



def listStudents():
    
    print("List students:")
    for student in StudentList:
        print(f"{student.id}    {student.name}  {student.dob}")


def listCourses():
    
    print("List of courses")
    for course in CourseList:
        print(f"{course.id}     {course.name}")        
        

#input marks for student with selected course        
def inputMarks():
    
    print("Input student marks")
    course_id = str(input("Enter course ID: "))
    for course in CourseList:
        if course.id == course_id:
            marksList = {}
            for student in StudentList:
                mark = float(input(f"Enter mark for {student.name} {student.id}: "))
                thisMark = {course.name:mark}
                student.marks = thisMark
                marksList.update({student.id:mark})
                course.marksList = marksList
        break
                

#show marks for student with selected course    
def showMarks():
    
    print("Show marks:")
    course_id = str(input("Enter course ID: "))
    for course in CourseList:
        if course.id == course_id:
            sid = list(course.marksList.keys())
            smark = list(course.marksList.values())
            for i in range(0, len(sid)):    
                print(f"{sid[i]}    {smark[i]}")
        break

            
inputStudent()
inputCourse()
inputMarks()
listCourses()
listStudents()
showMarks()