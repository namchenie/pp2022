#Input number of students in a class
def numOfStudent():
    StudentCount = int(input("Enter the number of students: "))
    if StudentCount < 0:
        print("Invalid number! Please enter again.")
    else:
        return StudentCount


#Input student information: id, name, DoB
def inputStudentInformation(StudentCount):

    students = []

    for i in range(0, StudentCount):

        id = input("Enter student's ID: ")
        name = input("Enter student's name: ")
        dob = input("Enter sutdent's DoB: ")

        student = {
            "id" : id,
            "name" : name,
            "dob" : dob,
            "marks" : {}
        }

        students.append(student)

    return students
       

#Input number of course
def numofCourse():
    CourseCount = int(input("Enter the number of courses: "))
    if CourseCount < 0:
        print("Invalid number! Please enter again.")
    else:
        return CourseCount


#Input course information: id, name
def InputCourseInformation(CourseCount):

    courses = []

    for i in range(0, CourseCount): 
        id = input("Enter course's ID: ")
        name = input("Enter course's name: ")
        course = {
            "id" : id,
            "name" : name
        }

        courses.append(course)

    return courses



#List courses
def listCourses(courses):
    print("\n All courses list")
    for course in courses:
        print(f"{course['id']: <10}     {course['name']: <30}")



# #Select course
def selectCourses(courses):
    listCourses(courses)
    courseid = input("Enter course ID: ")
    return courseid


#Input marks for student in the selected course
def inputMark(courseid, students):
    print(f"Enter marks of the course {courseid} for students: ")
    for student in students:
        mark = float(input(f"- Student {student['id']} {student['name']} "))
        student["marks"][courseid] = mark


#List students
def listStudents(students):
    print("\n All students list")
    for student in students:
        print(f"{student['name']: <20}   {student['id']: <10}   {student['dob']: <15}")


#Show students marks
def showMark(courseid, students):
    print(f"\nAll marks for the course {courseid}: ")
    for student in students:
        print(f"{student['name']: <20}  {student['marks'][courseid]}")


#Enter student count and information
StudentCount = numOfStudent()
students = inputStudentInformation(StudentCount)
listStudents(students)

#Enter course count and information
CourseCount = numofCourse()
courses = InputCourseInformation(CourseCount)
listCourses(courses)

#Select course and input mark for students
courseid = selectCourses(courses)
inputMark(courseid, students)

#Show marks for a given course
courseid = selectCourses(courses)
showMark(courseid, students)

