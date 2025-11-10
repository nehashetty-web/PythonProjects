students = []   # empty list to store student data

while True:
    print("\n------ Student Management System ------")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Add Student
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        students.append({"roll": roll, "name": name, "marks": marks})
        print("✅ Student added successfully!")

    elif choice == 2:
        # Update Student
        roll = int(input("Enter roll number to update: "))
        for s in students:
            if s["roll"] == roll:
                s["marks"] = int(input("Enter new marks: "))
                print("✅ Updated!")
                break
        else:
            print("❌ Student not found.")

    elif choice == 3:
        # Delete Student
        roll = int(input("Enter roll number to delete: "))
        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                print("🗑️ Deleted successfully!")
                break
        else:
            print("❌ Student not found.")

    elif choice == 4:
        # Search Student
        roll = int(input("Enter roll number to search: "))
        for s in students:
            if s["roll"] == roll:
                print(f"Name: {s['name']}, Marks: {s['marks']}")
                break
        else:
            print("❌ Student not found.")

    elif choice == 5:
        # Display All Students
        if students:
            print("\n📋 Student Records:")
            for s in students:
                print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")
        else:
            print("No records found.")

    elif choice == 6:
        print("👋 Exiting... Thank you!")
        break

    else:
        print("❌ Invalid choice! Try again.")
