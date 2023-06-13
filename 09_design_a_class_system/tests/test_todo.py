from lib import Todo

def test_mark_complete():
    todo = Todo("This is a unit test!")

    before_state = todo.complete

    todo.mark_complete()
    after_state = todo.complete

    assert before_state == False
    assert after_state == True