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


def test_complete_tasks_return_one_complete_task():
    todo_list = TodoList()
    todo = Todo('Task to complete')
    todo_list.add(todo)
    todo.mark_complete()
    result = todo_list.complete()
    assert result == [todo]


def test_complete_tasks_return_three_complete_tasks():
    todo_list = TodoList()
    todo1 = Todo('Task to complete')
    todo2 = Todo('Task to complete 2')
    todo3 = Todo('Task to complete 3')
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo1.mark_complete()
    todo2.mark_complete()
    todo3.mark_complete()
    result = todo_list.complete()
    assert result == [todo1, todo2, todo3]

def test_give_up_marks_one_task_complete():
    todo_list = TodoList()
    todo1 = Todo('Task tp complete')
    todo_list.add(todo1)
    todo_list.give_up()
    result = todo1.is_task_complete
    assert result == True

def test_give_up_marks_two_tasks_complete():
    todo_list = TodoList()
    todo1 = Todo('Task tp complete')
    todo2 = Todo('Task tp complete')
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    result = todo1.is_task_complete and todo2.is_task_complete
    assert result == True
