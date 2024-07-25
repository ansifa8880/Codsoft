import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, complexity):
    if complexity == "Weak":
        characters = string.ascii_lowercase
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def submit():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    password = generate_password(length, complexity)
    password_label.config(text="Generated Password: " + password)

root = tk.Tk()
root.title("Password Generator")
root.configure(background='black')  # Set background color to black

length_label = tk.Label(root, text="Enter password length:", fg="green", bg="black", font=("Helvetica", 12))
length_label.pack()

length_entry = tk.Entry(root, fg="green", bg="black", font=("Helvetica", 12), width=60)  # Increased width to 20
length_entry.pack()

complexity_label = tk.Label(root, text="Select password complexity:", fg="green", bg="black", font=("Helvetica", 12))
complexity_label.pack()

complexity_var = tk.StringVar()
complexity_var.set("Weak")

weak_radio = tk.Radiobutton(root, text="Weak", variable=complexity_var, value="Weak", fg="green", bg="black", font=("Helvetica", 12))
weak_radio.pack()

medium_radio = tk.Radiobutton(root, text="Medium", variable=complexity_var, value="Medium", fg="green", bg="black", font=("Helvetica", 12))
medium_radio.pack()

strong_radio = tk.Radiobutton(root, text="Strong", variable=complexity_var, value="Strong", fg="green", bg="black", font=("Helvetica", 12))
strong_radio.pack()

submit_button = tk.Button(root, text="Generate Password", command=submit, fg="green", bg="black", font=("Helvetica", 12))
submit_button.pack()

password_label = tk.Label(root, text="Generated Password: ", fg="green", bg="black", font=("Helvetica", 12), wraplength=1000)  # Added wraplength to 400
password_label.pack()

root.mainloop()