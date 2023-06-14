import string
import random
from lib import Todo, TodoList

ASCII_LOWERCASE = string.ascii_lowercase

def test_add():
    todo_list = TodoList()

    todo = Todo("Complete the challenge for 08!")
    todo_list.add(todo)

    assert todo_list.incomplete()[0] == todo

def test_is_complete():
    todo_list = TodoList()

    todo = Todo("Complete the challenge for 08!")
    todo_list.add(todo)
    todo.mark_complete()

    assert todo_list.complete()[0].complete is True

def test_give_up():
    todo_list = TodoList()

    for i in range(1, 10):
        k = random.randint(6, 20)
        todo = Todo(random.choices(ASCII_LOWERCASE, k=k))
        todo_list.add(todo)

    todo_list.give_up()
    
    complete_list = todo_list.complete()
    incomplete_list = todo_list.incomplete()

    assert len(complete_list) > 0
    assert len(incomplete_list) == 0

