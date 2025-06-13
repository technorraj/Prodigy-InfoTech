# Password Complexity Checker

This Python program helps users evaluate the strength of their passwords by checking key security criteria. It provides real-time feedback on password quality and educates users with helpful tips on creating strong and secure passwords.

The project uses only Python's built-in libraries and was developed as part of an internship at **The Prodigy Infotech**, demonstrating a practical and educational approach to password validation.

## Features

- **Password Strength Assessment:**
  - Verifies presence of:
    - Uppercase letters
    - Lowercase letters
    - Numbers
    - Special characters
    - Minimum length (8 characters)
    
- **Feedback on Password Strength:**
  - Ranks the password as:
    - Very Strong (5/5 criteria met)
    - Strong (4/5 criteria met)
    - Moderate (3/5 criteria met)
    - Weak (Less than 3 criteria met)

- **Password Masking:**
  - Partially masks the input password for privacy when displaying it back to the user.

- **Security Tips:**
  - Displays 10 essential tips for creating and maintaining strong passwords.


## Requirements

- Python 3.x
- No external libraries needed (uses `re` for regex)


## Usage

1. **Run the Program:**
   - Execute the script using Python:

2. **Review Tips:**
   - The program will display helpful guidelines for secure password creation.

3. **Enter Your Password:**
   - Type your password (it will be shown in plain text as you type).

4. **View the Feedback:**
   - See your masked password
   - Get a strength rating and criteria breakdown
