import tkinter as tk
from tkinter import ttk, messagebox
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
        self.root.geometry("400x400")
        
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.style.configure("TFrame", background="#ffffff")  # White background for frames
        self.style.configure("TLabel", background="#ffffff", font=("Helvetica", 12))
        self.style.configure("TEntry", font=("Helvetica", 12))
        
        self.style.configure("TButton", 
                             background="#ffcc99",  # Light orange background
                             foreground="#000000",  # Black text
                             font=("Helvetica", 10), 
                             padding=10)
        self.style.map("TButton", 
                       background=[("active", "#ff9966")],  # Darker orange on hover
                       foreground=[("active", "#ffffff")])  # White text on hover

        self.tasks = load_tasks()
        
        self.frame = ttk.Frame(root, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.task_listbox = tk.Listbox(self.frame, 
                                       selectmode=tk.SINGLE, 
                                       height=10, 
                                       font=("Helvetica", 12), 
                                       bg="#ffffcc",  # Light yellow background
                                       fg="#000000")  # Black text
        self.task_listbox.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(0, 10))
        
        self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.load_task_listbox()
        
        self.entry = ttk.Entry(self.frame)
        self.entry.pack(fill=tk.X, padx=5, pady=(5, 10))
        
        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.pack(fill=tk.X, padx=5, pady=(0, 10))
        
        self.add_button = ttk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)
        
        self.update_button = ttk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_button = ttk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        
        self.complete_button = ttk.Button(self.button_frame, text="Mark as Completed", command=self.mark_task_completed)
        self.complete_button.pack(side=tk.LEFT, padx=5)
    
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

