# Project 1: Student Management System
# Level: Beginner | Estimated time: 2–3 hours
# 🎯 Objective
# Build a program that manages student records.

# Each student should have:
# - Student ID
# - Name
# - Age
# - Marks
# - Grade

# Requirements
# 1. Add a new student.
# 2. Display all students.
# 3. Search for a student using their ID.
# 4. Update a student's marks.
# 5. Delete a student record.
# 6. Calculate the average marks of all students.
# 7. Display students who scored above 80.
# 8. Handle invalid input using try-except.

# | Concept               | Application |
# ----------------------------------------------------------
# | Lists                 | Store multiple student records |
# | Dictionaries          | Store individual student details |
# | Loops                 | Display and search records |
# | Conditions            | Determine grades |
# | Functions             | Separate each operation |
# | Try-except            | Handle invalid marks and IDs |
import sys
 

import sys

StudentDetail = {}

def addStudent():
    print("=== Add New Student ===")

    StudentName = input("Enter student name: ").strip().title()

    if StudentName.lower() in ("exit", "quit"):
        print("Exiting application")
        sys.exit()

    while True:
        try:
            StudentAge = int(input("Enter student age: "))
            if StudentAge <= 0 or StudentAge >= 30:
                print("Age must be greater than zero and small then 30")
                continue
            break
        except ValueError:
            print("Enter a valid number for age")

    while True:
        try:
            StudentMarks = float(input("Enter student marks (0-100): "))
            if not 0 <= StudentMarks <= 100:
                print("Marks must be between 0 and 100")
                continue
            break
        except ValueError:
            print("Enter valid numeric marks")

    while True:
        StudentGrade = input("Enter student grade (A/B/C/D/F): ").strip().upper()

        if len(StudentGrade) == 1 and StudentGrade in ("A", "B", "C", "D", "F"):
            break
        else:
            print("Enter exactly one valid grade: A, B, C, D, or F")

    StudentID = int(input("Enter student ID: "))

    StudentDetail[StudentID] = {
        "Name": StudentName,
        "Age": StudentAge,
        "Marks": StudentMarks,
        "Grade": StudentGrade
    }
    print("Student added successfully!")



def displayAllStudent():
    print(" ===All students=== ")
    print(StudentDetail)



def searchStudent():
    print(" ===Search student detail=== ")

    while True:
        try:
            SearchStudentID = int(input("Enter Student ID: "))
            break
        except ValueError:
            print("Enter numbers only!")
            continue
    if SearchStudentID in StudentDetail:
        print("Student found!")
        print(StudentDetail[SearchStudentID])
    else:
        print("Student ID not found.")



def updateStudentMark():
    print(" ===Update student marks=== ")
    while True:
    
        try:
          StudentIDtoUpdateMark= int(input("Enter student ID"))
        except ValueError:
            print("Enter only number")
            continue

        if StudentIDtoUpdateMark in StudentDetail:
             print("Student found")
             break
        else:
             print("Student not found. Enter valid student ID")

    while True:
        try:
            StudentMarkToUpdate = float(input("Enter new marks: "))

            if not 0 <= StudentMarkToUpdate <= 100:
                print("Marks must be between 0 and 100.")
                continue

            break
        except ValueError:
            print("Enter valid numeric marks!")

        StudentDetail[StudentIDtoUpdateMark]["Marks"] = StudentMarkToUpdate

    print("Student marks updated successfully!")
    print(StudentDetail[StudentIDtoUpdateMark])


def deleteStudentRecord():
    print(" ===Delete a student record=== ")

    while True:
        try:
            StudentIDtoDelete= int(input("Enter Student ID to delete"))
        except ValueError:
            print("Enter only number")
            continue
        if StudentIDtoDelete in StudentDetail:
            print("Student found")
            break
        else:
            print("Record not found. Enter valid Student ID")
                

    StudentDetail.pop(StudentIDtoDelete)
    print("Student record deleted successfully!")



def avarageMarks():
    print(" ===Calculate the average marks of all students=== ")
    TotalMarks=0
    AvgMarks = 0
   
    if len(StudentDetail) == 0:
        print("No student records available")
        return

    for student in StudentDetail.values():
            TotalMarks += student["Marks"]

    AvgMarks == float(TotalMarks/len(StudentDetail))
    print(f"Avg marks are : {AvgMarks}")
        

def Studentabove80Score():
    print(" ===Display students who scored above 80=== ")

    StudentMoreThan80 = {}

    for StudentID, student in StudentDetail.items():
        if student["Marks"] > 80:
            StudentMoreThan80[StudentID] = student

    if StudentMoreThan80:
        for StudentID, student in StudentMoreThan80.items():
            print(f"ID: {StudentID}, Name: {student['Name']}, Marks: {student['Marks']}")
    else:
        print("No student has scored above 80")




while True:
    print("==== Welcome Student Management System ====")
    print("Press 1 to Add new student")
    print("Press 2 to Display All students")
    print("Press 3 to search student detail")
    print("Press 4 to update a student marks")
    print("Press 5 to delete a student record")
    print("Press 6 to Calculate the average marks of all students")
    print("Press 7 to Display students who scored above 80")
    print("Type Exit or stope to stope the program")

    UserInput = input("Enter your choice: ").strip().lower()

    if UserInput in ["exit", "stop"]:
        print("Exiting application")
        sys.exit()

    try:   
        UserInput= int(UserInput)
    except Exception:
        print("Enter only valid input")
        continue
    

    if UserInput==1:
        addStudent()
    elif UserInput == 2:
        displayAllStudent()
    elif UserInput == 3:
        searchStudent()
    elif UserInput == 4:
        updateStudentMark()
    elif UserInput == 5:
        deleteStudentRecord()
    elif UserInput == 6:
        avarageMarks()
    elif UserInput == 7:
        Studentabove80Score()
    else:
        print("Invalid choice! Please select between 1 and 7.")
