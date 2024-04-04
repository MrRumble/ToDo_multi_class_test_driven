from lib.todo_list import *

def test_todo_list_initialised_with_empty_list():
    todo_list = TodoList()
    assert todo_list.tasks_todo == []