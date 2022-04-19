def listStudents():
    
    print("List students:")
    for student in StudentList:
        print(f"{student.id}    {student.name}  {student.dob}")


def listCourses():
    
    print("List of courses")
    for course in CourseList:
        print(f"{course.id}     {course.name}       {course.credit}")        
        

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


#Average mark
def calAverage(self):
    MarkSum = 0;
    for courseMark in self.MarkList:
        MarkSum += courseMark["mark"]
    average = MarkSum / len(self.MarkList)
    return math.floor(average * 10) / 10

def sortAverageMark(ListStudents):
    listStudents.sort(key=lambda student: student.getaverage(),reverse = False)