from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_password(password):
    cipher = Fernet(load_key())
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    cipher = Fernet(load_key())
    return cipher.decrypt(encrypted_password.encode()).decode()
