# Secure Password Manager

A simple and secure password manager web application built with Flask, Python, and Bootstrap. The app allows users to securely store and manage their passwords, encrypting them with the **Fernet** encryption method, and supports copying passwords to the clipboard for ease of use.

## Features

- **Password Encryption**: All passwords are encrypted using the **Fernet** encryption algorithm.
- **Master Key**: A master key is required to access stored passwords, ensuring only the user can view their data.
- **Password Copy**: Users can easily copy passwords to the clipboard.
- **Responsive Design**: The app is built using **Bootstrap** for a responsive and user-friendly interface.
- **Secure Storage**: Passwords are stored securely in an SQLite database.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Encryption**: Fernet (cryptography)
- **Database**: SQLite

## Usage

### Step 1: Access the Application

When you first open the web application in your browser (http://127.0.0.1:5000), you will be prompted to **create a master key** or **verify an existing master key**. 

- **Create Master Key**: If this is your first time using the app, you need to set a **master key**. This key is used to encrypt and decrypt all stored passwords.
- **Verify Master Key**: If you already have a master key, you will need to enter it to access the stored passwords.

### Step 2: Add a New Password

Once you have created or verified the master key, you will be taken to the password management page, where you can add your passwords.

1. **Enter Website**: Type the name of the website or service you want to store the password for.
2. **Enter Username**: Enter the username or email associated with the account.
3. **Enter Password**: Type the password you want to store.
4. **Save**: Click the "Save Password" button to encrypt and securely store the password in the database.

The password will be encrypted using the **master key** and stored securely.

### Step 3: View and Copy Passwords

- **View Saved Passwords**: Once passwords are saved, you will see a list of stored websites, usernames, and their encrypted passwords.
  
  A notification (e.g., a Bootstrap Toast or an alert) will appear confirming that the password has been copied.

### Notes:
- Always keep your **master key** secure. If you lose or forget it, you won't be able to access the stored passwords.
- Passwords are encrypted and securely stored in the **SQLite** database.

