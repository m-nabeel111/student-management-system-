"""
Student Management System - Python CRUD Project
By: M.Nabeel | BS Software Engineering - Indus University
GitHub: neelamwassan-naz
"""

import json
import os

FILE_NAME = "students.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_data(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

def add_student():
    students = load_data()
    print("\n--- Add New Student ---")
    student_id = input("Student ID: ")
    name = input("Full Name: ")
    department = input("Department: ")
    gpa = input("GPA: ")
    
    students.append({
        "id": student_id,
        "name": name,
        "department": department,
        "gpa": gpa
    })
    save_data(students)
    print(f"Student {name} added successfully!")

def view_students():
    students = load_data()
    if not students:
        print("\nNo students found!")
        return
    print("\n--- All Students List ---")
    print(f"{'ID':<10} {'Name':<20} {'Dept':<15} {'GPA'}")
    print("-"*50)
    for s in students:
        print(f"{s['id']:<10} {s['name']:<20} {s['department']:<15} {s['gpa']}")

def search_student():
    students = load_data()
    sid = input("\nSearch by ID: ")
    for s in students:
        if s['id'] == sid:
            print(f"\nFound: {s}")
            return
    print("Student not found!")

def delete_student():
    students = load_data()
    sid = input("\nEnter ID to delete: ")
    new_list = [s for s in students if s['id'] != sid]
    if len(new_list) == len(students):
        print("ID not found!")
    else:
        save_data(new_list)
        print("Student deleted successfully!")

def update_student():
    students = load_data()
    sid = input("\nEnter ID to update: ")
    for s in students:
        if s['id'] == sid:
            s['name'] = input(f"New Name ({s['name']}): ") or s['name']
            s['gpa'] = input(f"New GPA ({s['gpa']}): ") or s['gpa']
            save_data(students)
            print("Updated!")
            return
    print("Student not found!")

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Choose (1-6): ")

        if choice == '1': add_student()
        elif choice == '2': view_students()
        elif choice == '3': search_student()
        elif choice == '4': update_student()
        elif choice == '5': delete_student()
        elif choice == '6': 
            print("Allah Hafiz! - Neelam Wassan")
            break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()
