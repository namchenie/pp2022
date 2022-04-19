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
        course_credit = int(input("Enter course's credit: "))
        CourseList.append(Course(course_id, course_name, course_credit))




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
                print(f"{sid[i]}   {smark[i]}")
        break

