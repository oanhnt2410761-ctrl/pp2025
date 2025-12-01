students = []
courses = []
marks = {}

def input_students():
    n = int(input("Please enter the number of student:"))
    for _ in range(n):
        sid = input("Student ID:")
        sname = input("Student's name:")
        sdob = input("Date of birth:")
        students.append({"ID": sid, "Name": sname, "DOB": sdob})
    print("Students have been added.\n")

def input_courses():
    m = int(input("Please enter the number of courses: "))
    for _ in range(m):
        cid = input("Course ID: ")
        cname = input("Course name: ")
        courses.append({"Course ID: ": cid, "Course name: ": cname})
    print("Courses have been added. \n")

def input_marks():
    if not courses:
        print("No courses available. Please input the course first. \n")
        return
    if not students:
        print("No student available. Please input the student first. \n")
        return 
    
    cid = input("Please enter the course ID to input marks for: ")

    course_ids = [course["Course ID: "] for course in courses]
    if cid not in course_ids:
        print("Course not found. \n")
        return 
    
    for student in students:
        while True:
            try:
                mark = float(input(f"Enter mark for {student['Name']}: "))
                break
            except ValueError:
                print("Invalid mark. Please enter a number. \n")
            marks[{student["ID"], cid}] = mark
print("Marks have been added. \n")

def list_students():
    if not students:
        print("No students available. \n")
        return
    print("List of students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")
    print()

def list_courses():
    if not courses:
        print("No students available. \n")
        return
    print("List of course:")
    for course in courses:
        print(f"ID: {course['id']}, Name:{course['name']}")
    print()

def list_marks():
    if not courses:
        print("No courses available. Please input the courses first. \n")
    if not students:
        print("No students available. Please input the students first. \n")
    
    cid = input("Please enter the course to enter the marks for: ")

    course_ids = [course in ["Course ID"] for course in courses]
    if cid not in course_ids:
        print("Course not found. \n")
        return
    
    print ("Marks for course{cid}:")
    for student in students:
        key = (student["ID"], cid)
        if key in marks:
            print(f"Student: {student['Name']}, Mark: {marks['key']}")
        else:
            print(f"Student: {student['Name']}, Mark: Not available.")

def main():
    while True:
        print("Menu:")
        print("1. Add students")
        print("2. Add courses")
        print("3. Add marks")
        print("4. List of students")
        print("5. List of courses ")
        print("6. List of marks")
        print("7. Exit")

        choice = input("Please enter your option (number between 1 - 7):")

        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif  choice == '6':
            list_marks()
        elif choice == '7':
            break 
main()