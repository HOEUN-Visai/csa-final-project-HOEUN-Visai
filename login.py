import customtkinter as ctk
import tkinter.messagebox as tkmb
from tkinter import *


# Selecting GUI theme
ctk.set_appearance_mode("dark")

# Selecting color theme
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Login Page")


def login():

    username = "Visai"
    password = "12345"

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful",
                      message="You have logged in Successfully!!")
        app.destroy()  # Close the login window
        # root.destroy()
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong password',
                         message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong username',
                         message='Please check your username')
    else:
        tkmb.showerror(title="Login Failed",
                       message="Invalid Username and password")


label = ctk.CTkLabel(app, text="Welcome, This is Login System Page")

label.pack(pady=20)


frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Login to Start Code4U!')
label.pack(pady=12, padx=10)


user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)


button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)


app.mainloop()
