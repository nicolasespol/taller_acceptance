class Task:
    def __init__(self, description, status='Pending'):
        self.description = description
        self.status = status

    def __str__(self):
        return f'{self.description} ({self.status})'

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def mark_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = 'Completed'

    def remove_task(self, description):
        self.tasks = [task for task in self.tasks if task.description != description]

    def clear_list(self):
        self.tasks = []

if __name__ == '__main__':
    todo_list = ToDoList()
    todo_list.add_task('Buy groceries')
    todo_list.add_task('Pay bills')
    todo_list.list_tasks()
    todo_list.mark_completed('Buy groceries')
    todo_list.list_tasks()
    todo_list.remove_task('Buy groceries')
    todo_list.list_tasks()
    todo_list.clear_list()
    todo_list.list_tasks()
