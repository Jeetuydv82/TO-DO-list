# 📝 To-Do List Application (Python CLI)

A simple **Command-Line Based To-Do List App** built in **Python**. This app helps you manage your daily tasks by allowing you to add, view, complete, and delete tasks easily.

---

## 🚀 Features

- ✅ Add new tasks with optional description and due date
- 📄 View all tasks with status (completed or pending)
- ✔️ Mark tasks as completed
- 🗑️ Delete tasks
- 💾 Tasks are saved in a JSON file for persistence
- 🖥️ Simple command-line interface

---

## 📁 Project Structure

todo_app/
├── todo.py # Main Python script
├── tasks.json # JSON file to store tasks

yaml
Copy
Edit

---

## ⚙️ Requirements

- Python 3.x

---

## 💡 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/todo-list-cli.git
   cd todo-list-cli
Create an empty tasks.json file (if not already present):

bash
Copy
Edit
echo [] > tasks.json   # Linux/macOS
type nul > tasks.json  # Windows
Run the app

bash
Copy
Edit
python todo.py
Or, if you use Python 3:

bash
Copy
Edit
python3 todo.py
📸 Sample Output
mathematica
Copy
Edit
--- To-Do List Menu ---
1. Add Task
2. Show Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
Enter your choice:
🛠 Future Improvements
GUI version using Tkinter

Priority-based sorting

Notifications/reminders

Export to PDF or CSV

User login system

🧑‍💻 Author
Jeetu Yadav
