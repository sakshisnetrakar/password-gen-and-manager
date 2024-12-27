# password-gen-and-manager

# Password Generator and Manager

A Python application to generate secure random passwords with customizable options for length and complexity. It features a simple Tkinter GUI for easy password generation, copying, and saving.

## Features

- **Customizable Length**: Specify the password length (must be at least 4 characters).
- **Complexity Levels**: Choose from:
  - **Easy**: Letters only (A-Z, a-z)
  - **Medium**: Letters and numbers (A-Z, a-z, 0-9)
  - **Hard**: Letters, numbers, and special characters (A-Z, a-z, 0-9, !@#$%^&*)
- **Copy to Clipboard**: Copy the generated password with one click.
- **Save to File**: Passwords are saved to `SavedPasswords.txt` on the Desktop.
- **Open Directory**: After saving, the Desktop folder is opened automatically.

## Technologies Used

- **Python** and **Tkinter** for GUI.
- **OS** and **Subprocess** modules for file operations.

## Installation

1. Clone or download the project.
2. Run the script:
   ```bash
   python password_generator.py

## File Details 
- SavedPasswords.txt: Stored on the Desktop with each generated password on a new line.
