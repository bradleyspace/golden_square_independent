from .todo import Todo

class TodoList:
    def __init__(self):
        self._items = []

    def add(self, todo: Todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self._items.append(todo)
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return list(filter(lambda x: x.complete is False, self._items))

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return list(filter(lambda x: x.complete == True, self._items))

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for item in self._items:
            item.mark_complete()