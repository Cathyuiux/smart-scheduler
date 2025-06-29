 📚 Smart Exam Scheduler (CLI Version)

The Smart Exam Scheduler is a command-line Python program designed to help students or teachers manage their exam schedules efficiently. It allows you to add, view, edit, and delete exam schedules with ease while automatically checking for time conflicts.

---

✅ Features

- 📝 **Add Exams** — Input subject name, date, time, and assigned room.
- 📅 **View Schedule** — Displays a sorted list of all scheduled exams.
- ✏️ **Edit Entries** — Update exam information with optional field changes.
- 🗑️ **Delete Exams** — Remove an exam from the schedule list.
- ⏰ **Conflict Detection** — Prevents overlapping exams at the same date and time.
- 🔢 **Sorted View** — Exams are automatically sorted by date and time.
- 🎨 **User-Friendly CLI** — Emoji-enhanced, clean interface for an improved user experience.

---

⚙️ Requirements

- Python 3.6 or higher installed on your machine  
- Compatible with Windows, macOS, and Linux

---

🚀 Getting Started

 1. Clone or Download the Repository

bash
git clone https://github.com/cathyuiux/smart-exam-scheduler.git
cd smart-exam-scheduler

 2. Run the Program
   Open a terminal or command prompt and navigate to the project folder. Then run:
    bash
    python scheduler.py

3. 🧪 Program Usage
  Upon running the script, you'll be presented with a main menu:
  
  📚 SMART SCHEDULER
  
  Welcome! What would you like to do?
  1. Add Exam
  2. View Exam
  3. Edit Exam
  4. Delete Exam
  5. Exit

     ➕ Add Exam
        You will be prompted to enter:
        Subject name
        Date (MM-DD-YYYY)
        Time (HH:MM AM/PM)
        Room
        The program checks for conflicting schedules before saving.
        
      📋 View Exam
          Displays a list of scheduled exams sorted by date and time, including:
          Subject
          Date
          Time
          Room
     
      ✏️ Edit Exam
          You can update any of the fields for an existing exam. Leave a field blank to keep the current value. The program ensures that any changes do not conflict with other entries.

       🗑️ Delete Exam
           Choose an exam by its number from the list to delete it.

     🚪 Exit
        Exits the program with a farewell message and credits.


💡 Sample Output
    1. 📘 Math — 06-20-2025 at 08:00 AM in Room A1
    2. 📘 Science — 06-21-2025 at 09:30 AM in Room B2

👩‍💻 Authors

Created with care by:
  Capili, Catherina A.
  Capuras, Joanna Margariet V.
  Esplago, Stephaney Rae O.
