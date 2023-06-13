from .todo import TodoList, Todo
from .diary import Diary, DiaryEntry

class User:
    
    def __init__(self, diary: Diary, todo_list: TodoList) -> None:
        self.diary = diary
        self.todo_list = todo_list