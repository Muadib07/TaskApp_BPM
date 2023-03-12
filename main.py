from datetime import datetime
from tkinter import *
import sqlite3

root = Tk()
root.title('TaskApp BPM')
root.geometry("800x800")

def create_db():
    database_conn = sqlite3.connect('tasks.db')
    c = database_conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tasks
            (title TEXT, description TEXT, deadline INT)""")
    database_conn.close()
def fetch_db():
    database_conn = sqlite3.connect('tasks.db')
    c = database_conn.cursor()
    c.execute("SELECT * FROM tasks;")
    tasks = c.fetchall()

    print_tasks = ''
    for task in tasks:
        print_tasks += str(task) + '\n'

    query_label = Label(root, text=print_tasks)
    query_label.grid(row=1, column=2, columnspan=2, rowspan=5)

    database_conn.close()

def pre_process_db():
    return 0



def submit_task():
    database_conn = sqlite3.connect('tasks.db')
    title_value = title.get()
    description_value = description.get()
    deadline_value = deadline.get()
    print(title_value)
    print(description_value)
    print(deadline_value)
    data_insert_query = '''INSERT INTO tasks (title, description, deadline) VALUES (?, ?, ?)'''
    data_insert_tuple = (title_value, description_value, deadline_value)
    c = database_conn.cursor()
    c.execute(data_insert_query, data_insert_tuple)
    database_conn.commit()
    database_conn.close()

    #clear text boxes
    title.delete(0, END)
    description.delete(0, END)
    deadline.delete(0, END)



#Text boxes
title = Entry(root, width=30)
title.grid(row=1, column=1, padx=20)
description = Entry(root, width=30)
description.grid(row=2, column=1, padx=20)
deadline = Entry(root, width=30)
deadline.grid(row=3, column=1, padx=20)

#Text box labels
main_label = Label(root, text="ADD TASK HERE")
main_label.grid(row=0, column=0, columnspan=2)
title_label = Label(root, text="Title")
title_label.grid(row=1, column=0)
description_label = Label(root, text="Description")
description_label.grid(row=2, column=0)
deadline_label = Label(root, text="Deadline")
deadline_label.grid(row=3, column=0)

#Submit Button
submit_btn = Button(root, text="Add task", cursor="hand2", command=submit_task)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Fetch Button
fetch_btn = Button(root, text="Show tasks", cursor="hand2", command=fetch_db)
fetch_btn.grid(row=0, column=2, columnspan=2, pady=10, padx=10, ipadx=100)


create_db()
root.mainloop()












# # Function to print the data stored in the list
# def printDates(dates):
#     for i in range(len(dates)):
#         print(dates[i])
#
#
# if __name__ == "__main__":
#     dates = ["23 Jun 2018", "2 Dec 2017", "11 Jun 2018",
#              "01 Jan 2019", "10 Jul 2016", "01 Jan 2007"]
#
#
# class Task:
#     def __init__(self, title: str, description: str, deadline, completed: bool):
#         self.title = title
#         self.description = description
#         self.deadline = deadline
#         self.completed = completed
#
#     def set_data(self):
#         self.title = input("title : ")
#         self.description = input("description : ")
#         date_string = input("deadline dd-mm-rrrr : ")
#         try:
#             self.deadline = datetime.strptime(date_string, "%d-%m-%Y")
#         except ValueError:
#             print("Invalid date format. Please enter the deadline date in the format dd-mm-yyyy.")
#             self.set_data()
#
#         self.completed = False
#
#     def change_status(self):
#         change = int(input(" task complete : 1 | task incomplete : 0 "))
#         if change == 1:
#             self.completed = True
#             return self.completed
#         elif change == 0:
#             self.completed = False
#             return self.completed
#         else:
#             print("Invalid date format. Please enter 1 or 0.")
#             self.change_status()
#
#     def show_data(self):
#         print("{} | {} | {} | {}".format(self.title, self.description, self.deadline, self.completed))
#
#
# class TaskList:
#     def __init__(self):
#         self.tasks_list = []
#
#     def add_task(self, task: Task):
#         return self.tasks_list.append(task)
#
#     def get_task(self, title: str):
#         for t in self.tasks_list:
#             if t.title == title:
#                 return t.title, t.description, t.deadline, t.completed
#         return "No such task found"
#
#     #     watcher = len(self.tasks) - 1
#     #     i = 0
#     #     while i <= watcher:
#     #         for x in self.tasks:
#     #             if task == self.tasks[i]:
#     #                 return task
#     #             else:
#     #                 i += 1
#
#     def remove_task(self, task):
#         return self.tasks_list.remove(task)
#
#     def show_tasks(self):
#         for task in self.tasks_list:
#             task.show_data()
#
#     def get_completed_tasks(self):
#         task_completed_list = ""
#         for t in self.tasks_list:
#             if t.completed == True:
#                 t.show_data()
#         #         task_completed_list += str(t) + "\n"
#         # return task_completed_list
#
#     def get_incompleted_tasks(self):
#         for t in self.tasks_list:
#             if t.completed == False:
#                 t.show_data()
#
#     def __str__(self):
#         task_list_str = ""
#         for task in self.tasks_list:
#             task_list_str += str(task) + "\n"
#         return task_list_str
#
#     def get_tasks_due_today(self):
#         pass
#
#     def get_tasks_due_tomorrow(self):
#         pass
#
#     def get_tasks_due_in_next_week(self):
#         pass
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     task_1 = Task("Test task", "Test description", '21-02-1997', True)
#     task_2 = Task("2", "Test sad", '21-02-1994', False)
#     task_4 = Task("dsad task", "Test sad", '20-02-1994', True)
#     task_5 = Task("Test dsa", "Test dsa", '21-02-1994', False)
#     # task.set_data()
#     # task.show_data()
#     # task_1.change_status()
#
#     list_a = TaskList()
#
#     list_a.add_task(task_1)
#     list_a.add_task(task_2)
#     list_a.add_task(task_4)
#     list_a.add_task(task_5)
#
#     # TaskList.get_task(task_1)
#     task_found = list_a.get_task("Test task")
#     print(str(task_found))
