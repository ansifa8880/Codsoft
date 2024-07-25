# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:46:18 2024

@author: ALEEM BAIG
"""

import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.task_list = tk.Listbox(self.root, width=40)
        self.task_list.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        self.task_list.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)

    def update_task(self):
        task_num = int(self.task_list.curselection()[0])
        new_task = self.task_entry.get()
        self.task_list.delete(task_num)
        self.task_list.insert(task_num, new_task)
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        task_num = int(self.task_list.curselection()[0])
        self.task_list.delete(task_num)

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()