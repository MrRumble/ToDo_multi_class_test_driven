from lib.todo import *

class TodoList():
    def __init__(self):
        self.tasks_todo = []

    def add(self, todo):
        if type(todo) is not Todo:
            raise Exception('TodoList.add() only accepts ToDo object as a parameter.')
        self.tasks_todo.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        if len(self.tasks_todo) == 0:
            return 'All tasks have been completed!'  
        incomplete_tasks = []
        for task in self.tasks_todo:
            if task.is_task_complete == False:
                incomplete_tasks.append(task)
        return incomplete_tasks

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete


        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass