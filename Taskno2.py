
import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result.set(eval(expression.get()))
    except Exception as e:
        result.set("Error")

# Function to clear the expression
def clear_expression():
    expression.set("")
    result.set("")

# Function to append operators and operands to the expression
def append_to_expression(value):
    expression.set(expression.get() + str(value))

# Main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#F0F0F0")  # Set background color

# Variables
expression = tk.StringVar()
result = tk.StringVar()

# Entry for displaying the expression and result
entry_expression = tk.Entry(root, textvariable=expression, font=("Arial", 14), bd=10, insertwidth=4, width=20, justify="right")
entry_result = tk.Entry(root, textvariable=result, font=("Arial", 14), bd=10, insertwidth=4, width=10, justify="right")

# Buttons
buttons = [
    ("7", lambda: append_to_expression(7)),
    ("8", lambda: append_to_expression(8)),
    ("9", lambda: append_to_expression(9)),
    ("/", lambda: append_to_expression("/")),
    ("4", lambda: append_to_expression(4)),
    ("5", lambda: append_to_expression(5)),
    ("6", lambda: append_to_expression(6)),
    ("*", lambda: append_to_expression("*")),
    ("1", lambda: append_to_expression(1)),
    ("2", lambda: append_to_expression(2)),
    ("3", lambda: append_to_expression(3)),
    ("-", lambda: append_to_expression("-")),
    ("C", clear_expression),
    ("0", lambda: append_to_expression(0)),
    (".", lambda: append_to_expression(".")),
    ("+", lambda: append_to_expression("+")),
    ("=", evaluate_expression)
]

# Layout
row = 1
col = 0
for text, command in buttons:
    button = tk.Button(root, text=text, font=("Arial", 14), padx=20, pady=10, command=command, bg="#D3D3D3")  # Set button color
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

entry_expression.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")  # Center-align entry
entry_result.grid(row=0, column=4, columnspan=2, padx=10, pady=10, sticky="ew")  # Center-align entry

# Center the window on the screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x_offset = (root.winfo_screenwidth() - width) // 2
y_offset = (root.winfo_screenheight() - height) // 2
root.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

root.mainloop()
