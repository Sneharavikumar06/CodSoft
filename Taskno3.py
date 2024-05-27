import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    if complexity == "Low":
        chars = string.ascii_letters + string.digits
    elif complexity == "Medium":
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

    password = ''.join(random.choice(chars) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Configure window size and background color
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Label for password length
length_label = tk.Label(root, text="Password Length:", bg="#f0f0f0", font=("Helvetica", 28))
length_label.pack()

# Entry for password length
length_entry = tk.Entry(root, font=("Helvetica", 28))
length_entry.pack()

# Label for complexity
complexity_label = tk.Label(root, text="Complexity:", bg="#f0f0f0", font=("Helvetica", 28))
complexity_label.pack()

# Radio buttons for complexity
complexity_var = tk.StringVar()
complexity_var.set("Low")
low_radio = tk.Radiobutton(root, text="Low", variable=complexity_var, value="Low", bg="#f0f0f0", font=("Helvetica", 28))
medium_radio = tk.Radiobutton(root, text="Medium", variable=complexity_var, value="Medium", bg="#f0f0f0", font=("Helvetica", 28))
high_radio = tk.Radiobutton(root, text="High", variable=complexity_var, value="High", bg="#f0f0f0", font=("Helvetica", 28))

low_radio.pack()
medium_radio.pack()
high_radio.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Helvetica", 28))
generate_button.pack(pady=10)

# Label to display generated password
password_label = tk.Label(root, text="", bg="#f0f0f0", font=("Helvetica", 14), wraplength=300)
password_label.pack()

# Run the main loop
root.mainloop()