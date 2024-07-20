from cryptography.fernet import Fernet, InvalidToken  
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_key():
    key = Fernet.generate_key()
    with open("Secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("Secret.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except InvalidToken:
            messagebox.showerror("Error", "Invalid key")
            return
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def encrypt_file():
    filename = filedialog.askopenfilename()
    if filename:
        generate_key()
        key = load_key()
        encrypt(filename, key)
        messagebox.showinfo("Success", "File Encrypted Successfully!")

def decrypt_file():
    filename = filedialog.askopenfilename()
    if filename:
        key = load_key()
        decrypt(filename, key)
        messagebox.showinfo("Success", "File Decrypted Successfully!")

def create_gui():
    root = tk.Tk()
    root.title("File Encryptor/Decryptor")
    root.geometry("400x300")  

    frame = tk.Frame(root,pady=20)
    frame.pack(expand=True)

    encrypt_button = tk.Button(frame, text="Encrypt File", command=encrypt_file, width=20, height=2, bg="green", fg="white")
    encrypt_button.pack(pady=10)

    decrypt_button = tk.Button(frame, text="Decrypt File", command=decrypt_file, width=20, height=2, bg="red", fg="white")
    decrypt_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
