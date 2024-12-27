import random
from tkinter import *
from tkinter import messagebox
import string
import os
import subprocess

def generate_password():
    try:
        length = int(length_var.get())
        complexity = complexity_var.get()

        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length must be at least 4.")
            return

        if complexity == "Easy":
            characters = string.ascii_letters
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits
        elif complexity == "Hard":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            messagebox.showwarning("Invalid Complexity", "Please select a valid complexity level.")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a number.")

def copy_to_clipboard():
    generated_password = password_var.get()
    if generated_password:
        # Copy to clipboard
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        root.update()

        # Save to .txt file on Desktop
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop, "SavedPasswords.txt")
        with open(file_path, "a") as file:
            file.write(f"{generated_password}\n")
        
        # Open the directory
        subprocess.Popen(f'explorer "{desktop}"', shell=True)
        
        messagebox.showinfo("Saved", f"Password copied and saved to {file_path}!")
    else:
        messagebox.showwarning("No Password", "Generate a password first!")

# Root window setup
root = Tk()
root.title("Password Generator")
root.geometry("400x400")
root.config(bg="#f2f2f2")

# Variables
password_var = StringVar()
length_var = StringVar()
complexity_var = StringVar()

# Title label
title_label = Label(
    root, text="Secure Password Generator", font=("Helvetica", 16, "bold"), bg="#f2f2f2", fg="#333"
)
title_label.pack(pady=10)

# Password length
length_label = Label(root, text="Password Length:", font=("Arial", 12), bg="#f2f2f2")
length_label.pack(pady=5)
length_entry = Entry(root, textvariable=length_var, font=("Arial", 12), width=10, justify="center")
length_entry.pack(pady=5)

# Password complexity
complexity_label = Label(root, text="Password Complexity:", font=("Arial", 12), bg="#f2f2f2")
complexity_label.pack(pady=5)

complexity_options = ["Easy", "Medium", "Hard"]
complexity_menu = OptionMenu(root, complexity_var, *complexity_options)
complexity_menu.config(font=("Arial", 12))
complexity_menu.pack(pady=5)

# Generated password display
password_entry = Entry(
    root, textvariable=password_var, font=("Courier", 14), width=30, justify="center", state="readonly"
)
password_entry.pack(pady=10)

# Generate button
generate_btn = Button(
    root, text="Generate Password", command=generate_password, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5
)
generate_btn.pack(pady=10)

# Copy button
copy_btn = Button(
    root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12, "bold"), bg="#2196F3", fg="white", padx=10, pady=5
)
copy_btn.pack(pady=10)

# Run the application
root.mainloop()
