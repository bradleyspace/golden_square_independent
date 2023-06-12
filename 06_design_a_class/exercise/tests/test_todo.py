import pytest
import random
from lib.todo import TodoList, TodoNotFound
import string

LOWERCASE_LETTERS = string.ascii_letters

def test_add_todo():
    instance = TodoList()
    _id = instance.create("My Todo!")

    assert "My Todo!" == instance.get_by_id(_id)


def test_multiple():
    instance = TodoList()

    strings = ["".join(random.choices(LOWERCASE_LETTERS, k=7)) for i in range(15)]

    expected_items = []

    for string in strings:
        _id = instance.create(string)
        expected_items.append((_id, string))

    assert instance.get_all() == expected_items

def test_delete():
    instance = TodoList() 
    name = "My Super Short Todo!"
    _id = instance.create(name)

    instance.delete(_id)

    all_todos = instance.get_all()
    assert (_id, name) not in all_todos

