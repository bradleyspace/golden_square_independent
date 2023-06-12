import pytest
from lib.todo import TodoList, TodoNotFound

def test_add_todo():
    instance = TodoList()
    _id = instance.create("My Todo!")

    assert "My Todo!" == instance.get_by_id(_id)

