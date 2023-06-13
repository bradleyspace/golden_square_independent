from lib import User, Diary, DiaryEntry, TodoList, Todo

def test_init():

    diary = Diary()
    todo_list = TodoList()
    user = User(diary, todo_list)

    todo = Todo("Complete this integration test!")
    user.todo_list.add(todo)

    diary_entry = DiaryEntry("My Diary Entry", "This is so cool!")
    user.diary.add(diary_entry)

    assert todo in user.todo_list.incomplete()
    assert user.diary == diary
    assert user.todo_list == todo_list
    assert user.diary.count_words() == 4
    assert diary_entry in user.diary.all()
