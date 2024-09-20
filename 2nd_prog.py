import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title('To Do List')
app.geometry('350x450')
app.config(bg='black')

font1 = ('Arial', 30, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 10, 'bold')

# Corrected: width and height passed during CTkFrame creation
tasks_frame = customtkinter.CTkFrame(app, fg_color='black', width=310, height=270)
tasks_frame.place(x=20, y=160)


def add_task():
    task = task_entry.get()
    if task:
        add_task_to_frame(task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showerror('error', 'Enter a task')


def remove_task(task_frame, task_text):
    task_frame.destroy()
    save_tasks()


def add_task_to_frame(task_text):
    task_frame = Frame(tasks_frame, bg='black')
    task_frame.pack(fill='x', pady=5)

    task_label = Label(task_frame, text=task_text, font=font3, bg='black', fg='white')
    task_label.pack(side=LEFT, padx=10)

    remove_button = Button(task_frame, text='X', font=font3, bg='red', fg='white',
                           command=lambda: remove_task(task_frame, task_text))
    remove_button.pack(side=RIGHT, padx=10)


def save_tasks():
    tasks = [frame.winfo_children()[0].cget("text") for frame in tasks_frame.winfo_children()]
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                add_task_to_frame(task.strip())
    except FileNotFoundError:
        pass


title_label = customtkinter.CTkLabel(app, font=font1, text='To Do List', text_color="red", bg_color="black")
title_label.place(x=100, y=20)

add_button = customtkinter.CTkButton(app, font=font2, command=add_task, text='Add Task', fg_color='red')
add_button.place(x=40, y=80)

task_entry = customtkinter.CTkEntry(app, font=font3, fg_color='blue', width=280)
task_entry.place(x=40, y=120)

load_tasks()
app.mainloop()
