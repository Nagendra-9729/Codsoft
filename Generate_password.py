import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length, include_numbers=True):
    characters = string.ascii_letters + (string.digits if include_numbers else '') + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        include_numbers = numbers_var.get()
        password = generate_password(length, include_numbers)
        password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        password_label.config(text="Please enter a valid length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and configure widgets with themed styles
style = ttk.Style()
style.configure("TLabel", foreground="blue")
style.configure("TButton", foreground="green")
style.configure("TCheckbutton", foreground="purple")

length_label = ttk.Label(window, text="Enter Password Length:")
length_entry = ttk.Entry(window)
include_numbers_label = ttk.Label(window, text="Include Numbers:")
numbers_var = tk.BooleanVar()
numbers_checkbox = ttk.Checkbutton(window, variable=numbers_var, onvalue=True, offvalue=False)
generate_button = ttk.Button(window, text="Generate Password", command=generate_and_display_password)
password_label = ttk.Label(window, text="Generated Password will appear here", wraplength=300)

# Place widgets in the window
length_label.pack(pady=10)
length_entry.pack()
include_numbers_label.pack()
numbers_checkbox.pack()
generate_button.pack(pady=10)
password_label.pack(padx=20, pady=10)

# Start the GUI event loop
window.mainloop()
