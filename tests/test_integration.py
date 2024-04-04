from lib.todo import *
from lib.todo_list import *
import pytest

def test_task_is_added_to_todo_list():
    todo_list = TodoList()
    todo = Todo('Task to complete')
    todo_list.add(todo)
    assert todo_list.tasks_todo == [todo]

def test_add_task_raise_exception_if_not_todo_object():
    todo_list = TodoList()
    not_todo_object = "This is a string"
    with pytest.raises(Exception) as e:
        todo_list.add(not_todo_object)
    error_message = str(e.value)
    assert error_message == 'TodoList.add() only accepts ToDo object as a parameter.'

def test_add_task_adds_two_tasks():
    todo_list = TodoList()
    todo = Todo('Task to complete')
    todo2 = Todo('Another task.')
    todo_list.add(todo)
    todo_list.add(todo2)
    assert todo_list.tasks_todo == [todo, todo2]

def test_return_incomplete_tasks_with_two_todos_incomplete():
    todo_list = TodoList()
    todo = Todo('Task to complete')
    todo2 = Todo('Another task.')
    todo_list.add(todo)
    todo_list.add(todo2)
    result = todo_list.incomplete()
    assert result == [todo, todo2]  

def test_return_incomplete_tasks_with_two_todos_one_incomplete():
    todo_list = TodoList()
    todo = Todo('Task to complete')
    todo2 = Todo('Another task.')
    todo_list.add(todo)
    todo_list.add(todo2)
    todo.mark_complete()
    result = todo_list.incomplete()
    assert result == [todo2]  

def test_return_message_with_none_incomplete():
    todo_list = TodoList()
    todo = Todo('Task to complete')
    todo2 = Todo('Another task.')
    todo_list.add(todo)
    todo_list.add(todo2) ###### I GAVE UP HERE
    todo.mark_complete()
    todo2.mark_complete()
    result = todo_list.incomplete()
    assert result == 'All tasks have been completed!'  