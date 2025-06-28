from datetime import datetime 

exams = []

def add_exam(): 
    print("\n ➕ADD EXAMS")
    name  = input("📝Enter subject: ")
    date = input("📅 Enter Date (MM-DD-YYYY): ").strip()
    time = input("⏰ Enter time HH:MM: ").strip()
    room = input("🏫 Enter your assigned room: ")

    for exam in exams: 
        if exam["date"] == date and exam["time"] == time:
            print(f"❌CONFLICT!!! '{exam['name']} is already scheduled on {date} at {time}.")
            return
        
    exams.append({
        "name" : name, 
        "date" : date, 
        "time" : time, 
        "room" : room
        })
    print("✅ Exam added succesfully!")

def view_exam():
    if not exams:
        print("\n😴 No exams scheduled.\n")
        return

    print("\n📋 SCHEDULED EXAMS (Sorted):")

    def exam_key(exam):
        try:
            return datetime.strptime(exam["date"] + " " + exam["time"], "%m-%d-%Y %I:%M %p")
        except ValueError:
            return datetime.max 

    sorted_exams = sorted(exams, key=exam_key)

    for i, exam in enumerate(sorted_exams, start=1):
        print(f"{i}. 📘 {exam['name']} — {exam['date']} at {exam['time']} in Room {exam['room']}")
    print()

def edit_exam():
    if not exams:
        print("No exams to edit.\n")
        return

    view_exam()

    try:
        choice = int(input("Enter the number of the exam to edit: "))
        if (1 <= choice) and (choice <= len(exams)):

            exam = exams[choice - 1]

            print("Leave blank to keep the current value.\n")

            new_name = input(f"name ({exam['name']}): ")
            new_date = input(f"Date ({exam['date']}): ")
            new_time = input(f"Time ({exam['time']}): ")
            new_room = input(f"Room ({exam['room']}): ")

            # Use the new value if provided, otherwise keep the old one
            name = new_name if new_name else exam['name']
            date = new_date if new_date else exam['date']
            time = new_time if new_time else exam['time']
            room = new_room if new_room else exam['room']

            # Check for conflicts (excluding itself)
            for i in range(len(exams)):
                if i != choice - 1 and exams[i]["date"] == date and exams[i]["time"] == time:
                    print("Conflict: another exam is already scheduled at that time.\n")
                    return

            # Update the exam
            exams[choice - 1] = {
                "name": name,
                "date": date,
                "time": time,
                "room": room
            }

            print("Exam updated successfully.\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_exam():
    print("🗑️ DELETE EXAM SCHEDULE")
    if not exams:
        print("No exams to delete.")
        return
    
    view_exam()

    try:
        choice = int(input("Enter the number of exam you want to delete: "))
        if 1 <= choice <= len(exams):
            removed = exams.pop(choice - 1)
            print(f"'{removed['name']}' has been deleted.")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main_menu():
    while True:
        print("📚SMART SCHEDULER\n")
        print("Welcome smart scheduler! What do you want to do today? ")
        print("1. Add Exam")
        print("2. View Exam")
        print("3. Edit Exam")
        print("4. Delete Exam")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_exam()
        elif choice == "2":
            view_exam()
        elif choice == "3":
            edit_exam()
        elif choice == "4": 
            delete_exam()
        elif choice == "5":
            print("👋Good bye!")
            print("Created by: \n")
            print("- Capili, Catherina A.")
            print("- Capuras, Joanna Margarier V.")
            print("- Esplago, Stephaney Rae O.")
            break
        else:
            print("❌ Invalid choice! Please try again. ")

main_menu()