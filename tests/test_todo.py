from lib.todo import *
import pytest

def test_todo_initialised_with_self_string():
    todo = Todo('task')
    assert todo.task == 'task'

def test_todo_task_initially_set_as_false():
    todo = Todo('task')
    assert todo.is_task_complete == False

def test_mark_complete_sets_complete_property_to_true():
    todo = Todo('task')
    todo.mark_complete()
    assert todo.is_task_complete == True 

def test_task_pararmeter_gives_exception_if_not_string():
    with pytest.raises(Exception) as e:
        todo = Todo(0)
    error_message = str(e.value)
    assert error_message == 'Task entry must be a string!'


