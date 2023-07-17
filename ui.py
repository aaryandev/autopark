from tkinter import Tk, Button, messagebox
import subprocess

def run_program():
    subprocess.Popen(["g++", "main.cpp", "-o", "auto_park"], shell=False)
    subprocess.Popen(["./auto_park"], shell=False)

def open_file():
    subprocess.Popen(["open", "-t", "main.cpp"], shell=False)

def show_about():
    messagebox.showinfo("About", "Auto Park\nDeveloped by Aaryan Rawat")

root = Tk()
root.title("Auto Park")
root.geometry("300x200")

btn_run = Button(root, text="Run Program", command=run_program)
btn_run.pack(pady=10)

btn_file = Button(root, text="Open Source Code", command=open_file)
btn_file.pack(pady=10)

btn_about = Button(root, text="About", command=show_about)
btn_about.pack(pady=10)

root.mainloop()
