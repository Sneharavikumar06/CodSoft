import tkinter as tk
from tkinter import messagebox
import json
import os

TODO_FILE = 'todo.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = load_tasks()
        
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(fill=tk.BOTH, expand=1)
        self.load_task_listbox()
        
        self.entry = tk.Entry(root)
        self.entry.pack(fill=tk.X, padx=5, pady=5)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_completed)
        self.complete_button.pack(side=tk.LEFT, padx=5, pady=5)
    
    def load_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            self.task_listbox.insert(tk.END, f"{task['title']} [{status}]")
    
    def add_task(self):
        title = self.entry.get()
        if title:
            self.tasks.append({"title": title, "completed": False})
            save_tasks(self.tasks)
            self.load_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task title cannot be empty.")
    
    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            title = self.entry.get()
            if title:
                self.tasks[index]["title"] = title
                save_tasks(self.tasks)
                self.load_task_listbox()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Task title cannot be empty.")
        else:
            messagebox.showwarning("Selection Error", "No task selected.")
    
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks.pop(index)
            save_tasks(self.tasks)
            self.load_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected.")
    
    def mark_task_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = True
            save_tasks(self.tasks)
            self.load_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
