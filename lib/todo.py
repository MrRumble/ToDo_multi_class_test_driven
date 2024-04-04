class Todo:
    def __init__(self, task):
        if type(task) is not str:
            raise Exception('Task entry must be a string!') 
        self.task = task
        self.is_task_complete = False
        
    def mark_complete(self):

        self.is_task_complete = True
        