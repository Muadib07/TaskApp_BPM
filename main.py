from datetime import datetime



def printDates(dates):
    for i in range(len(dates)):
        print(dates[i])


if __name__ == "__main__":
    dates = ["23 Jun 2018", "2 Dec 2017", "11 Jun 2018",
             "01 Jan 2019", "10 Jul 2016", "01 Jan 2007"]


class Task:
    def __init__(self, title: str, description: str, deadline, completed: bool):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = completed

    def set_data(self):
        self.title = input("title : ")
        self.description = input("description : ")
        date_string = input("deadline dd-mm-rrrr : ")
        try:
            self.deadline = datetime.strptime(date_string, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format. Please enter the deadline date in the format dd-mm-yyyy.")
            self.set_data()

        self.completed = False

    def change_status(self):
        change = int(input(" task complete : 1 | task incomplete : 0 "))
        if change == 1:
            self.completed = True
            return self.completed
        elif change == 0:
            self.completed = False
            return self.completed
        else:
            print("Invalid date format. Please enter 1 or 0.")
            self.change_status()

    def show_data(self):
        print("{} | {} | {} | {}".format(self.title, self.description, self.deadline, self.completed))

    def __repr__(self):
        return "{} | {} | {} | {}".format(self.title, self.description, self.deadline, self.completed)


class TaskList:
    def __init__(self):
        self.tasks_list = []


    def add_task(self, task: Task):
        return self.tasks_list.append(task)

    def get_task(self, title: str):
        for t in self.tasks_list:
            if t.title == title:
                return t.title, t.description, t.deadline, t.completed
        return "No such task found"

    #     watcher = len(self.tasks) - 1
    #     i = 0
    #     while i <= watcher:
    #         for x in self.tasks:
    #             if task == self.tasks[i]:
    #                 return task
    #             else:
    #                 i += 1

    def remove_task(self, task):
        return self.tasks_list.remove(task)

    def show_tasks(self):
        for task in self.tasks_list:
            task.show_data()

    def get_completed_tasks(self):
        task_completed_list = ""
        for t in self.tasks_list:
            if t.completed == True:
                t.show_data()
        #         task_completed_list += str(t) + "\n"
        # return task_completed_list

    def get_incompleted_tasks(self):
        for t in self.tasks_list:
            if t.completed == False:
                t.show_data()

    def __str__(self):
        task_list_str = ""
        for task in self.tasks_list:
            task_list_str += str(task) + "\n"
        return task_list_str

    def get_tasks_due_today(self):
        current_date_on_current_time = []
        current_datetime_date = datetime.datetime.now().date()
        for date_str in self.tasks_list:
            data = datetime.datetime.strptime(date_str.deadline, '%d-%m-%Y').date()
            if data.day == current_datetime_date.day:
                current_date_on_current_time.append(data)

        print(current_datetime_date)

    def get_tasks_due_tomorrow(self):
        pass

    def get_tasks_due_in_next_week(self):
        pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    task_1 = Task("Test task", "Test description", '21-02-1997', True)
    task_2 = Task("2", "Test sad", '21-02-1994', False)
    task_4 = Task("dsad task", "Test sad", '20-02-1994', True)
    task_5 = Task("Test dsa", "Test dsa", '21-02-1994', False)
    task_6 = Task("Test dsa", "Test dsa", '11-03-2023', False)
    # task.set_data()
    # task.show_data()
    # task_1.change_status()

    list_a = TaskList()

    list_a.add_task(task_1)
    list_a.add_task(task_2)
    list_a.add_task(task_4)
    list_a.add_task(task_5)

    # TaskList.get_task(task_1)
    task_found = list_a.get_task("Test task")

    print(TaskList.get_tasks_due_today)
